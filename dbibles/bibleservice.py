
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse
from . import bible_service_pb2 as bible_pb2
from . import bible_service_pb2_grpc as bible_pb2_grpc

class BibleServicer(bible_pb2_grpc.BibleServiceServicer):
    def GetBibleVersions(self, request, context):
        versions = [version.name for version in BibleVersion.objects.all()]
        return bible_pb2.BibleVersionList(versions=versions)

    def GetBooksInVersion(self, request, context):
        version_name = request.version
        version = BibleVersion.objects.get(name=version_name)
        books = [book.name for book in version.books.all()]
        return bible_pb2.BibleBookList(books=books)

    def GetChaptersInBook(self, request, context):
        version_name = request.version
        book_name = request.book
        version = BibleVersion.objects.get(name=version_name)
        book = version.books.get(name=book_name)
        chapters = [chapter.number for chapter in book.chapters.all()]
        return bible_pb2.BibleChapterList(chapters=chapters)

    def GetVerseInChapter(self, request, context):
        version_name = request.version
        book_name = request.book
        chapter_number = request.chapter
        verse_number = request.verse
        version = BibleVersion.objects.get(name=version_name)
        book = version.books.get(name=book_name)
        chapter = book.chapters.get(number=chapter_number)
        verse = chapter.verses.get(number=verse_number)
        content = verse.content
        return bible_pb2.BibleVerseResponse(
            version=version_name, book=book_name, chapter=chapter_number, verse=verse_number, content=content
        )

    def CompareVerses(self, request, context):
        versions = request.versions
        book_name = request.book
        chapter_number = request.chapter
        verse_number = request.verse
        verses = []
        for version_name in versions:
            version = BibleVersion.objects.get(name=version_name)
            book = version.books.get(name=book_name)
            chapter = book.chapters.get(number=chapter_number)
            verse = chapter.verses.get(number=verse_number)
            verses.append(
                bible_pb2.BibleVerseResponse(
                    version=version_name, book=book_name, chapter=chapter_number, verse=verse_number, content=verse.content
                )
            )
        return bible_pb2.CompareVersesResponse(verses=verses)

