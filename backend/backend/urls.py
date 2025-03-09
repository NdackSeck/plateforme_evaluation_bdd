from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from users.views import register_user, login_user, logout_user  # Importez les vues depuis users/views.py
from users.views import register_user, login_user, logout_user, get_csrf_token  # Importez la nouvelle vue

def home(request):
    return HttpResponse("Bienvenue sur la plateforme d'évaluation automatisée des exercices de bases de données !")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Route pour la racine
    path('api/register/', register_user, name='register'),
    path('api/login/', login_user, name='login'),
    path('api/logout/', logout_user, name='logout'),
     path('api/csrf-token/', get_csrf_token, name='csrf_token'),  # Nouvelle route pour le token CSRF
]
