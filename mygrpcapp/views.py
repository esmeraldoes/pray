# mygrpcapp/views.py
from concurrent import futures
import grpc
from django.http import HttpResponse

from mygrpcapp import bible_pb2_grpc
from mygrpcapp.bible_service import BibleServiceServicer



# mygrpcapp/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from concurrent import futures
import grpc
from mygrpcapp import bible_pb2
from mygrpcapp import bible_pb2_grpc
from mygrpcapp.bible_service import BibleServiceServicer































from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import grpc
from mygrpcapp import bible_pb2_grpc
from mygrpcapp.bible_pb2 import (
    Empty,
    GetBooksRequest,
    GetChaptersRequest,
    GetVersesRequest,
    GetVerseRequest,
)

from .serializers import (
    EmptySerializer,
    GetBooksRequestSerializer,
    GetChaptersRequestSerializer,
    GetVersesRequestSerializer,
    GetVerseRequestSerializer,
    BibleVersionListSerializer,
    BibleBookListSerializer,
    BibleChapterListSerializer,
    BibleVerseSerializer,
)
class BibleVersionsView(APIView):
    serializer_class = BibleVersionListSerializer
    def get(self, request):
        
        try:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)
                request = Empty()
                response = stub.GetBibleVersions(request)

            # Convert the repeated field to a Python list
            versions_list = list(response.versions)

            serializer = BibleVersionListSerializer(data={'versions': versions_list})
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BibleBooksView(APIView):
    serializer_class = BibleBookListSerializer
    def get(self, request):
        try:
            version = request.GET.get('version', 'ENGLISHAMP')

            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)
                request_proto = GetBooksRequest(version=version)
                response_proto = stub.GetBooksInVersion(request_proto)

            # Convert the repeated field to a Python list
            books_list = list(response_proto.books)

            # Define a function to categorize books
            def categorize_book(book_name):
                old_testament_books = [
                    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges",
                    "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles",
                    "Ezra", "Nehemiah", "Esther", "Job", "Psalm", "Proverbs", "Ecclesiastes",
                    "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel",
                    "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah",
                    "Haggai", "Zechariah", "Malachi"
                ]
                if book_name in old_testament_books:
                    return "Old_Testament"
                else:
                    return "New_Testament"

            # Categorize the books
            categorized_books = {
                "Old_Testament": [],
                "New_Testament": [],
            }

            for book in books_list:
                category = categorize_book(book)
                categorized_books[category].append(book)

            serializer = BibleBookListSerializer(data=categorized_books)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class BibleBooksView(APIView):
#     serializer_class = BibleBookListSerializer
#     def get(self, request):
#         try:
#             version = request.GET.get('version', 'ENGLISHAMP')

#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)
#                 request_proto = GetBooksRequest(version=version)
#                 response_proto = stub.GetBooksInVersion(request_proto)

#             # Convert the repeated field to a Python list
#             books_list = list(response_proto.books)

#             serializer = BibleBookListSerializer(data={'books': books_list})
#             serializer.is_valid(raise_exception=True)
#             return Response(serializer.data)

