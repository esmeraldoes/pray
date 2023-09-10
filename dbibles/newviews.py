# from django.http import JsonResponse
# from django.views import View
# import grpc

# from . import bible_service_pb2 as bible_pb2
# # from . import bible_service_pb2_grpc as bible_pb2_grpc
# # import bible_service_pb2
# # # import bible_service_pb2
# # import bible_service_pb2_grpc

# # Assuming your gRPC server is running on localhost:50051
# GRPC_HOST = '127.0.0.1'
# GRPC_PORT = 8000

# from django.views import View
# from django.http import JsonResponse
# from dbibles.bible_service_pb2_grpc import BibleServiceStub, BibleServiceServicer

# # from bible_service_pb2_grpc import BibleServiceStub
# from dbibles.bible_service_pb2 import GetBibleVersionsRequest
# # from dbibles.bible_server import BibleServicer




# # class GetBibleVersionsView(View):

# #     def get(self, request):
# #         with grpc.insecure_channel('localhost:80001') as channel:
# #             stub = BibleServiceServicer(channel)
# #             # stub = BibleServiceStub(channel)

# #             response = stub.GetBibleVersions(GetBibleVersionsRequest())

# #             return JsonResponse({'versions': response.versions})
        
# # from dbibles.tryi import BibleServiceCustomClient

# # class GetBibleVersionsView(View):
# #     """Get a list of all the Bible versions."""

# #     def get(self, request):
# #         with grpc.insecure_channel('localhost:80001') as channel:
# #             client = BibleServiceCustomClient(channel)
# #             response = client.GetBibleVersions(bible_pb2.GetBibleVersionsRequest())
# #         return JsonResponse(response.versions, safe=False)



# from django.http import JsonResponse
# from .models import BibleVersion  # Replace with your actual model

# GRPC_SERVER_ADDRESS = 'localhost:80001'

# def get_bible_versions(request):
#     with grpc.insecure_channel(GRPC_SERVER_ADDRESS) as channel:
#         stub = bible_pb2_grpc.BibleServiceStub(channel)
        
#         # Fetch data from the database (assuming you have a BibleVersion model)
#         versions = BibleVersion.objects.all()
        
#         # Construct gRPC request
#         grpc_request = bible_pb2.GetBibleVersionsRequest()
        
#         # Process the gRPC response and create a JSON response
#         response = stub.GetBibleVersions(grpc_request)
#         data = {
#             'versions': [version.name for version in response.versions],
#         }
#         return JsonResponse(data)



# class GetBibleVersions(View):
#     def get(self, request, *args, **kwargs):
#         with grpc.insecure_channel(f"{GRPC_HOST}:{GRPC_PORT}") as channel:
#             stub = bible_pb2_grpc.BibleServiceStub(channel)
#             response = stub.GetBibleVersions(bible_pb2.EmptyRequest())
            
#             versions = [version.name for version in response.versions]
#             return JsonResponse({"versions": versions})

# class GetBooksInVersion(View):
#     def get(self, request, *args, **kwargs):
#         version_name = request.GET.get("version", "ENGLISHAMP")
#         if not version_name:
#             return JsonResponse({"error": "Version is required."}, status=400)
            
#         with grpc.insecure_channel(f"{GRPC_HOST}:{GRPC_PORT}") as channel:
#             stub = bible_pb2_grpc.BibleServiceStub(channel)
#             response = stub.GetBooksInVersion(bible_pb2.BibleVersionRequest(version=version_name))
            
#             books = [book.name for book in response.books]
#             return JsonResponse({"books": books})
        
# from custom_grpc import BibleServiceCustomClient
# import bible_service_pb2

# class GetBibleVersionsView4(View):
#     """Get a list of all the Bible versions."""

#     def get(self, request):
#         with grpc.insecure_channel('localhost:50051') as channel:
#             client = BibleServiceCustomClient(channel)
#             response = client.GetBibleVersions(bible_service_pb2.GetBibleVersionsRequest())
#         return JsonResponse(response.versions, safe=False)



