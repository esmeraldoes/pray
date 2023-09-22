from rest_framework import serializers
from .models import Church, Community, Team, Membership
from bibleApp.models import CustomUser

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'community']#, 'team_lead', 'members']


class CommunitySerializer(serializers.ModelSerializer):
    # members = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True, required=False)
    # members = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True, required=False, read_only=True)
    teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Community
        exclude = ['members']
        # fields = '__all__'
        

class ChurchSerializer(serializers.ModelSerializer):
    communities = CommunitySerializer(many=True, read_only=True)

    class Meta:
        model = Church
        fields = '__all__'

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'