#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class BibleChaptersView(APIView):
    serializer_class = BibleChapterListSerializer
    def get(self, request, version, book,):
        try:
            # version = request.GET.get('version', 'ENGLISHAMP')
            # book = request.GET.get('book', 'John')

            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)
                request_proto = GetChaptersRequest(version=version, book=book)
                response_proto = stub.GetChaptersInBook(request_proto)

            # Convert the repeated field to a Python list
            chapters_list = list(response_proto.chapters)

            serializer = BibleChapterListSerializer(data={'chapters': chapters_list})
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class BibleVersesView(APIView):
    serializer_class = BibleVerseSerializer
    def get(self, request, version, book, chapter,):
        try:
            # version = request.GET.get('version', 'ENGLISHAMP')
            # book = request.GET.get('book', 'John')
            # chapter = int(request.GET.get('chapter', 3))

            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)
                request_proto = GetVersesRequest(version=version, book=book, chapter=chapter)
                response_proto = stub.GetVersesInChapter(request_proto)

            # Create a list of verse content strings with verse numbers
            verses = [{'number': verse.number, 'content': verse.content} for verse in response_proto.verses]

            return Response({'verses': verses})

        except grpc.RpcError as e:
            status_code = e.code()
            if status_code == grpc.StatusCode.UNKNOWN:
                details = e.details()
                return Response({'error': details}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# class BibleVerseView(APIView):
#     def get(self, request):
#         try:
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')
#             chapter = int(request.GET.get('chapter', 3))
#             verse = int(request.GET.get('verse', 16))

#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)
#                 request = GetVerseRequest(version=version, book=book, chapter=chapter, verse=verse)
#                 response = stub.GetVerse(request)

#             serializer = BibleVerseSerializer({'content': response.content})
#             return Response(serializer.data)

#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# class BibleVerseView(APIView):
#     def get(self, request):
#         try:
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')
#             chapter = int(request.GET.get('chapter', 3))
#             verse = int(request.GET.get('verse', 16))

#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)
#                 request_proto = GetVerseRequest(version=version, book=book, chapter=chapter, verse=verse)
#                 response_proto = stub.GetVerse(request_proto)

#             # Include verse number in the response
#             verse_data = {
#                 'number': verse,
#                 'content': response_proto.content,
#             }

#             return Response(verse_data)

#         except grpc.RpcError as e:
#             status_code = e.code()
#             if status_code == grpc.StatusCode.UNKNOWN:
#                 details = e.details()
#                 return Response({'error': details}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#             else:
#                 return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







class CompareVersesView(APIView):
    serializer_class = BibleVerseSerializer
    def get(self, request, versions, books, chapters, verses):
        try:
            versions = versions.split('/')
            books = books.split('/')
            chapters = chapters.split('/')
            verses = verses.split('/')

            if not versions or not books or not chapters or not verses:
                return Response({'error': 'Versions, books, chapters, and verses are required.'}, status=status.HTTP_400_BAD_REQUEST)

            verse_data = {}

            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)

                for version, book, chapter, verse_reference in zip(versions, books, chapters, verses):
                    verse_data[version] = {}
                    verse_parts = verse_reference.split(':')
                    if len(verse_parts) == 2:
                        verse, = verse_parts  # Unpack the single value
                    elif len(verse_parts) == 3:
                        verse, = verse_parts  # Unpack the single value
                    else:
                        return Response({'error': 'Invalid verse reference format.'}, status=status.HTTP_400_BAD_REQUEST)

                    request_proto = GetVerseRequest(version=version, book=book, chapter=int(chapter), verse=int(verse))
                    response_proto = stub.GetVerse(request_proto)

                    verse_data[version][verse_reference] = response_proto.content

            return Response(verse_data)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


















from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import grpc
from . import bible_pb2_grpc
from .bible_pb2 import GetVerseRequest

class CompareVerseView(APIView):
    serializer_class = BibleVerseSerializer
    def get(self, request):
        try:
            versions = request.GET.getlist('versions[]', [])
            verse_references = request.GET.getlist('verses[]', [])

            if not versions or not verse_references:
                return Response({'error': 'Versions and verse references are required.'}, status=status.HTTP_400_BAD_REQUEST)

            verse_data = {}

            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)

                for version in versions:
                    verse_data[version] = {}
                    for verse_reference in verse_references:
                        verse_parts = verse_reference.split(':')
                        if len(verse_parts) == 2:
                            book, chapter = verse_parts
                            verse = "1"  # Default to the first verse if not provided
                        elif len(verse_parts) == 3:
                            book, chapter, verse = verse_parts
                        else:
                            return Response({'error': 'Invalid verse reference format.'}, status=status.HTTP_400_BAD_REQUEST)

                        request_proto = GetVerseRequest(version=version, book=book, chapter=int(chapter), verse=int(verse))
                        response_proto = stub.GetVerse(request_proto)

                        verse_data[version][verse_reference] = response_proto.content

            return Response(verse_data)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






