# class GetChaptersInBook(View):
#     def get(self, request, *args, **kwargs):
#         version_name = request.GET.get("version")
#         book_name = request.GET.get("book")
        
#         if not version_name or not book_name:
#             return JsonResponse({"error": "Version and book are required."}, status=400)
            
#         with grpc.insecure_channel(f"{GRPC_HOST}:{GRPC_PORT}") as channel:
#             stub = bible_pb2_grpc.BibleServiceStub(channel)
#             response = stub.GetChaptersInBook(bible_pb2.BookRequest(version=version_name, book=book_name))
            
#             chapters = response.chapters
#             return JsonResponse({"chapters": chapters})

# class GetVerseInChapter(View):
#     def get(self, request, *args, **kwargs):
#         version_name = request.GET.get("version")
#         book_name = request.GET.get("book")
#         chapter_number = int(request.GET.get("chapter", 0))
#         verse_number = int(request.GET.get("verse", 0))
        
#         if not version_name or not book_name or chapter_number <= 0 or verse_number <= 0:
#             return JsonResponse({"error": "Version, book, chapter, and verse are required."}, status=400)
            
#         with grpc.insecure_channel(f"{GRPC_HOST}:{GRPC_PORT}") as channel:
#             stub = bible_pb2_grpc.BibleServiceStub(channel)
#             response = stub.GetVerseInChapter(bible_pb2.VerseRequest(
#                 version=version_name,
#                 book=book_name,
#                 chapter=chapter_number,
#                 verse=verse_number
#             ))
            
#             return JsonResponse({
#                 "version": response.version,
#                 "book": response.book,
#                 "chapter": response.chapter,
#                 "verse": response.verse,
#                 "content": response.content
#             })

# class CompareVerses(View):
#     def get(self, request, *args, **kwargs):
#         versions = request.GET.getlist("versions[]")
#         book_name = request.GET.get("book")
#         chapter_number = int(request.GET.get("chapter", 0))
#         verse_number = int(request.GET.get("verse", 0))
        
#         if not versions or not book_name or chapter_number <= 0 or verse_number <= 0:
#             return JsonResponse({"error": "Versions, book, chapter, and verse are required."}, status=400)
            
#         with grpc.insecure_channel(f"{GRPC_HOST}:{GRPC_PORT}") as channel:
#             stub = bible_pb2_grpc.BibleServiceStub(channel)
#             response = stub.CompareVerses(bible_pb2.CompareRequest(
#                 versions=versions,
#                 book=book_name,
#                 chapter=chapter_number,
#                 verse=verse_number
#             ))
            
#             verses = [{
#                 "version": verse.version,
#                 "book": verse.book,
#                 "chapter": verse.chapter,
#                 "verse": verse.verse,
#                 "content": verse.content
#             } for verse in response.verses]
            
#             return JsonResponse({"verses": verses})































# from rest_framework import viewsets
# from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse
# from .serializers import BibleVersionSerializer, BibleBookSerializer, BibleChapterSerializer, BibleVerseSerializer

# class BibleVersionViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = BibleVersionSerializer
#     queryset = BibleVersion.objects.all()

# class BibleBookViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = BibleBookSerializer
#     queryset = BibleBook.objects.all()

#     def get_queryset(self):
#         version_id = self.request.query_params.get('version_id')
#         if version_id:
#             return self.queryset.filter(version_id=version_id)
#         return self.queryset


# class BibleChapterViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = BibleChapterSerializer
#     queryset = BibleChapter.objects.all()

# class BibleVerseViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = BibleVerseSerializer
#     queryset = BibleVerse.objects.all()

#     def get_queryset(self):
#             chapter_id = self.request.query_params.get('chapter_id')
#             book_id = self.request.query_params.get('book_id')
#             version_id = self.request.query_params.get('version_id')
#             verse_number = self.request.query_params.get('verse_number')

#             queryset = self.queryset

#             if version_id:
#                 queryset = queryset.filter(chapter__book__version_id=version_id)
#             if book_id:
#                 queryset = queryset.filter(chapter__book_id=book_id)
#             if chapter_id:
#                 queryset = queryset.filter(chapter_id=chapter_id)
#             if verse_number:
#                 queryset = queryset.filter(number=verse_number)

