from rest_framework import serializers
from community.models import Church, Community, Team, TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class CommunitySerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Community
        fields = '__all__'

class ChurchSerializer(serializers.ModelSerializer):
    communities = CommunitySerializer(many=True, read_only=True)

    class Meta:
        model = Church
        fields = '__all__'
