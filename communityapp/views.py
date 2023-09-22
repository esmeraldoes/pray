from rest_framework import generics, status
from rest_framework.response import Response
from .models import Church, Community, Team, Membership

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from communityapp.serializers import ChurchSerializer, CommunitySerializer, TeamSerializer, MembershipSerializer

from django.shortcuts import get_object_or_404





class ChurchListView(generics.ListAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer

class CreateChurchView(APIView):
    serializer_class = ChurchSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        if not request.user.email.endswith('.org'):
            return Response({"message": "Only users with .org email addresses can create a church. Please contact the Django admin for assistance."}, status=status.HTTP_403_FORBIDDEN)
        
        # serializer = ChurchSerializer(data=request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(admin=self.request.user)
            # serializer.save(admin=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ADDJoinChurchView(generics.UpdateAPIView):
    serializer_class = ChurchSerializer

    def get_object(self):
        church_id = self.kwargs.get('pk')
        return Church.objects.get(id=church_id)

    def update(self, request, *args, **kwargs):
        church = self.get_object()
        user = self.request.user

        
        church.members.add(user)
        church.save()

        return Response({"message": f"You joined {church.name}"}, status=status.HTTP_200_OK)
    

class JoinChurchView(APIView):
    serializer_class = MembershipSerializer
    def post(self, request, name, format=None):
        try:
            church = Church.objects.get(name=name)
        except Church.DoesNotExist:
            return Response({"message": "Church not found."}, status=status.HTTP_404_NOT_FOUND)

        if Membership.objects.filter(user=request.user, church=church).exists():
            return Response({"message": "You are already a member of this church."}, status=status.HTTP_400_BAD_REQUEST)

        Membership.objects.create(user=request.user, church=church)

        return Response({"message": "You have successfully joined the church."}, status=status.HTTP_201_CREATED)

class CreateCommunityView(CreateAPIView):
    serializer_class = CommunitySerializer

    def perform_create(self, serializer):
        church_id = self.kwargs['church_id']
        church = get_object_or_404(Church, id=church_id)
        user = self.request.user

        is_admin = Membership.objects.filter(user=user, church=church, is_admin=True).exists()

        community = serializer.save(church=church)

        
        if is_admin:
            Membership.objects.create(user=user, community=community, is_admin=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateTeamView(CreateAPIView):
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        community_id = self.request.data.get('community')
        community = get_object_or_404(Community, id=community_id)
        user = self.request.user

        
        is_admin = Membership.objects.filter(user=user, church=community.church, is_admin=True).exists()

        team = serializer.save(community=community)


        if is_admin:
            team.members.add(user)
            team.team_lead = user
            team.save()



class CommunityListView(generics.ListAPIView):
    serializer_class = CommunitySerializer

    def get_queryset(self):
        church_id = self.kwargs.get('church_pk')
        if church_id:
            return Community.objects.filter(church_id=church_id)
        return Community.objects.all()
        

class JoinCommunityView(CreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def perform_create(self, serializer):
        community_id = self.request.data.get('community_id')
        if Membership.objects.filter(user=self.request.user, community_id=community_id).exists():
            return Response({"message": "You are already a member of this community."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=self.request.user, community_id=community_id)

class ADDJoinCommunityView(generics.UpdateAPIView):
    serializer_class = CommunitySerializer

    def get_object(self):
        community_id = self.kwargs.get('pk')
        return Community.objects.get(id=community_id)

    def update(self, request, *args, **kwargs):
        community = self.get_object()
        user = self.request.user

        community.members.add(user)
        community.save()

        return Response({"message": f"You joined {community.name}"}, status=status.HTTP_200_OK)

class TeamListView(generics.ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        community_id = self.kwargs.get('community_pk')
        return Team.objects.filter(community_id=community_id)

class ADDJoinTeamView(generics.UpdateAPIView):
    serializer_class = TeamSerializer

    def get_object(self):
        team_id = self.kwargs.get('pk')
        return Team.objects.get(id=team_id)

    def update(self, request, *args, **kwargs):
        team = self.get_object()
        user = self.request.user

        team.members.add(user)
        team.save()

        return Response({"message": f"You joined {team.name}"}, status=status.HTTP_200_OK)
    

class JoinTeamView(CreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def perform_create(self, serializer):
        team_id = self.request.data.get('team_id')
        if Membership.objects.filter(user=self.request.user, team_id=team_id).exists():
            return Response({"message": "You are already a member of this team."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=self.request.user, team_id=team_id)

class CommunityMembersView(generics.ListAPIView):
    serializer_class = CommunitySerializer

    def get_queryset(self):
        community_id = self.kwargs.get('pk')
        return Community.objects.filter(id=community_id).select_related('members__customuser')

class TeamMembersView(generics.ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        team_id = self.kwargs.get('pk')
        return Team.objects.filter(id=team_id).select_related('members__customuser')