#             return queryset
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse
# from .serializers import BibleVerseSerializer

# class getVerseComparison(APIView):
#     def get(self, request):
#         book_name = request.query_params.get('book')
#         chapter_number = request.query_params.get('chapter')
#         verse_number = request.query_params.get('verse')
#         version_ids = request.query_params.getlist('version_ids[]')

#         # Validate the input
#         if not book_name or not chapter_number or not verse_number or not version_ids:
#             return Response({"error": "book, chapter, verse, and version_ids are required."}, status=400)

#         try:
#             chapter_number = int(chapter_number)
#             verse_number = int(verse_number)
#         except ValueError:
#             return Response({"error": "chapter and verse must be valid integers."}, status=400)

#         # Retrieve the verses for the specified book, chapter, verse number, and versions
#         verses = []
#         versions = BibleVersion.objects.filter(id__in=version_ids)
#         for version in versions:
#             try:
#                 book = BibleBook.objects.get(version=version, name=book_name)
#                 chapter = BibleChapter.objects.get(book=book, number=chapter_number)
#                 verse = BibleVerse.objects.get(chapter=chapter, number=verse_number)

#                 verses.append({
#                     "version": version.name,
#                     "book": book.name,
#                     "chapter": chapter.number,
#                     "verse": verse.number,
#                     "content": verse.content
#                 })
#             except (BibleBook.DoesNotExist, BibleChapter.DoesNotExist, BibleVerse.DoesNotExist):
#                 pass

#         return Response(verses)























































# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse
# # from .serializers import BibleVerseSerializer

# # class VerseComparison(APIView):
# #     def get(self, request):
# #         book_name = request.query_params.get('book')
# #         chapter_number = request.query_params.get('chapter')
# #         verse_number = request.query_params.get('verse')

# #         # Validate the input
# #         if not book_name or not chapter_number or not verse_number:
# #             return Response({"error": "book, chapter, and verse are required."}, status=400)

# #         try:
# #             chapter_number = int(chapter_number)
# #             verse_number = int(verse_number)
# #         except ValueError:
# #             return Response({"error": "chapter and verse must be valid integers."}, status=400)

# #         # Retrieve the verses for the specified book, chapter, and verse number from different versions
# #         verses = []
# #         versions = BibleVersion.objects.all()
# #         for version in versions:
# #             try:
# #                 book = BibleBook.objects.get(version=version, name=book_name)
# #                 chapter = BibleChapter.objects.get(book=book, number=chapter_number)
# #                 verse = BibleVerse.objects.get(chapter=chapter, number=verse_number)

# #                 verses.append({
# #                     "version": version.name,
# #                     "book": book.name,
# #                     "chapter": chapter.number,
# #                     "verse": verse.number,
# #                     "content": verse.content
# #                 })
# #             except (BibleBook.DoesNotExist, BibleChapter.DoesNotExist, BibleVerse.DoesNotExist):
# #                 pass

# #         return Response(verses)








































# # from rest_framework import generics
# # # from rest_framework.pagination import PageNumberPagination
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # # from .models import BibleBook, BibleChapter, BibleVerse
# # # from .serializers import BibleBookSerializer, BibleChapterSerializer, BibleVerseSerializer, VerseComparisonSerializer


# # from rest_framework.generics import ListAPIView
# # from .models import BibleVersion, BibleBook, BibleVerse, BibleChapter
# # from .serializers import VersionSerializer, BibleBookSerializer, BibleChapterSerializer,  BibleVerseSerializer
# # from rest_framework.viewsets import ModelViewSet







# # # # class BibleVerseView(APIView):
# # # #     def get(self, request, version, book, chapter, verse):
# # # #         try:
# # # #             verse_obj = BibleVerse.objects.get(
# # # #                 version__name=version,
# # # #                 book__name=book,
# # # #                 chapter__number=chapter,
# # # #                 number=verse
# # # #             )
# # # #         except BibleVerse.DoesNotExist:
# # # #             return Response({'message': 'Verse not found'}, status=404)

