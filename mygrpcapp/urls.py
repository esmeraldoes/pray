# mygrpcapp/urls.py
from django.urls import path




from django.urls import path
from . import views

urlpatterns = [
    path('grpc_server/', views.grpc_serve, name='grpc-serve'),
    # Endpoint to get a list of Bible versions
    path('bible/versions/', views.BibleVersionsView.as_view(), name='bible-versions'),

    # Endpoint to get a list of books in a specific Bible version
    path('bible/books/', views.BibleBooksView.as_view(), name='bible-books'),

    # Endpoint to get a list of chapters in a specific book
    path('bible/chapters/<str:version>/<str:book>/', views.BibleChaptersView.as_view(), name='bible-chapters'),

    # Endpoint to get a list of verses in a specific chapter
    path('bible/verses/<str:version>/<str:book>/<int:chapter>/', views.BibleVersesView.as_view(), name='bible-verses'),
    # path('bible/verses/', views.BibleVersesView.as_view(), name='bible-verses'),
    path('compare-verse/', views.CompareVerseView.as_view(), name='compare-verse'),
    path('compare-verses/<str:versions>/<str:books>/<int:chapters>/<str:verses>/', views.CompareVersesView.as_view(), name='compare-verses'),



    # Endpoint to get a specific verse
    # path('bible/verse/', views.BibleVerseView.as_view(), name='bible-verse'),
    # path('bible/verse/<int:chapter>/<int:verse>/', views.BibleVerseView.as_view(), name='verse-detail'),
    path('bible/verse/<str:version>/<str:book>/<int:chapter>/<int:verse>/', views.BibleVerseView.as_view(), name='verse-detail')
    # path('bible/verse/<str:version>/<str:book>/<int:chapter>/<int:verse>/', views.BibleVerseView.as_view(), name='verse-detail')


]



# # urls.py
# from django.urls import path
# from . import views


# urlpatterns = [
#     path('api/grpc_server/', views.grpc_serve, name='grpc-serve'),
#     path('chapters/', views.ChapterListView.as_view(), name='chapter-list'),
#     path('verse_numbers/', views.VerseListView.as_view(), name='verse-number-list'),
#     path('verse/<int:chapter>/<int:verse>/', views.VerseDetailView.as_view(), name='verse-detail'),
# ]

















# from .views import grpc_proxy, grpc_serve, get_books_in_version, get_chapters_in_book, get_specific_verse, get_verse_numbers_in_chapter, get_all_verses_in_chapter

# urlpatterns = [
#     path('api/grpc_server/', grpc_serve, name='grpc-serve'),
#     path('api/grpc/', grpc_proxy, name='grpc-s'),
#     path('api/books/', get_books_in_version, name='get-books'),
#     path('api/chapter/', get_chapters_in_book, name='get-chapter'),
#     path('api/verse/', get_specific_verse, name='get-verse'),
#     path('api/verses/', get_all_verses_in_chapter, name='get-verses'),
#     # path('api/verse_numbers/', get_verse_numbers_in_chapter, name='get-verse-number'),
# ]


