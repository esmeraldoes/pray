from django.urls import path
from .views import (
    ChurchListView, ChurchDetailView,
    CommunityListView, CommunityDetailView,
    TeamListView, TeamDetailView,
    CreateChurchView, CreateCommunityView, CreateTeamView, JoinChurchView, JoinCommunityView, JoinTeamView
)

urlpatterns = [
    path('churches/', ChurchListView.as_view(), name='church-list'),
    path('churches/<int:pk>/', ChurchDetailView.as_view(), name='church-detail'),
    path('communities/', CommunityListView.as_view(), name='community-list'),
    path('communities/<int:pk>/', CommunityDetailView.as_view(), name='community-detail'),
    path('teams/', TeamListView.as_view(), name='team-list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('churches/create/', CreateChurchView.as_view(), name='create-church'),
    path('communities/create/', CreateCommunityView.as_view(), name='create-community'),
    path('teams/create/', CreateTeamView.as_view(), name='create-team'),
    path('churches/join/', JoinChurchView.as_view(), name='join-church'),
    path('communities/join/', JoinCommunityView.as_view(), name='join-community'),
    path('teams/join/', JoinTeamView.as_view(), name='join-team'),

]