# # # #         serializer = BibleVerseSerializer(verse_obj)
# # # #         return Response(serializer.data)


# # # class BibleChapterView(APIView):
# # #     def get(self, request, version, book, chapter):
# # #         try:
# # #             chapter_obj = BibleChapter.objects.get(
# # #                 book__version__name=version,
# # #                 book__name=book,
# # #                 number=chapter
# # #             )
# # #         except BibleChapter.DoesNotExist:
# # #             return Response({'message': 'Chapter not found'}, status=404)

# # #         verses = BibleVerse.objects.filter(chapter=chapter_obj)
# # #         serializer = BibleVerseSerializer(verses, many=True)
# # #         return Response(serializer.data)
    


# # # from rest_framework.views import APIView
# # # from rest_framework.response import Response
# # # from .models import BibleChapter, BibleVersion
# # # from .serializers import BibleChapterSerializer


# # class BibleChapterView1(APIView):
# #     def get(self, request, version='ENGLISHAMP'):
# #         try:
# #             bible_version = BibleVersion.objects.get(name=version)
# #             print("NA THE VERSION", bible_version)
# #             chapters = BibleChapter.objects.filter(book__version=bible_version)
# #             print([i for i in chapters])
# #             serializer = BibleChapterSerializer(chapters, many=True)
# #             return Response(serializer.data)
# #         except BibleVersion.DoesNotExist:
# #             return Response({"error": f"Version '{version}' not found."}, status=404)

# # # class BibleVerseView(APIView):
# # #     def get(self, request, version='ENGLISHAMP', book=None, chapter=None):
# # #         if not book or not chapter:
# # #             return Response({'error': 'Both book and chapter parameters are required.'}, status=400)

# # #         verses = BibleVerse.objects.filter(version__name=version, book__name=book, chapter__number=chapter)
# # #         serializer = BibleVerseSerializer(verses, many=True)
# # #         return Response(serializer.data)




















# # class BibleVersionListView(generics.ListAPIView):
# #     queryset = BibleVersion.objects.all()
# #     serializer_class = VersionSerializer


# # # # class BibleChapterListView(generics.ListAPIView):
# # # #     serializer_class = BibleChapterSerializer

# # # #     def get_queryset(self):
# # # #         version_name = self.kwargs['version_name']
# # # #         book_name = self.kwargs['book_name']
# # # #         return BibleChapter.objects.filter(book__version__name=version_name, book__name=book_name)

# # # # class BibleVerseListView(generics.ListAPIView):
# # # #     serializer_class = BibleVerseSerializer

# # # #     def get_queryset(self):
# # # #         version_name = self.kwargs['version_name']
# # # #         book_name = self.kwargs['book_name']
# # # #         chapter_number = self.kwargs['chapter_number']
# # # #         return BibleVerse.objects.filter(
# # # #             version__name=version_name,
# # # #             chapter__book__name=book_name,
# # # #             chapter__number=chapter_number
# # # #         )

# # # ###STOPPED



# # # from rest_framework import generics
# # # from rest_framework.response import Response
# # # from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse
# # # from .serializers import VersionSerializer, BibleBookSerializer, BibleChapterSerializer, BibleVerseSerializer


# # # class BibleBookList(generics.ListAPIView):
# # #     serializer_class = BibleBookSerializer

# # #     def get_queryset(self):
# # #         version_name = self.kwargs['version']
# # #         return BibleBook.objects.filter(version__name=version_name)

# # # class BibleChapterList(generics.ListAPIView):
# # #     serializer_class = BibleChapterSerializer

# # #     def get_queryset(self):
# # #         version_name = self.kwargs['version']
# # #         book_name = self.kwargs['book']
# # #         return BibleChapter.objects.filter(book__version__name=version_name, book__name=book_name)

# # # class BibleVerseList(generics.ListAPIView):
# # #     serializer_class = BibleVerseSerializer

