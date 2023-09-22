from django.urls import path
from . import views



urlpatterns = [
    # path('grpc_server/', views.grpc_serve, name='grpc-serve'),
    
    path('versions/', views.BibleVersionsView.as_view(), name='bible-versions'),
    
    path('books/', views.BibleBooksView.as_view(), name='bible-books'),
   
    path('chapters/<str:version>/<str:book>/', views.BibleChaptersView.as_view(), name='bible-chapters'),

    path('verses/<str:version>/<str:book>/<int:chapter>/', views.BibleVersesView.as_view(), name='bible-verses'),
    # path('bible/verses/', views.BibleVersesView.as_view(), name='bible-verses'),
    path('compare-verse/', views.CompareVerseView.as_view(), name='compare-verse'),
    path('compare-verses/<str:versions>/<str:books>/<int:chapters>/<str:verses>/', views.CompareVersesView.as_view(), name='compare-verses'),
    path('verse/<str:version>/<str:book>/<int:chapter>/<int:verse>/', views.BibleVerseView.as_view(), name='verse-detail'),
    
]

