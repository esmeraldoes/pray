from django.urls import path
from .views import (
    ChurchListView,
    CreateChurchView,
    JoinChurchView,
    CommunityListView,
    JoinCommunityView,
    TeamListView,
    JoinTeamView,
    CommunityMembersView,
    TeamMembersView,
    ADDJoinChurchView,
    ADDJoinCommunityView,
    ADDJoinTeamView,
    CreateTeamView,
    CreateCommunityView,
)

urlpatterns = [
    path('create_church/', CreateChurchView.as_view(), name='create_church'),
    path('churches/', ChurchListView.as_view(), name='church-list'),
    path('churches/<int:pk>/join/', ADDJoinChurchView.as_view(), name='join-church'),
    path('churches/<int:church_pk>/communities/', CommunityListView.as_view(), name='community-list'),
    path('communities/<int:pk>/join/', ADDJoinCommunityView.as_view(), name='join-community'),
    path('communities/<int:community_pk>/teams/', TeamListView.as_view(), name='team-list'),
    path('teams/<int:pk>/join/', ADDJoinTeamView.as_view(), name='join-team'),
    path('communities/<int:pk>/members/', CommunityMembersView.as_view(), name='community-members'),
    path('teams/<int:pk>/members/', TeamMembersView.as_view(), name='team-members'),

    path('create_community/<int:church_id>/', CreateCommunityView.as_view(), name='create_community'),

    path('create_team/', CreateTeamView.as_view(), name='create_team'), 
    path('churches/<str:name>/join/', JoinChurchView.as_view(), name='join_church'),
    path('join_community/', JoinCommunityView.as_view(), name='join_community'),
    path('join_team/', JoinTeamView.as_view(), name='join_team'),
]




