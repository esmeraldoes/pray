from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import bible_server
from django.urls import path
from dbibles import views



# from .views import GetBibleVersions, GetBibleVersionsView4, GetBooksInVersion, GetChaptersInBook, GetVerseInChapter, CompareVerses,  BibleVersionViewSet, BibleBookViewSet, BibleChapterViewSet, BibleVerseViewSet, getVerseComparison

# router = DefaultRouter()
# router.register(r'bible-versions', BibleVersionViewSet, basename='bible-version')
# router.register(r'bible-books', BibleBookViewSet, basename='bible-book')
# router.register(r'bible-chapters', BibleChapterViewSet, basename='bible-chapter')
# router.register(r'bible-verses', BibleVerseViewSet, basename='bible-verse')
# # from .views import get_bible_versions

urlpatterns =[
    path('getversion4/', views.grpc_serve, name='get_bible_versions4'), 

]
# urlpatterns = [
#     path('read/', include(router.urls)),
#     path('verse-comparison/', getVerseComparison.as_view(), name='verse-comparison'),
#     path('get-bible-versions/', get_bible_versions, name='get_bible_versions'),
#     path('getversion4/', GetBibleVersionsView4, name='get_bible_versions4'),
    
#     # path('get-bible-versions', GetBibleVersionsView.as_view()),

#     # path('documentation/', views.documentation, name='documentation'),
#     # path('grpc_swagger/', views.grpc_swagger, name='grpc_swagger'),
#     path('api/grpc/bible-versions/', GetBibleVersions.as_view(), name='get_bible_versions'),
#     path('api/grpc/bible-books/', GetBooksInVersion.as_view(), name='get_books_in_version'),
#     path('api/grpc/bible-chapters/', GetChaptersInBook.as_view(), name='get_chapters_in_book'),
#     path('api/grpc/bible-verses/', GetVerseInChapter.as_view(), name='get_verse_in_chapter'),
#     path('api/grpc/compare-verses/', CompareVerses.as_view(), name='compare_verses'),
#     path('grpc/', bible_server.serve, name='grpc-serve'),
# ]




































# # from django.urls import path, include
# # from rest_framework import routers
# # from .views import import_bible_data

# # # router = routers.DefaultRouter()
# # # router.register(r'bible-versions', BibleVersionViewSet)

# # urlpatterns = [
# #     path('import-bible-data/', import_bible_data, name='import_bible_data'),
# #     # path('api/', include(router.urls)),
# # ]
# # from django.urls import path
# # from .views import BibleVerseListAPIView, BibleChapterListAPIView, BibleBookListAPIView

# # urlpatterns = [
# #     path('verses/', BibleVerseListAPIView.as_view(), name='verses-list'),
# #     path('chapters/', BibleChapterListAPIView.as_view(), name='chapters-list'),
# #     path('books/', BibleBookListAPIView.as_view(), name='books-list'),
# # ]



# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# # from .views import (BibleViewSet, BibleChapterViewSet, BibleVerseListAPIView, BibleChapterVerseList, BibleChapterListAPIView, BibleBookListAPIView, ChapterVersesAPIView, VerseComparisonView, VersionListView)

# # router = DefaultRouter()
# # # router.register('chapters', BibleChapterViewSet, basename='chapter')
# # # router.register(r'chapters', BibleChapterViewSet)
# # # router.register('verses', BibleVerseViewSet, basename='verse')
# # router.register(r'bibles', BibleViewSet, basename='bible')
# # # router.register(r'chapters', BibleChapterViewSet, basename='chapter')
# # # router.register(r'verses', BibleVerseViewSet, basename='verse')

# # from .views import VersionListView

# from django.urls import path, include
# from rest_framework import routers
# from .views import VersionListView


# from .views import BibleChapterView1, BibleBookListView, BibleBookListAPIView, BibleBookViewSet
# # from .views import BibleVersionViewSet, BibleChapterView, BibleVerseView, BibleChapterView1

# # from .views import BibleVersionList, BibleBookList, BibleChapterList, BibleVerseList, BibleVerseDetail, import_bible_data

# # router = routers.DefaultRouter()
# # router.register(r'bible-versions', BibleVersionViewSet)
# # # router.register(r'bible', BibleViewSet)


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BibleBookViewSet, biblevesion

