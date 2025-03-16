from django.contrib import admin
from django.urls import path
from django.shortcuts import render  # Ajouter cette ligne

from users.views import register_user, login_user, logout_user, get_csrf_token  # Import correct des vues
from users.views import afficher_inscription, afficher_connexion  # Import des vues pour l'affichage des pages HTML

# Vue pour la page d'accueil
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),  # Route pour l'administration Django
    path('', home, name='home'),  # Route pour la racine de l'application
    path('api/register/', register_user, name='register'),  # Route pour l'inscription (API)
    path('api/login/', login_user, name='login'),  # Route pour la connexion (API)
    path('api/logout/', logout_user, name='logout'),  # Route pour la déconnexion (API)
    path('api/csrf-token/', get_csrf_token, name='csrf_token'),  # Route pour récupérer le token CSRF

    # Routes pour afficher les formulaires HTML
    path('register/', afficher_inscription, name='inscription'),  # Page d'inscription
    path('login/', afficher_connexion, name='connexion'),  # Page de connexion
]
