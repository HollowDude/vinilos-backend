from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class SameSiteSecureCookieMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Configura `_auth` y `_refresh` cookies con SameSite=None y Secure=True
        auth_cookie = settings.REST_AUTH.get("JWT_AUTH_COOKIE", "_auth")
        refresh_cookie = settings.REST_AUTH.get("JWT_AUTH_REFRESH_COOKIE", "_refresh")
        
        for cookie_name in [auth_cookie, refresh_cookie]:
            if cookie_name in response.cookies:
                response.cookies[cookie_name]["samesite"] = "None"
                response.cookies[cookie_name]["secure"] = True
        return response