# class BibleVerseView(APIView):
#     def get(self, request, chapter, verse):
#         try:
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')

#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)
#                 request_proto = GetVerseRequest(version=version, book=book, chapter=chapter, verse=verse)
#                 response_proto = stub.GetVerse(request_proto)

#             # Include verse number in the response
#             verse_data = {
#                 'number': verse,
#                 'content': response_proto.content,
#             }

#             return Response(verse_data)

#         except grpc.RpcError as e:
#             status_code = e.code()
#             if status_code == grpc.StatusCode.UNKNOWN:
#                 details = e.details()
#                 return Response({'error': details}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#             else:
#                 return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class BibleVerseView(APIView):
#     def get(self, request, chapter, verse):
#         try:
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')

#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)
#                 request_proto = GetVerseRequest(version=version, book=book, chapter=chapter, verse=verse)
#                 response_proto = stub.GetVerse(request_proto)

#             # Include version, book, chapter, and verse number in the response
#             verse_data = {
#                 'version': version,
#                 'book': book,
#                 'chapter': chapter,
#                 'verse': verse,
#                 'content': response_proto.content,
#             }

#             return Response(verse_data)

#         except grpc.RpcError as e:
#             status_code = e.code()
#             if status_code == grpc.StatusCode.UNKNOWN:
#                 details = e.details()
#                 return Response({'error': details}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#             else:
#                 return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class BibleVerseView(APIView):
    serializer_class = BibleVerseSerializer
    def get(self, request, version, book, chapter, verse):
        try:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)
                request_proto = GetVerseRequest(version=version, book=book, chapter=chapter, verse=verse)
                response_proto = stub.GetVerse(request_proto)

            # Include version, book, chapter, and verse number in the response
            verse_data = {
                'version': version,
                'book': book,
                'chapter': chapter,
                'verse': verse,
                'content': response_proto.content,
            }

            return Response(verse_data)

        except grpc.RpcError as e:
            status_code = e.code()
            if status_code == grpc.StatusCode.UNKNOWN:
                details = e.details()
                return Response({'error': details}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)








































# # from mygrpcapp import bible_pb2_grpc
# # from mygrpcapp.bible_pb2 import GetChaptersRequest, GetVersesRequest, GetVerseRequest #GetVerseListRequest
# from dbibles.serializers import BibleBookSerializer, BibleChapterSerializer, BibleVerseSerializer, BibleVersionSerializer










# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from dbibles.models import BibleVersion, BibleBook, BibleChapter, BibleVerse

# import grpc
# from mygrpcapp import bible_pb2_grpc
# from mygrpcapp.bible_pb2 import (
#     GetChaptersRequest,
#     GetVersesRequest,
#     GetVerseRequest,
# )

# class ChapterListView(APIView):
#     def get(self, request):
#         try:
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')

#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)
#                 request = GetChaptersRequest(version=version, book=book)
#                 response = stub.GetChaptersInBook(request)
#                 chapters_list = list(response.chapters)

#             serializer = BibleChapterSerializer(chapters_list, many=True)
#             return Response({'chapters': serializer.data})

#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class VerseListView(APIView):
#     def get(self, request):
#         try:
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')
#             chapter = int(request.GET.get('chapter', 3))

#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)
#                 request = GetVersesRequest(version=version, book=book, chapter=chapter)
#                 response = stub.GetVersesInChapter(request)
#                 verse_numbers = [verse.number for verse in response.verses]

#             serializer = BibleVerseSerializer(verse_numbers, many=True)
#             return Response({'verse_numbers': serializer.data})

