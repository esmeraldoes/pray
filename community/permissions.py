from rest_framework import permissions
from .models import Church, Community

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

class IsChurchAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        church_id = view.kwargs.get('church_id')
        church = Church.objects.get(id=church_id)
        return request.user == church.admin

class IsCommunityMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        community_id = view.kwargs.get('community_id')
        community = Community.objects.get(id=community_id)
        return request.user in community.members.all()
    
# class IsCommunityMemberOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         community_id = view.kwargs.get('community_id')
#         community = Community.objects.get(id=community_id)
#         return request.user in community.members.all() or request.user.is_staff


























# # # models.py
# # from django.contrib.auth.models import AbstractUser, Group, Permission
# # from django.db import models

# # # class CustomUser(AbstractUser):
# #     # Add fields and methods relevant to users

# # class Church(models.Model):
# #     name = models.CharField(max_length=100)
# #     creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_churches')
# #     members = models.ManyToManyField(CustomUser, related_name='churches_joined')
# #     # Other church fields

# # class Community(models.Model):
# #     name = models.CharField(max_length=100)
# #     church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name='communities')
# #     members = models.ManyToManyField(CustomUser, related_name='communities_joined')
# #     creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_communities')
# #     # Other community fields

# # class Team(models.Model):
# #     name = models.CharField(max_length=100)
# #     community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='teams')
# #     creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_teams')
# #     members = models.ManyToManyField(CustomUser, related_name='teams_joined')
# #     team_lead = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='leading_teams')
# #     # Other team fields

# # # permissions.py
# # from django.contrib.auth.models import Permission
# # from django.contrib.contenttypes.models import ContentType
# # from django.db.models import Q

# # def create_custom_permissions():
# #     # Define custom permissions for church admins
# #     church_content_type = ContentType.objects.get_for_model(Church)
# #     custom_permissions = [
# #         Permission.objects.create(
# #             codename='can_create_community',
# #             name='Can create community',
# #             content_type=church_content_type,
# #         ),
# #         Permission.objects.create(
# #             codename='can_delete_community',
# #             name='Can delete community',
# #             content_type=church_content_type,
# #         ),
# #     ]

# #     # Assign custom permissions to a group (church admins)
# #     church_admins, _ = Group.objects.get_or_create(name='Church Admins')
# #     church_admins.permissions.add(*custom_permissions)

# #     # Create a superuser with church admin privileges
# #     superuser = CustomUser.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
# #     superuser.groups.add(church_admins)

# #     # Define custom permissions for team leads
# #     team_content_type = ContentType.objects.get_for_model(Team)
# #     custom_permissions = [
# #         Permission.objects.create(
# #             codename='can_manage_team',
# #             name='Can manage team',
# #             content_type=team_content_type,
# #         ),
# #     ]

# #     # Assign custom permissions to a group (team leads)
# #     team_leads, _ = Group.objects.get_or_create(name='Team Leads')
# #     team_leads.permissions.add(*custom_permissions)

# # create_custom_permissions()

# # permissions.py
# from rest_framework import permissions

# class IsChurchAdminOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # Check if the user is a church admin
#         return request.user.is_authenticated and request.user.is_church_admin

# class IsCommunityMemberOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # Check if the user is a member of the community to which the object belongs
#         return request.user.is_authenticated and obj.members.filter(id=request.user.id).exists()

# class IsTeamLeadOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # Check if the user is the team lead or a church admin
#         return request.user.is_authenticated and (obj.team_lead == request.user or request.user.is_church_admin)
