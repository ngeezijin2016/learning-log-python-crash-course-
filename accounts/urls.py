from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default auth urls (login, logout, password_change, etc.)
    path('', include('django.contrib.auth.urls')),
    path('create_ll_account/', views.register, name='register'),
]