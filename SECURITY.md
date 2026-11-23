# Security Policy

## Supported Versions

This is a learning / personal project. Security fixes are applied to the `main` branch only.

## Reporting a Vulnerability

If you discover a security issue, please open a private security advisory on GitHub or contact the repository owner.

Do **not** open a public issue for sensitive reports.

## Known Hardening Steps Already Taken

- `DJANGO_SECRET_KEY` is required from the environment; the app will not start without it.
- `DEBUG` defaults to `False` and is controlled via `DJANGO_DEBUG`.
- Database credentials / connection string come from `DATABASE_URL` (or local SQLite).
- Production settings enable HTTPS redirect, secure cookies, HSTS, and related headers when `DEBUG` is False.
- User content is ownership-checked in views; CSRF protection is enabled.

## Important Notes for Operators

1. **Never commit** `db.sqlite3`, `.env`, or any file containing secrets.
2. If a database or secret was ever committed, **rotate all passwords and the Django secret key** immediately and purge the sensitive data from git history (e.g. `git filter-repo` or BFG).
3. On Render (or similar), use a managed Postgres instance and set `DATABASE_URL`. The free-tier filesystem is ephemeral.
4. Generate a fresh secret key for every environment:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

## Disclaimer

This service and its developer accept no liability for any damage arising from use of the application.