# router = DefaultRouter()
# router.register(r'bible-books', BibleBookViewSet, basename='bible-book')
# router.register(r'bible-versions', BibleVersionViewSet, basename='bible-version')


# urlpatterns = [
#     # path('api/', namez)
#     path('version/', VersionListView.as_view()),
#     path('read/<str:version_name>', BibleBookListView.as_view()),
#     path('books/', BibleBookListAPIView.as_view(), name='books-list'),
#     path('reader/', include(router.urls)),
#     # path('bibleread/', BibleBookViewSet, name='books-read'),

    
#     # path('chapters/<str:version>/books/<str:book>/chapters/<int:chapter>/verses/', BibleChapterView.as_view(), name='chapter-verses'),
# # #    
#     # path('api/', include(router.urls)),
#     path('chapters/<str:version>/', BibleChapterView1.as_view(), name='bible-chapter-list'),
#     # path('verses/', BibleVerseView.as_view(), name='verse-list'),

#     # path('versions/', BibleVersionList.as_view(), name='version-list'),
#     # path('versions/<str:version>/books/', BibleBookList.as_view(), name='book-list'),
#     # path('versions/<str:version>/books/<str:book>/chapters/', BibleChapterList.as_view(), name='chapter-list'),
#     # path('versions/<str:version>/books/<str:book>/chapters/<int:chapter>/verses/', BibleVerseList.as_view(), name='verse-list'),
#     # path('versions/<str:version>/books/<str:book>/chapters/<int:chapter>/verses/<int:verse>/', BibleVerseDetail.as_view(), name='verse-detail'),

#     # path('import-bible/', import_bible_data, name='bible_data')



#     # path('versions/', BibleVersionListView.as_view(), name='version-list'),
#     # path('versions/<str:version_name>/books/', BibleBookListView.as_view(), name='book-list'),
#     # path('versions/<str:version_name>/books/<str:book_name>/chapters/', BibleChapterListView.as_view(), name='chapter-list'),
#     # path('versions/<str:version_name>/books/<str:book_name>/chapters/<int:chapter_number>/verses/', BibleVerseListView.as_view(), name='verse-list'),


#     # path('chapters/', BibleChapterView1.as_view(), name='chapter-list'),

#     # path('chapters/', BibleChapterView.as_view(), name='bible-chapters'),
#     # path('api2/chapters/', BibleChapterView.as_view(), name='chapter-list'),
# #     path('api2/<str:version>/books/<str:book>/chapters/<int:chapter>/verses/', BibleChapterView.as_view(), name='chapter-verses'),
# # #    
# #     path('api2/chapters/<str:version>/', BibleChapterView.as_view(), name='chapter-list-by-version'),

# #     path('api2/verses/<str:version>/<str:book>/<int:chapter>/<int:verse>/', BibleVerseView.as_view(), name='verse-detail'),
# #     path('api2/chapters/<str:version>/<str:book>/<int:chapter>/', BibleChapterView.as_view(), name='chapter-verse-list'),

#     # path('api2/verses/<str:version>/<str:book>/<int:chapter>/<int:verse>/', BibleVerseView.as_view(), name='verse-detail'),
#     # path('api2/verses/<str:version>/<str:book>/<int:chapter>/', BibleChapterView.as_view(), name='chapter-verse-list'),

#     # path('chapters/<int:chapter_number>/', BibleChapterView.as_view(), name='bible-chapter-detail'),
# ]



# # urlpatterns = [
# #     # path('', include(router.urls)),
# #     # path('verses_list/', BibleVerseListAPIView.as_view(), name='verses-list'),
# #     # path('chapters_list/', BibleChapterListAPIView.as_view(), name='chapters-list'),
# #     # path('books_list/', BibleBookListAPIView.as_view(), name='books-list'),
# #     # path('api2/<str:version>/books/<str:book>/chapters/<int:chapter>/verses/', ChapterVersesAPIView.as_view(), name='chapter-verses'),
# #     #  path('chapters/<int:chapter_id>/verses/', BibleChapterVerseList.as_view(), name='chapter-verses'),##
# #     # path('api/verse-comparison/', VerseComparisonView.as_view(), name='verse-comparison'),
# #     path('versions/', VersionListView.as_view(), name='version-list'),
    
 







