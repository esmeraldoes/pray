# # swagger.py

# from drf_spectacular.utils import extend_schema
# from drf_spectacular.settings import spectacular_settings
# from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme
# from drf_spectacular.extensions import OpenApiAuthenticationExtension

# @spectacular_settings.postprocess_schema()
# def add_authentication_extension(schema, request, public):
#     if not public:
#         schema['components']['securitySchemes']['JWTAuth'] = SimpleJWTScheme

#     return schema

# @spectacular_settings.postprocess_schema()
# def add_authentication_security(schema, request, public):
#     if not public:
#         schema['security'] = [{'JWTAuth': []}]

#     return schema

# @extend_schema(
#     description="API Root",
#     tags=["API Root"]
# )
# def api_root(request):
#     return {}



























SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '802944885729-5p6m0ku0hgmbirpgguai9s794lppqgui.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


SOCIAL_AUTH_FACEBOOK_KEY = '1450115019174104'
SOCIAL_AUTH_FACEBOOK_SECRET = '0ed8e65c4e050522b27e684b20653c4c'
