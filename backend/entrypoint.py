from time import sleep
from os import getenv

sleep(10)

from django.contrib.auth import get_user_model

User = get_user_model()

USER_DEFAULT_USERNAMES = {
    "email": "admin@gmail.com",
    "username": "admin",
    "phone": "996312312312"
}

DEFAULT_USERNAME = USER_DEFAULT_USERNAMES.get(User.USERNAME_FIELD)
if DEFAULT_USERNAME is None:
    raise ValueError("Unsupported `USERNAME_FIELD`")

DEFAULT_PASSWORD = "admin"

USERNAME = getenv("DJANGO_ADMIN_USERNAME") or DEFAULT_USERNAME
PASSWORD = getenv("DJANGO_ADMIN_PASSWORD") or DEFAULT_PASSWORD

FILTER = {User.USERNAME_FIELD: USERNAME}
if not User.objects.filter(**FILTER).exists():
    User.objects.create_superuser(USERNAME, PASSWORD)
    print("Superuser created")
else:
    print("Superuser already exists!")