# # #     def get_queryset(self):
# # #         version_name = self.kwargs['version']
# # #         book_name = self.kwargs['book']
# # #         chapter_number = self.kwargs['chapter']
# # #         return BibleVerse.objects.filter(version__name=version_name, chapter__book__name=book_name, chapter__number=chapter_number)

# # # class BibleVerseDetail(generics.RetrieveAPIView):
# # #     queryset = BibleVerse.objects.all()
# # #     serializer_class = BibleVerseSerializer
# # #     lookup_url_kwarg = 'verse'






































































































# # # # class BibleVerseView(APIView):
# # # #     def get(self, request, version, book, chapter, verse):
# # # #         try:
# # # #             verse_obj = BibleVerse.objects.get(
# # # #                 version__name=version,
# # # #                 book__name=book,
# # # #                 chapter__number=chapter,
# # # #                 number=verse
# # # #             )
# # # #         except BibleVerse.DoesNotExist:
# # # #             return Response({'message': 'Verse not found'}, status=404)

# # # #         serializer = BibleVerseSerializer(verse_obj)
# # # #         return Response(serializer.data)


# # # # class BibleChapterView(APIView):
# # # #     def get(self, request, version, book, chapter):
# # # #         try:
# # # #             chapter_obj = BibleChapter.objects.get(
# # # #                 book__version__name=version,
# # # #                 book__name=book,
# # # #                 number=chapter
# # # #             )
# # # #         except BibleChapter.DoesNotExist:
# # # #             return Response({'message': 'Chapter not found'}, status=404)

# # # #         verses = BibleVerse.objects.filter(chapter=chapter_obj)
# # # #         serializer = BibleVerseSerializer(verses, many=True)
# # # #         return Response(serializer.data)







# # class VersionListView(ListAPIView):
# #     queryset = BibleVersion.objects.all()
# #     serializer_class = VersionSerializer

# # # class BibleVersionViewSet(ModelViewSet):
# # #     queryset = BibleVersion.objects.all()
# # #     serializer_class = VersionSerializer


# # class BibleChapterView5(APIView):
# #     def get(self, request, version=1):
# #         chapters = BibleBook.objects.filter(version=version)
# #         serializer = BibleBookSerializer(chapters, many=True)
# #         # print(serializer)
# #         return Response(serializer.data)


# # from rest_framework import viewsets
# # from .models import BibleBook
# # from .serializers import BibleBookSerializer



# # class BibleVersionViewSet(viewsets.ReadOnlyModelViewSet):
# #     serializer_class = BibleVersionSerializer
# #     queryset = BibleVersion.objects.all()
    
# # class BibleBookViewSet(viewsets.ReadOnlyModelViewSet):
# #     serializer_class = BibleBookSerializer
    

# #     def get_queryset(self):
# #         version_id = self.request.query_params.get('version_id', 1)  # Set DEFAULT_VERSION_ID to the desired default version ID
# #         return BibleBook.objects.filter(version_id=version_id)


# # # class BibleBookViewSet(viewsets.ReadOnlyModelViewSet):
# # #     serializer_class = BibleBookSerializer

# # #     def get_queryset(self):
# # #         version_id = self.request.query_params.get('version_id')
# # #         if version_id:
# # #             return BibleBook.objects.filter(version_id=version_id)
# # #         return BibleBook.objects.none()  # Return an empty queryset if version_id is not provided


# # # class BibleChapterVerseList(generics.ListAPIView):
# # #     serializer_class = BibleVerseSerializer

# # #     def get_queryset(self):
# # #         version = self.request.GET.get('version', '1')
# # #         chapter_id = self.kwargs['chapter_id']
# # #         return BibleVerse.objects.filter(chapter_id=chapter_id, version=version)
    




# # # # class ChapterVersesAPIView(generics.ListAPIView):
# # # #     serializer_class = BibleVerseSerializer

# # # #     def get_queryset(self):
# # # #         version = self.kwargs['version']
# # # #         book = self.kwargs['book']
# # # #         chapter = self.kwargs['chapter']
        
# # # #         queryset = BibleVerse.objects.filter(chapter__book__name=book, chapter__number=chapter, version=version)
# # # #         return queryset


