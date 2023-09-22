# community/views.py

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Church

class CreateChurchView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not request.user.email.endswith('.org'):
            return Response({'error': 'Only users with .org emails can create a church.'}, status=status.HTTP_403_FORBIDDEN)

        name = request.data.get('name')
        if not name:
            return Response({'error': 'Church name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        org_email_required = request.data.get('org_email_required', True)

        church = Church.objects.create(name=name, org_email_required=org_email_required)
        return Response({'message': 'Church created successfully.'}, status=status.HTTP_201_CREATED)










































# views.py

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Church, Community, Team
from .serializers import ChurchSerializer, CommunitySerializer, TeamSerializer
# from .permissions import IsChurchAdminOrReadOnly, IsCommunityMemberOrReadOnly, IsTeamLeadOrReadOnly

class ChurchCreateView(generics.CreateAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
    # permission_classes = [permissions.IsAuthenticated, IsChurchAdminOrReadOnly]

class ChurchListView(generics.ListAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer

class CommunityCreateView(generics.CreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated]

class CommunityListView(generics.ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class TeamCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class JoinLeaveCommunityView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, community_id):
        try:
            community = Community.objects.get(id=community_id)
            if request.user not in community.members.all():
                community.members.add(request.user)
                return Response({'message': 'Joined the community successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'You are already a member of this community.'}, status=status.HTTP_400_BAD_REQUEST)
        except Community.DoesNotExist:
            return Response({'message': 'Community not found.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, community_id):
        try:
            community = Community.objects.get(id=community_id)
            if request.user in community.members.all():
                community.members.remove(request.user)
                return Response({'message': 'Left the community successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'You are not a member of this community.'}, status=status.HTTP_400_BAD_REQUEST)
        except Community.DoesNotExist:
            return Response({'message': 'Community not found.'}, status=status.HTTP_404_NOT_FOUND)

class JoinLeaveTeamView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            if request.user not in team.members.all():
                team.members.add(request.user)
                team.team_lead = request.user  # Assign the user as the team lead
                team.save()
                return Response({'message': 'Joined the team successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'You are already a member of this team.'}, status=status.HTTP_400_BAD_REQUEST)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            if request.user in team.members.all():
                team.members.remove(request.user)
                if team.team_lead == request.user:
                    # If the user was the team lead, remove them as the lead
                    team.team_lead = None
                    team.save()
                return Response({'message': 'Left the team successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'You are not a member of this team.'}, status=status.HTTP_400_BAD_REQUEST)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found.'}, status=status.HTTP_404_NOT_FOUND)
