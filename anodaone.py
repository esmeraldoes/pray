from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import grpc
from mygrpcapp import bible_pb2_grpc
from mygrpcapp.bible_pb2 import GetChaptersRequest, GetVersesRequest, GetVerseRequest, GetVerseListRequest

@csrf_exempt
def get_chapters_in_book(request):
    if request.method == 'GET':
        try:
            # Extract parameters from the query string
            version = request.GET.get('version', 'ENGLISHAMP')
            book = request.GET.get('book', 'John')

            # Create a gRPC channel and stub
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)

                # Create a gRPC request to get chapters in the specified book and version
                request = GetChaptersRequest(version=version, book=book)

                # Make the gRPC call
                response = stub.GetChaptersInBook(request)

                # Convert the repeated field to a Python list
                chapters_list = list(response.chapters)

                # Return the list of chapters as JSON
                return JsonResponse({'chapters': chapters_list})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def get_verse_numbers_in_chapter(request):
    if request.method == 'GET':
        try:
            # Extract parameters from the query string
            version = request.GET.get('version', 'ENGLISHAMP')
            book = request.GET.get('book', 'John')
            chapter = int(request.GET.get('chapter', 3))

            # Create a gRPC channel and stub
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)

                # Create a gRPC request to get verse numbers in the specified chapter, book, and version
                request = GetVersesRequest(version=version, book=book, chapter=chapter)

                # Make the gRPC call
                response = stub.GetVersesInChapter(request)

                # Extract the verse numbers
                verse_numbers = [verse.number for verse in response.verses]

                # Return the list of verse numbers as JSON
                return JsonResponse({'verse_numbers': verse_numbers})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def get_all_verses_in_chapter(request):
    if request.method == 'GET':
        try:
            # Extract parameters from the query string
            version = request.GET.get('version', 'ENGLISHAMP')
            book = request.GET.get('book', 'John')
            chapter = int(request.GET.get('chapter', 3))

            # Create a gRPC channel and stub
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)

                # Create a gRPC request to get all verses in the specified chapter, book, and version
                request = GetVersesRequest(version=version, book=book, chapter=chapter)

                # Make the gRPC call
                response = stub.GetVersesInChapter(request)

                # Convert the repeated field to a list of verse dictionaries
                verses_list = [{'number': verse.number, 'content': verse.content} for verse in response.verses]

                # Return the list of verses as JSON
                return JsonResponse({'verses': verses_list})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def get_specific_verse(request):
    if request.method == 'GET':
        try:
            # Extract parameters from the query string
            version = request.GET.get('version', 'ENGLISHAMP')
            book = request.GET.get('book', 'John')
            chapter = int(request.GET.get('chapter', 3))
            verse = int(request.GET.get('verse', 16))

            # Create a gRPC channel and stub
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = bible_pb2_grpc.BibleServiceStub(channel)

                # Create a gRPC request to get a specific verse in the specified chapter, book, and version
                request = GetVerseRequest(version=version, book=book, chapter=chapter, verse=verse)

                # Make the gRPC call
                response = stub.GetVerse(request)

                # Return the specific verse content as JSON
                return JsonResponse({'content': response.content})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

# Add more endpoints as needed...
