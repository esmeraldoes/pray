from grpc import UnaryUnaryClientInterceptor

from django.http import JsonResponse
from dbibles.bible_service_pb2_grpc import BibleServiceStub, BibleServiceServicer
# bible_service.py

import grpc
from concurrent import futures
from . import bible_service_pb2 as bible_pb2
from . import bible_service_pb2_grpc as bible_pb2_grpc
from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse
from .serializers import BibleVersionSerializer, BibleBookSerializer, BibleChapterSerializer, BibleVerseSerializer
import dbibles.bible_service_pb2 as bible_service_pb2
# from bible_service_pb2_grpc import BibleServiceStub
from dbibles.bible_service_pb2 import GetBibleVersionsRequest
from dbibles.bible_server import BibleServicer

class BibleServiceCustomClient(BibleServiceStub):

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

