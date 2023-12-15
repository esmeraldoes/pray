
import grpc

from mygrpcapp import bible_pb2_grpc
from django.views.decorators.csrf import csrf_exempt
from concurrent import futures
import grpc
from mygrpcapp import bible_pb2
from mygrpcapp import bible_pb2_grpc

from mygrpcapp.bibbbtrble_service import BibleServiceServicer

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
from django.conf import settings
# server_address = '127.0.0.1:50051' 
server_address = f'{settings.GRPC_SERVER_ADDRESS}:8001' 


class BibleVersionsView(APIView):
    serializer_class = BibleVersionListSerializer
    def get(self, request):
        
        try:
            with grpc.insecure_channel(server_address) as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)
                request = Empty()
                response = stub.GetBibleVersions(request)

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

            with grpc.insecure_channel(server_address) as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)
                request_proto = GetBooksRequest(version=version)
                response_proto = stub.GetBooksInVersion(request_proto)

            books_list = list(response_proto.books)

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

class BibleChaptersView(APIView):
    serializer_class = BibleChapterListSerializer
    def get(self, request, version, book,):
        try:
            # version = request.GET.get('version', 'ENGLISHAMP')
            # book = request.GET.get('book', 'John')

            with grpc.insecure_channel(server_address) as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)
                request_proto = GetChaptersRequest(version=version, book=book)
                response_proto = stub.GetChaptersInBook(request_proto)

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

            with grpc.insecure_channel(server_address) as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)
                request_proto = GetVersesRequest(version=version, book=book, chapter=chapter)
                response_proto = stub.GetVersesInChapter(request_proto)

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

            with grpc.insecure_channel(server_address) as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)

                for version, book, chapter, verse_reference in zip(versions, books, chapters, verses):
                    verse_data[version] = {}
                    verse_parts = verse_reference.split(':')
                    if len(verse_parts) == 2:
                        verse, = verse_parts  
                    elif len(verse_parts) == 3:
                        verse, = verse_parts  
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

            with grpc.insecure_channel(server_address) as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)

                for version in versions:
                    verse_data[version] = {}
                    for verse_reference in verse_references:
                        verse_parts = verse_reference.split(':')
                        if len(verse_parts) == 2:
                            book, chapter = verse_parts
                            verse = "1" 
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








class BibleVerseView(APIView):
    serializer_class = BibleVerseSerializer
    def get(self, request, version, book, chapter, verse):
        try:
            with grpc.insecure_channel(server_address) as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)
                request_proto = GetVerseRequest(version=version, book=book, chapter=chapter, verse=verse)
                response_proto = stub.GetVerse(request_proto)

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



# def grpc_serve(request):
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     bible_pb2_grpc.add_BibleServiceServicer_to_server(BibleServiceServicer(), server)
#     server.add_insecure_port('[::]:50051')  # Specify the port you want to use
#     server.start()
#     server.wait_for_termination()
#     return HttpResponse("gRPC server started", content_type="text/plain")
