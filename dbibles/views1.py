from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BibleBook, BibleChapter, BibleVerse
from .serializers import BibleBookSerializer, BibleChapterSerializer, BibleVerseSerializer, VerseComparisonSerializer


class ChapterVersesAPIView(generics.ListAPIView):
    serializer_class = BibleVerseSerializer

    def get_queryset(self):
        version = self.kwargs['version']
        book = self.kwargs['book']
        chapter = self.kwargs['chapter']
        
        queryset = BibleVerse.objects.filter(chapter__book__name=book, chapter__number=chapter, version=version)
        return queryset


class BibleVerseListAPIView(generics.ListAPIView):
    serializer_class = BibleVerseSerializer
    # pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = BibleVerse.objects.all()
        chapter_id = self.request.query_params.get('chapter_id')
        book_id = self.request.query_params.get('book_id')
        if chapter_id:
            queryset = queryset.filter(chapter_id=chapter_id)
        if book_id:
            queryset = queryset.filter(chapter__book_id=book_id)
        return queryset

class BibleChapterListAPIView(generics.ListAPIView):
    serializer_class = BibleChapterSerializer
    # pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = BibleChapter.objects.all()
        book_id = self.request.query_params.get('book_id')
        if book_id:
            queryset = queryset.filter(book_id=book_id)
        return queryset

class BibleBookListAPIView(generics.ListAPIView):
    serializer_class = BibleBookSerializer
    # pagination_class = PageNumberPagination
    queryset = BibleBook.objects.all()


from rest_framework.generics import ListAPIView
from .models import BibleVersion
from .serializers import VersionSerializer

class VersionListView(ListAPIView):
    queryset = BibleVersion.objects.all()
    serializer_class = VersionSerializer












from rest_framework.viewsets import ModelViewSet
from .serializers import BibleBookSerializer, BibleChapterSerializer, BibleVerseSerializer
from .models import BibleBook, BibleChapter, BibleVerse

class BibleViewSet(ModelViewSet):
    queryset = BibleBook.objects.all()
    serializer_class = BibleBookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        version = self.request.query_params.get('version')  # Get the version from query parameters
        if version:
            queryset = queryset.filter(verses__version=version).distinct()  # Filter based on the chosen version
        return queryset


class BibleChapterViewSet(ModelViewSet):
    queryset = BibleChapter.objects.all()
    serializer_class = BibleChapterSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        version = self.request.query_params.get('version')  # Get the version from query parameters
        if version:
            queryset = queryset.filter(book__verses__version=version).distinct()  # Filter based on the chosen version
        return queryset


# class BibleVerseViewSet(ModelViewSet):
#     queryset = BibleVerse.objects.all()
#     serializer_class = BibleVerseSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         version = self.request.query_params.get('version')  # Get the version from query parameters
#         if version:
#             queryset = queryset.filter(version=version) 
#         return queryset



class VerseComparisonView(APIView):
    serializer_class = VerseComparisonSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        versions = serializer.validated_data['versions']
        chapter = serializer.validated_data['chapter']
        verse = serializer.validated_data['verse']

        verses = []
        for version in versions:
            try:
                verse_text = BibleVerse.objects.get(version=version, chapter=chapter, content=verse).text
            except BibleVerse.DoesNotExist:
                verse_text = 'Verse not found'
            verses.append({ 'version': version, 'text': verse_text })

        return Response(verses)
