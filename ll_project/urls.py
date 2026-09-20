from django.contrib import admin
from django.urls import path, include
from learning_logs.views import google_verification

urlpatterns = [
    path('google123456789.html', google_verification), # use your exact filename
    # ... your existing paths ...
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('learning_logs.urls')),
]