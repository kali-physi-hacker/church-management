from .settings import *


INSTALLED_APPS += ["corsheaders"]
CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]
CSRF_TRUSTED_ORIGINS = ["localhost:3000", "127.0.0.1:3000"]


ALLOWED_HOSTS = ["*"]
SECRET_KEY = "oxbes^t9@8+t!s8898jh!&b1s04aj=s8^0qeg1js8g4iow0(h+"
COOKIE_SECURE = False

DEBUG = True
