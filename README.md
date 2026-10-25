# Learning Log

## Configuration

The Django signing key must be supplied through `DJANGO_SECRET_KEY`. Generate a
new key with:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Set `DJANGO_DEBUG=true` only for local development. It defaults to `false`.
`DJANGO_ALLOWED_HOSTS` accepts a comma-separated list and defaults to
`localhost,127.0.0.1,[::1]`.

For a local PowerShell session:

```powershell
$env:DJANGO_SECRET_KEY = "paste-a-newly-generated-key-here"
$env:DJANGO_DEBUG = "true"
python manage.py runserver
```

Use a new, private key in each deployment environment. Rotate the key that was
previously present in the repository; removing it from the current source does
not remove it from repository history.

## Tests

```powershell
$env:DJANGO_SECRET_KEY = "test-only-secret-key"
python manage.py test
```
