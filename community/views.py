from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from .models import Church, Community, Team
from .serializers import *

class ChurchListView(generics.ListCreateAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer

class ChurchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer

class CommunityListView(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class CommunityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class TeamListView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class CreateChurchView(generics.CreateAPIView):
    serializer_class = ChurchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.email.endswith('.org'):
            raise serializers.ValidationError({'error': 'Only users with .org emails can create a church.'})
        serializer.save()

class CreateCommunityView(generics.CreateAPIView):
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.email.endswith('.org'):
            raise serializers.ValidationError({'error': 'Only users with .org emails can create a community.'})
        serializer.save()

class CreateTeamView(generics.CreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.email.endswith('.org'):
            raise serializers.ValidationError({'error': 'Only users with .org emails can create a team.'})
        serializer.save()



# ... (previous code)

class JoinChurchView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        church_id = request.data.get('church_id')
        try:
            church = Church.objects.get(id=church_id)
            user = self.request.user
            user.church = church
            user.save()
            return Response({'message': f'Joined {church.name} church.'})
        except Church.DoesNotExist:
            return Response({'message': 'Invalid church ID.'}, status=400)

class JoinCommunityView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        community_id = request.data.get('community_id')
        try:
            community = Community.objects.get(id=community_id)
            user = self.request.user
            user.community = community
            user.save()
            return Response({'message': f'Joined {community.name} community.'})
        except Community.DoesNotExist:
            return Response({'message': 'Invalid community ID.'}, status=400)

class JoinTeamView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        team_id = request.data.get('team_id')
        try:
            team = Team.objects.get(id=team_id)
            user = self.request.user
            user.team = team
            user.save()
            return Response({'message': f'Joined {team.name} team.'})
        except Team.DoesNotExist:
            return Response({'message': 'Invalid team ID.'}, status=400)









































# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from .models import Church, Community, Team
# from .serializers import ChurchSerializer, CommunitySerializer, TeamSerializer

# class ChurchListCreateView(generics.ListCreateAPIView):
#     queryset = Church.objects.all()
#     serializer_class = ChurchSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(admin=self.request.user)

# class ChurchDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Church.objects.all()
#     serializer_class = ChurchSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class CommunityListCreateView(generics.ListCreateAPIView):
#     serializer_class = CommunitySerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Community.objects.filter(church_id=self.kwargs['church_id'])

#     def perform_create(self, serializer):
#         church = Church.objects.get(id=self.kwargs['church_id'])
#         serializer.save(church=church)

# class CommunityDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Community.objects.all()
#     serializer_class = CommunitySerializer
#     permission_classes = [permissions.IsAuthenticated]

# class TeamListCreateView(generics.ListCreateAPIView):
#     serializer_class = TeamSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Team.objects.filter(community_id=self.kwargs['community_id'])

#     def perform_create(self, serializer):
#         community = Community.objects.get(id=self.kwargs['community_id'])
#         serializer.save(community=community)

# class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer
#     permission_classes = [permissions.IsAuthenticated]






























# # views.py

# from rest_framework import generics, status, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Church, Community, Team
# from .serializers import ChurchSerializer, CommunitySerializer, TeamSerializer
# from .permissions import IsChurchAdminOrReadOnly, IsCommunityMemberOrReadOnly, IsTeamLeadOrReadOnly



# class ChurchCreateView(generics.CreateAPIView):
#     queryset = Church.objects.all()
#     serializer_class = ChurchSerializer
#     permission_classes = [permissions.IsAuthenticated, IsChurchAdminOrReadOnly]

#     def perform_create(self, serializer):
#         # Check if the user's email ends with .org
#         user = self.request.user
#         if user.email.endswith('.org'):
#             # If the user has a .org email, allow creating the church
#             serializer.save(admin=user)
#         else:
#             # If the user does not have a .org email, return an error response
#             return Response({'message': 'Only users with .org email addresses can create a church.'}, status=status.HTTP_400_BAD_REQUEST)



# class ChurchListView(generics.ListAPIView):
#     queryset = Church.objects.all()
#     serializer_class = ChurchSerializer

# class CommunityCreateView(generics.CreateAPIView):
#     queryset = Community.objects.all()
#     serializer_class = CommunitySerializer
#     permission_classes = [permissions.IsAuthenticated]

# class CommunityListView(generics.ListAPIView):
#     queryset = Community.objects.all()
#     serializer_class = CommunitySerializer

# class TeamCreateView(generics.CreateAPIView):
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class TeamListView(generics.ListAPIView):
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer

# class JoinLeaveCommunityView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, community_id):
#         try:
#             community = Community.objects.get(id=community_id)
#             if request.user not in community.members.all():
#                 community.members.add(request.user)
#                 return Response({'message': 'Joined the community successfully.'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'You are already a member of this community.'}, status=status.HTTP_400_BAD_REQUEST)
#         except Community.DoesNotExist:
#             return Response({'message': 'Community not found.'}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, community_id):
#         try:
#             community = Community.objects.get(id=community_id)
#             if request.user in community.members.all():
#                 community.members.remove(request.user)
#                 return Response({'message': 'Left the community successfully.'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'You are not a member of this community.'}, status=status.HTTP_400_BAD_REQUEST)
#         except Community.DoesNotExist:
#             return Response({'message': 'Community not found.'}, status=status.HTTP_404_NOT_FOUND)

# class JoinLeaveTeamView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, team_id):
#         try:
#             team = Team.objects.get(id=team_id)
#             if request.user not in team.members.all():
#                 team.members.add(request.user)
#                 team.team_lead = request.user  # Assign the user as the team lead
#                 team.save()
#                 return Response({'message': 'Joined the team successfully.'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'You are already a member of this team.'}, status=status.HTTP_400_BAD_REQUEST)
#         except Team.DoesNotExist:
#             return Response({'message': 'Team not found.'}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, team_id):
#         try:
#             team = Team.objects.get(id=team_id)
#             if request.user in team.members.all():
#                 team.members.remove(request.user)
#                 if team.team_lead == request.user:
#                     # If the user was the team lead, remove them as the lead
#                     team.team_lead = None
#                     team.save()
#                 return Response({'message': 'Left the team successfully.'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'You are not a member of this team.'}, status=status.HTTP_400_BAD_REQUEST)
#         except Team.DoesNotExist:
#             return Response({'message': 'Team not found.'}, status=status.HTTP_404_NOT_FOUND)
