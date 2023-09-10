# mygrpcapp/views.py
from concurrent import futures
import grpc
from django.http import HttpResponse
from dbibles import bible_service_pb2_grpc
from dbibles.bibleservice import BibleServicer

def grpc_serve(request):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bible_service_pb2_grpc.add_BibleServicer_to_server(BibleServicer(), server)
    server.add_insecure_port('[::]:50051')  # Specify the port you want to use
    server.start()
    server.wait_for_termination()
    return HttpResponse("gRPC server started", content_type="text/plain")






















# from concurrent import futures
# from django.conf import settings
# import grpc
# from . import bible_service_pb2 as bible_pb2
# from . import bible_service_pb2_grpc as bible_pb2_grpc
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

# class BibleServicer(bible_pb2_grpc.BibleServiceServicer):
#     def GetBibleVersions(self, request, context):
#         versions = BibleVersion.objects.values_list('name', flat=True)
#         return bible_pb2.BibleVersionList(versions=versions)

#     def GetBooksInVersion(self, request, context):
#         version_name = request.version
#         books = BibleBook.objects.filter(version__name=version_name).values_list('name', flat=True)
#         return bible_pb2.BibleBookList(books=books)

#     def GetChaptersInBook(self, request, context):
#         version_name = request.version
#         book_name = request.book
#         chapters = BibleChapter.objects.filter(version__name=version_name, book__name=book_name).values_list('number', flat=True)
#         return bible_pb2.BibleChapterList(chapters=chapters)

#     def GetVerseInChapter(self, request, context):
#         version_name = request.version
#         book_name = request.book
#         chapter_number = request.chapter
#         verse_number = request.verse

#         try:
#             verse = BibleVerse.objects.get(
#                 version__name=version_name,
#                 book__name=book_name,
#                 chapter__number=chapter_number,
#                 number=verse_number
#             )
#             content = verse.text
#         except BibleVerse.DoesNotExist:
#             content = "Verse not found"
        
#         return bible_pb2.BibleVerseResponse(
#             version=version_name,
#             book=book_name,
#             chapter=chapter_number,
#             verse=verse_number,
#             content=content
#         )

#     def CompareVerses(self, request, context):
#         versions = request.versions
#         book_name = request.book
#         chapter_number = request.chapter
#         verse_number = request.verse

#         verses = []
#         for version_name in versions:
#             try:
#                 verse = BibleVerse.objects.get(
#                     version__name=version_name,
#                     book__name=book_name,
#                     chapter__number=chapter_number,
#                     number=verse_number
#                 )
#                 content = verse.text
#             except BibleVerse.DoesNotExist:
#                 content = "Verse not found"

#             verses.append(bible_pb2.BibleVerseResponse(
#                 version=version_name,
#                 book=book_name,
#                 chapter=chapter_number,
#                 verse=verse_number,
#                 content=content
#             ))

#         return bible_pb2.CompareVersesResponse(verses=verses)

# class BibleGRPCView(APIView):
#     def post(self, request):
#         server = grpc.server(futures.ThreadPoolExecutor(max_workers=settings.GRPC_MAX_WORKERS))
#         bible_pb2_grpc.add_BibleServiceServicer_to_server(BibleServicer(), server)
#         server.add_insecure_port(settings.GRPC_SERVER_ADDRESS)
#         server.start()
#         server.wait_for_termination()
#         return Response({"message": "gRPC server started"})