#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class VerseDetailView(APIView):
#     def get(self, request, chapter, verse):
#         try:
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')

#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)
#                 request = GetVerseRequest(version=version, book=book, chapter=chapter, verse=verse)
#                 response = stub.GetVerse(request)
#                 verse_content = response.content

#             serializer = BibleVerseSerializer({'number': verse, 'content': verse_content})
#             return Response({'content': serializer.data})

#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
































































# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import grpc
# from mygrpcapp import bible_pb2_grpc
# from mygrpcapp.bible_service import BibleServiceServicer

# @csrf_exempt
# def grpc_proxy(request):
#     if request.method == 'GET':
#         try:
#             # Extract the parameters from the query string
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')
#             chapter = int(request.GET.get('chapter', 3))
#             reference = request.GET.get('reference', '16-18')

#             # Parse the reference string to get the start and end verse numbers
#             start_verse, end_verse = map(int, reference.split('-'))

#             # Create a gRPC channel and stub
#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)

#                 # Initialize a list to store verses with their numbers
#                 verses_with_numbers = []

#                 # Loop through the verse range
#                 for verse_number in range(start_verse, end_verse + 1):
#                     # Create a gRPC request for each verse
#                     request = bible_pb2.GetVerseRequest(
#                         version=version,
#                         book=book,
#                         chapter=chapter,
#                         verse=verse_number
#                     )

#                     # Make the gRPC call
#                     response = stub.GetVerse(request)

#                     # Append the verse content along with its number to the list
#                     verses_with_numbers.append({
#                         'verse_number': verse_number,
#                         'content': response.content
#                     })

#                 # Return the list of verses as JSON
#                 return JsonResponse({'verses': verses_with_numbers})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import grpc
# from mygrpcapp import bible_pb2_grpc
# from mygrpcapp.bible_pb2 import GetBooksRequest

# @csrf_exempt
# def get_books_in_version(request):
#     if request.method == 'GET':
#         try:
#             # Extract the version parameter from the query string
#             version = request.GET.get('version', 'ENGLISHAMP')

#             # Create a gRPC channel and stub
#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)

#                 # Create a gRPC request to get books in the specified version
#                 request = GetBooksRequest(version=version)

#                 # Make the gRPC call
#                 response = stub.GetBooksInVersion(request)

#                 # Convert the repeated field to a Python list
#                 books_list = list(response.books)

#                 # Return the list of books as JSON
#                 return JsonResponse({'books': books_list})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid HTTP method'}, status=405)







# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import grpc
# from mygrpcapp import bible_pb2_grpc
# from mygrpcapp.bible_pb2 import GetChaptersRequest, GetVersesRequest, GetVerseRequest #GetVerseListRequest

# @csrf_exempt
# def get_chapters_in_book(request):
#     if request.method == 'GET':
#         try:
#             # Extract parameters from the query string
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')

#             # Create a gRPC channel and stub
#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)

#                 # Create a gRPC request to get chapters in the specified book and version
#                 request = GetChaptersRequest(version=version, book=book)

#                 # Make the gRPC call
#                 response = stub.GetChaptersInBook(request)

#                 # Convert the repeated field to a Python list
#                 chapters_list = list(response.chapters)

#                 # Return the list of chapters as JSON
#                 return JsonResponse({'chapters': chapters_list})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

# @csrf_exempt
# def get_verse_numbers_in_chapter(request):
#     if request.method == 'GET':
#         try:
#             # Extract parameters from the query string
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')
#             chapter = int(request.GET.get('chapter', 3))

#             # Create a gRPC channel and stub
#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)

#                 # Create a gRPC request to get verse numbers in the specified chapter, book, and version
#                 request = GetVersesRequest(version=version, book=book, chapter=chapter)

#                 # Make the gRPC call
#                 response = stub.GetVersesInChapter(request)

#                 # Extract the verse numbers
#                 verse_numbers = [verse.number for verse in response.verses]