# # # # class BibleVerseListAPIView(generics.ListAPIView):
# # # #     serializer_class = BibleVerseSerializer
# # # #     # pagination_class = PageNumberPagination

# # # #     def get_queryset(self):
# # # #         queryset = BibleVerse.objects.all()
# # # #         chapter_id = self.request.query_params.get('chapter_id')
# # # #         book_id = self.request.query_params.get('book_id')
# # # #         if chapter_id:
# # # #             queryset = queryset.filter(chapter_id=chapter_id)
# # # #         if book_id:
# # # #             queryset = queryset.filter(chapter__book_id=book_id)
# # # #         return queryset

# # # # class BibleChapterListAPIView(generics.ListAPIView):
# # # #     serializer_class = BibleChapterSerializer
# # # #     # pagination_class = PageNumberPagination

# # # #     def get_queryset(self):
# # # #         queryset = BibleChapter.objects.all()
# # # #         book_id = self.request.query_params.get('book_id')
# # # #         if book_id:
# # # #             queryset = queryset.filter(book_id=book_id)
# # # #         return queryset

# # class BibleBookListAPIView(generics.ListAPIView):
# #     serializer_class = BibleBookSerializer
# #     # pagination_class = PageNumberPagination
# #     queryset = BibleBook.objects.all()



# # class BibleBookListView(generics.ListAPIView):
# #     serializer_class = BibleBookSerializer

# #     def get_queryset(self):
# #         version_name = self.kwargs['version_name']
# #         return BibleBook.objects.filter(version__name=version_name)















# # # # from rest_framework.viewsets import ModelViewSet
# # # # from .serializers import BibleBookSerializer, BibleChapterSerializer, BibleVerseSerializer
# # # # from .models import BibleBook, BibleChapter, BibleVerse

# # # # class BibleViewSet(ModelViewSet):
# # # #     queryset = BibleBook.objects.all()
# # # #     serializer_class = BibleBookSerializer

# # # #     def get_queryset(self):
# # # #         queryset = super().get_queryset()
# # # #         version = self.request.query_params.get('version')  # Get the version from query parameters
# # # #         if version:
# # # #             queryset = queryset.filter(verses__version=version).distinct()  # Filter based on the chosen version
# # # #         return queryset


# # # # class BibleChapterViewSet(ModelViewSet):
# # # #     queryset = BibleChapter.objects.all()
# # # #     serializer_class = BibleChapterSerializer

# # # #     def get_queryset(self):
# # # #         queryset = super().get_queryset()
# # # #         version = self.request.query_params.get('version')  # Get the version from query parameters
# # # #         if version:
# # # #             queryset = queryset.filter(book__verses__version=version).distinct()  # Filter based on the chosen version
# # # #         return queryset


# # # # # class BibleVerseViewSet(ModelViewSet):
# # # # #     queryset = BibleVerse.objects.all()
# # # # #     serializer_class = BibleVerseSerializer

# # # # #     def get_queryset(self):
# # # # #         queryset = super().get_queryset()
# # # # #         version = self.request.query_params.get('version')  # Get the version from query parameters
# # # # #         if version:
# # # # #             queryset = queryset.filter(version=version) 
# # # # #         return queryset



# # # # class VerseComparisonView(APIView):
# # # #     serializer_class = VerseComparisonSerializer

# # # #     def post(self, request):
# # # #         serializer = self.serializer_class(data=request.data)
# # # #         serializer.is_valid(raise_exception=True)

# # # #         versions = serializer.validated_data['versions']
# # # #         chapter = serializer.validated_data['chapter']
# # # #         verse = serializer.validated_data['verse']

# # # #         verses = []
# # # #         for version in versions:
# # # #             try:
# # # #                 verse_text = BibleVerse.objects.get(version=version, chapter=chapter, content=verse).text
# # # #             except BibleVerse.DoesNotExist:
# # # #                 verse_text = 'Verse not found'
# # # #             verses.append({ 'version': version, 'text': verse_text })

# # # #         return Response(verses)
