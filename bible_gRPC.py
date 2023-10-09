import os
import django.conf
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()

print('Starting Bible gRPC Server')


from mygrpcapp.models import BibleVersion, BibleBook, BibleChapter, BibleVerse

import grpc
from django.http import HttpResponse
from django.db.models import Q

from concurrent import futures
import grpc
from mygrpcapp import bible_pb2 as bible_service_pb2
from mygrpcapp import bible_pb2_grpc as bible_service_pb2_grpc
from random import choice

# server_address = '127.0.0.1:50051' 
server_address = f'{settings.GRPC_SERVER_ADDRESS}:50051' 


class BibleServiceServicer(bible_service_pb2_grpc.BibleServiceServicer):
    def GetBibleVersions(self, request, context):
       
        versions = BibleVersion.objects.values_list('name', flat=True)
        response = bible_service_pb2.BibleVersionList(versions=versions)
        return response

    def GetBooksInVersion(self, request, context):
        
        books = BibleBook.objects.filter(version__name=request.version).values_list('name', flat=True)
        response = bible_service_pb2.BibleBookList(books=books)
        return response

    def GetChaptersInBook(self, request, context):
       
        chapters = BibleChapter.objects.filter(
            Q(book__name=request.book) & Q(book__version__name=request.version)
        ).values_list('number', flat=True)
        response = bible_service_pb2.BibleChapterList(chapters=chapters)
        return response

    def GetVersesInChapter(self, request, context):
        
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
        
    def GetRandomVerse(self, request, context):
        try:
           
            all_verses = BibleVerse.objects.all()

            random_verse = choice(all_verses)

            response = bible_service_pb2.BibleVerse(
                content=random_verse.content,
                number=random_verse.number
            )

            return response
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return bible_service_pb2.BibleVerse()
        
    
    def GetVerseByKeyword(self, request, context):
        try:
            keyword = request.keyword
            matching_verses = BibleVerse.objects.filter(content__icontains=keyword)

            response = bible_service_pb2.BibleVerseList(
                verses=[
                    bible_service_pb2.BibleVerse(
                        content=verse.content,
                        number=verse.number
                    )
                    for verse in matching_verses
                ]
            )

            return response
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return bible_service_pb2.BibleVerseList()


def grpc_serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bible_service_pb2_grpc.add_BibleServiceServicer_to_server(BibleServiceServicer(), server)
    server.add_insecure_port(server_address)  
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    grpc_serve()