#                 # Return the list of verse numbers as JSON
#                 return JsonResponse({'verse_numbers': verse_numbers})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

# @csrf_exempt
# def get_all_verses_in_chapter(request):
#     if request.method == 'GET':
#         try:
#             # Extract parameters from the query string
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')
#             chapter = int(request.GET.get('chapter', 3))

#             # Create a gRPC channel and stub
#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)

#                 # Create a gRPC request to get all verses in the specified chapter, book, and version
#                 request = GetVersesRequest(version=version, book=book, chapter=chapter)

#                 # Make the gRPC call
#                 response = stub.GetVersesInChapter(request)

#                 # Convert the repeated field to a list of verse dictionaries
#                 verses_list = [{'number': verse.number, 'content': verse.content} for verse in response.verses]

#                 # Return the list of verses as JSON
#                 return JsonResponse({'verses': verses_list})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

# @csrf_exempt
# def get_specific_verse(request):
#     if request.method == 'GET':
#         try:
#             # Extract parameters from the query string
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')
#             chapter = int(request.GET.get('chapter', 3))
#             verse = int(request.GET.get('verse', 16))

#             # Create a gRPC channel and stub
#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)

#                 # Create a gRPC request to get a specific verse in the specified chapter, book, and version
#                 request = GetVerseRequest(version=version, book=book, chapter=chapter, verse=verse)

#                 # Make the gRPC call
#                 response = stub.GetVerse(request)

#                 # Return the specific verse content as JSON
#                 return JsonResponse({'content': response.content})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

# # Add more endpoints as needed...





# def grpc_proxy(request):
#     if request.method == 'GET':
#         try:
#             # Extract the verse reference from the query string
#             reference = request.GET.get('reference')

#             # Split the reference into start and end parts
#             start_verse, end_verse = map(int, reference.split('-'))  # Convert to integers

#             # Extract other parameters like version and book if needed
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')

#             # Create a gRPC channel and stub
#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)

#                 # Iterate over the verse range and fetch each verse
#                 verses_content = []
#                 for verse_number in range(start_verse, end_verse + 1):
#                     # Create a gRPC request for each verse
#                     request = bible_pb2.GetVerseRequest(
#                         version=version,
#                         book=book,
#                         chapter=3,  # You may adjust the chapter as needed
#                         verse=verse_number
#                     )

#                     # Make the gRPC call for each verse
#                     response = stub.GetVerse(request)

#                     # Append the verse content to the list
#                     verses_content.append(response.content)

#                 # Return the response to the client as JSON
#                 return JsonResponse({'verses_content': verses_content})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

















# def grpc_proxy(request):
#     if request.method == 'GET':
#         try:
#             # Extract the parameters from the query string
#             version = request.GET.get('version', 'ENGLISHAMP')
#             book = request.GET.get('book', 'John')
#             chapter = int(request.GET.get('chapter', 3))
#             verse = int(request.GET.get('verse', 16))

#             # Create a gRPC channel and stub
#             with grpc.insecure_channel('localhost:50051') as channel:
#                 stub = bible_pb2_grpc.BibleServiceStub(channel)

#                 # Create a gRPC request
#                 # response = stub.GetVerse(bible_pb2.GetVerseRequest(version="ENGLISHAMP", book="John", chapter=3, verse=16))
#                 request = bible_pb2.GetVerseRequest(
#                     version=version,
#                     book=book,
#                     chapter=chapter,
#                     verse=verse
#                 )

#                 # Make the gRPC call
#                 response = stub.GetVerse(request)

#                 # Return the response to the client
#                 return JsonResponse({'content': response.content})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid HTTP method'}, status=405)



















def grpc_serve(request):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bible_pb2_grpc.add_BibleServiceServicer_to_server(BibleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')  # Specify the port you want to use
    server.start()
    server.wait_for_termination()
    return HttpResponse("gRPC server started", content_type="text/plain")
