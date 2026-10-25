import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ll_project.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if password:
    user, created = User.objects.get_or_create(username=username, defaults={"email": email})
    user.is_superuser = True
    user.is_staff = True
    user.set_password(password)
    user.save()
    print(f"Successfully updated superuser: {username}")
else:
    print("DJANGO_SUPERUSER_PASSWORD variable not set.")