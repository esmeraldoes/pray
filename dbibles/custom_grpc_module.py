# # from grpc import UnaryUnaryClientInterceptor
# from . import bible_service_pb2_grpc
# # from bible_service_pb2_grpc import BibleServiceStub
# from . import bible_service_pb2
# # import bible_service_pb2
# from .models import BibleVersion

# class BibleServiceCustomClient(bible_service_pb2_grpc.BibleServiceStub):

#     def GetBibleVersions(self, request, context):
#         """
#         Get a list of all the Bible versions.
#         """
#         response = bible_service_pb2.BibleVersionList()
#         for version in BibleVersion.objects.all():
#             response.versions.append(bible_service_pb2.BibleVersion(
#                 name=version.name
#             ))
#         return response

