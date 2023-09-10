import grpc

from django.db.models import Q
from dbibles.models import BibleVersion, BibleBook, BibleChapter, BibleVerse


from mygrpcapp import bible_pb2 as bible_service_pb2
from mygrpcapp import bible_pb2_grpc as bible_service_pb2_grpc
from dbibles.models import BibleVerse, BibleChapter, BibleBook, BibleVersion


class BibleServiceServicer(bible_service_pb2_grpc.BibleServiceServicer):
    def GetBibleVersions(self, request, context):
        # Retrieve a list of Bible versions from the database
        versions = BibleVersion.objects.values_list('name', flat=True)
        response = bible_service_pb2.BibleVersionList(versions=versions)
        return response

    def GetBooksInVersion(self, request, context):
        # Retrieve a list of books in the specified Bible version
        books = BibleBook.objects.filter(version__name=request.version).values_list('name', flat=True)
        response = bible_service_pb2.BibleBookList(books=books)
        return response

    def GetChaptersInBook(self, request, context):
        # Retrieve a list of chapters in the specified book of a Bible version
        chapters = BibleChapter.objects.filter(
            Q(book__name=request.book) & Q(book__version__name=request.version)
        ).values_list('number', flat=True)
        response = bible_service_pb2.BibleChapterList(chapters=chapters)
        return response

    def GetVersesInChapter(self, request, context):
        # Retrieve a list of verses in the specified chapter of a book in a Bible version
        verses = BibleVerse.objects.filter(
            Q(chapter__book__name=request.book) &
            Q(chapter__book__version__name=request.version) &
            Q(chapter__number=request.chapter)
        ).values('number', 'content')
        verse_list = [
            bible_service_pb2.BibleVerse(number=verse['number'], content=verse['content'])
            for verse in verses
        ]
        response = bible_service_pb2.BibleVerseList(verses=verse_list)
        return response

    def GetVerse(self, request, context):
        # Retrieve a specific verse in a chapter of a book in a Bible version
        try:
            verse = BibleVerse.objects.get(
                Q(chapter__book__name=request.book) &
                Q(chapter__book__version__name=request.version) &
                Q(chapter__number=request.chapter) &
                Q(number=request.verse)
            )
            response = bible_service_pb2.BibleVerse(content=verse.content)
            return response
        except BibleVerse.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Verse not found")
            return bible_service_pb2.BibleVerse()




























# # bible_service/service.py

# import grpc
# from mygrpcapp import bible_pb2
# from mygrpcapp import bible_pb2_grpc
# from dbibles.models import BibleVerse, BibleChapter, BibleBook, BibleVersion



# class BibleServicer(bible_pb2_grpc.BibleServicer):
#     def GetBibleVersions(self, request, context):
#         versions = BibleVersion.objects.all()
#         version_names = [version.name for version in versions]
#         return bible_pb2.BibleVersionList(versions=version_names)

#     def GetBooksInVersion(self, request, context):
#         version_name = request.version
#         try:
#             version = BibleVersion.objects.get(name=version_name)
#             books = BibleBook.objects.filter(version=version)
#             book_names = [book.name for book in books]
#             return bible_pb2.BibleBookList(books=book_names)
#         except BibleVersion.DoesNotExist:
#             context.set_code(grpc.StatusCode.NOT_FOUND)
#             context.set_details(f"Version '{version_name}' not found")
#             return bible_pb2.BibleBookList()

#     def GetChaptersInBook(self, request, context):
#         version_name = request.version
#         book_name = request.book
#         try:
#             version = BibleVersion.objects.get(name=version_name)
#             book = BibleBook.objects.get(version=version, name=book_name)
#             chapters = BibleChapter.objects.filter(book=book)
#             chapter_numbers = [chapter.number for chapter in chapters]
#             return bible_pb2.BibleChapterList(chapters=chapter_numbers)
#         except (BibleVersion.DoesNotExist, BibleBook.DoesNotExist):
#             context.set_code(grpc.StatusCode.NOT_FOUND)
#             context.set_details(f"Version '{version_name}' or book '{book_name}' not found")
#             return bible_pb2.BibleChapterList()

#     def GetVerse(self, request, context):
#         version_name = request.version
#         book_name = request.book
#         chapter_number = request.chapter
#         verse_number = request.verse
#         try:
#             version = BibleVersion.objects.get(name=version_name)
#             book = BibleBook.objects.get(version=version, name=book_name)
#             chapter = BibleChapter.objects.get(book=book, number=chapter_number)
#             verse = BibleVerse.objects.get(chapter=chapter, number=verse_number)
#             return bible_pb2.BibleVerseResponse(
#                 version=version.name,
#                 book=book.name,
#                 chapter=chapter.number,
#                 verse=verse.number,
#                 content=verse.content
#             )
#         except (BibleVersion.DoesNotExist, BibleBook.DoesNotExist, BibleChapter.DoesNotExist, BibleVerse.DoesNotExist):
#             context.set_code(grpc.StatusCode.NOT_FOUND)
#             context.set_details(f"Verse not found")
#             return bible_pb2.BibleVerseResponse()



























# # mygrpcapp/bible_service.py
# import grpc
# from mygrpcapp import bible_pb2
# from mygrpcapp import bible_pb2_grpc
# from dbibles.models import BibleVerse

# # class BibleServicer(bible_pb2_grpc.BibleServicer):
# #     def GetVerse(self, request, context):
# #         # Implement your logic here to fetch a Bible verse
# #         book = request.book
# #         chapter = request.chapter
# #         verse = request.verse
# #         content = f"This is {book} {chapter}:{verse}"  # Replace with your logic
# #         return bible_pb2.VerseResponse(content=content)


# class BibleServicer(bible_pb2_grpc.BibleServicer):
#     def GetVerse(self, request, context):
#         book = request.book
#         chapter = request.chapter
#         verse = request.verse

#         try:
#             # Fetch the Bible verse from your database
#             verse_obj = BibleVerse.objects.get(book=book, chapter=chapter, verse=verse)
#             content = verse_obj.text
#             return bible_pb2.VerseResponse(content=content)
#         except BibleVerse.DoesNotExist:
#             # Handle the case where the requested verse does not exist
#             context.set_code(grpc.StatusCode.NOT_FOUND)
#             context.set_details("Verse not found")
#             return bible_pb2.VerseResponse(content="")

#         except Exception as e:
#             # Handle other exceptions
#             context.set_code(grpc.StatusCode.INTERNAL)
#             context.set_details(f"Internal server error: {str(e)}")
#             return bible_pb2.VerseResponse(content="")
