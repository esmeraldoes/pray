# bible_service.py

import grpc
from concurrent import futures
# from . import bible_service_pb2 as bible_pb2
# from . import bible_service_pb2_grpc as bible_pb2_grpc
import bible_service_pb2 as bible_pb2
import bible_service_pb2_grpc as bible_pb2_grpc
# from models import *
# Import necessary Django models and serializers for Bible data
from dbibles.models import BibleVersion, BibleBook, BibleChapter, BibleVerse
from serializers import BibleVersionSerializer, BibleBookSerializer, BibleChapterSerializer, BibleVerseSerializer
import dbibles.bible_service_pb2 as bible_service_pb2
class BibleServicer(bible_pb2_grpc.BibleServiceServicer):
    # def GetBibleVersions(self, request, context):
    #     # Implement GetBibleVersions: Fetch and return Bible versions from the database
    #     # Handle the default version case (ENGLISHAMP)
    #     versions = BibleVersion.objects.all()
    #     serialized_versions = BibleVersionSerializer(versions, many=True)
    #     return bible_pb2.BibleVersionList(versions=serialized_versions.data)

    def GetBibleVersions(self, request, context):
        """
        Get a list of all the Bible versions.
        """
        response = bible_service_pb2.BibleVersionList()
        for version in BibleVersion.objects.all():
            response.versions.append(bible_service_pb2.BibleVersion(
            name=version.name
            ))
        return response



    def GetBooksInVersion(self, request, context):
        # Implement GetBooksInVersion: Fetch and return books in the specified version from the database
        version_name = request.version
        try:
            version = BibleVersion.objects.get(name=version_name)
            books = BibleBook.objects.filter(version=version)
            serialized_books = BibleBookSerializer(books, many=True)
            return bible_pb2.BibleBookList(books=serialized_books.data)
        except BibleVersion.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Bible version not found.")
            return bible_pb2.BibleBookList()

    def GetChaptersInBook(self, request, context):
        # Implement GetChaptersInBook: Fetch and return chapters in the specified book from the database
        version_name = request.version
        book_name = request.book
        try:
            version = BibleVersion.objects.get(name=version_name)
            book = BibleBook.objects.get(version=version, name=book_name)
            chapters = BibleChapter.objects.filter(book=book)
            serialized_chapters = BibleChapterSerializer(chapters, many=True)
            return bible_pb2.BibleChapterList(chapters=[chap.number for chap in serialized_chapters.data])
        except (BibleVersion.DoesNotExist, BibleBook.DoesNotExist):
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Bible version or book not found.")
            return bible_pb2.BibleChapterList()

    def GetVerseInChapter(self, request, context):
        # Implement GetVerseInChapter: Fetch and return a specific verse in the specified chapter from the database
        version_name = request.version
        book_name = request.book
        chapter_number = request.chapter
        verse_number = request.verse
        try:
            version = BibleVersion.objects.get(name=version_name)
            book = BibleBook.objects.get(version=version, name=book_name)
            chapter = BibleChapter.objects.get(book=book, number=chapter_number)
            verse = BibleVerse.objects.get(chapter=chapter, number=verse_number)
            serialized_verse = BibleVerseSerializer(verse)
            return bible_pb2.BibleVerseResponse(
                version=version.name,
                book=book.name,
                chapter=chapter.number,
                verse=verse.number,
                content=serialized_verse.data['content']
            )
        except (BibleVersion.DoesNotExist, BibleBook.DoesNotExist, BibleChapter.DoesNotExist, BibleVerse.DoesNotExist):
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Verse not found.")
            return bible_pb2.BibleVerseResponse()

    def CompareVerses(self, request, context):
        # Implement CompareVerses: Fetch and return verses from different versions for comparison
        versions = request.versions
        book_name = request.book
        chapter_number = request.chapter
        verse_number = request.verse
        try:
            verses = []
            for version_name in versions:
                version = BibleVersion.objects.get(name=version_name)
                book = BibleBook.objects.get(version=version, name=book_name)
                chapter = BibleChapter.objects.get(book=book, number=chapter_number)
                verse = BibleVerse.objects.get(chapter=chapter, number=verse_number)
                serialized_verse = BibleVerseSerializer(verse)
                verses.append(bible_pb2.BibleVerseResponse(
                    version=version.name,
                    book=book.name,
                    chapter=chapter.number,
                    verse=verse.number,
                    content=serialized_verse.data['content']
                ))
            return bible_pb2.CompareVersesResponse(verses=verses)
        except (BibleVersion.DoesNotExist, BibleBook.DoesNotExist, BibleChapter.DoesNotExist, BibleVerse.DoesNotExist):
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Verse not found.")
            return bible_pb2.CompareVersesResponse()

# Serve the gRPC service
def serve(request):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bible_pb2_grpc.add_BibleServiceServicer_to_server(BibleServicer(), server)
    server.add_insecure_port('[::]:8000')  # Use a unique port for your gRPC service
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

# def serve(request):
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=settings.GRPC_MAX_WORKERS))
#     bible_pb2_grpc.add_BibleServiceServicer_to_server(BibleServicer(), server)
#     server.add_insecure_port(settings.GRPC_SERVER_ADDRESS)
#     server.start()
#     server.wait_for_termination()

#     return JsonResponse({'result': 'gRPC server started'})































# # bible_app/bible_server.py

# import grpc
# from concurrent import futures
# from grpc.bible_service_pb2 import VerseRequest, VerseResponse, VerseComparisonRequest, VerseComparisonResponse, VerseWithContent
# from grpc.bible_service_pb2_grpc import BibleServiceServicer, add_BibleServiceServicer_to_server
# from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

# class BibleServiceImplementation(BibleServiceServicer):
#     def GetVerse(self, request, context):
#         try:
#             version = BibleVersion.objects.get(id=request.version_id)
#             book = BibleBook.objects.get(version=version, name=request.book)
#             chapter = BibleChapter.objects.get(book=book, number=request.chapter)
#             verse = BibleVerse.objects.get(chapter=chapter, number=request.verse)
#             response = VerseResponse(content=verse.content)
#             return response
#         except (BibleVersion.DoesNotExist, BibleBook.DoesNotExist, BibleChapter.DoesNotExist, BibleVerse.DoesNotExist):
#             context.set_code(grpc.StatusCode.NOT_FOUND)
#             context.set_details("Verse not found.")
#             return VerseResponse(content="")

#     def CompareVerses(self, request, context):
#         verses = []
#         for version_id in request.version_ids:
#             try:
#                 version = BibleVersion.objects.get(id=version_id)
#                 book = BibleBook.objects.get(version=version, name=request.book)
#                 chapter = BibleChapter.objects.get(book=book, number=request.chapter)
#                 verse = BibleVerse.objects.get(chapter=chapter, number=request.verse)

#                 verses.append(VerseWithContent(
#                     version=version.name,
#                     book=book.name,
#                     chapter=chapter.number,
#                     verse=verse.number,
#                     content=verse.content,
#                 ))
#             except (BibleVersion.DoesNotExist, BibleBook.DoesNotExist, BibleChapter.DoesNotExist, BibleVerse.DoesNotExist):
#                 pass

#         response = VerseComparisonResponse(verses=verses)
#         return response

# def serve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     add_BibleServiceServicer_to_server(BibleServiceImplementation(), server)
#     server.add_insecure_port('[::]:50051')
#     server.start()
#     server.wait_for_termination()

# if __name__ == '__main__':
#     serve()
