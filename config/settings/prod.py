from .base import *

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_secret("SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = get_secret("ALLOWED_HOSTS")

SITE_ID = 1

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": get_secret("DB_PROD")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379",
#     }
# }

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-x-forwarded-host
# USE_X_FORWARDED_HOST = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-host
SECURE_SSL_HOST = True
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = True

# TEMPLATES
# ------------------------------------------------------------------------------


# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
# EMAIL_HOST = get_secret("EMAIL_HOST")
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
# EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
# EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
# EMAIL_PORT = 465
# https://docs.djangoproject.com/en/dev/ref/settings/#email-use-ssl
# EMAIL_USE_SSL = True
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
# SERVER_EMAIL = get_secret("SERVER_EMAIL")
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
# DEFAULT_FROM_EMAIL = get_secret("DEFAULT_FROM_EMAIL")

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = get_secret("DJANGO_ADMIN_URL")

# LOGGING
# ------------------------------------------------------------------------------
