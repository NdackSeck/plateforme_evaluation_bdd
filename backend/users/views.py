from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.middleware.csrf import get_token


# Vues pour rendre les pages HTML d'inscription et de connexion
def afficher_inscription(request):
    return render(request, 'inscription.html')


def afficher_connexion(request):
    return render(request, 'connexion.html')


# Vues API pour l'inscription, la connexion, et la déconnexion

@api_view(['POST'])
def register_user(request):
    """
    Endpoint pour l'inscription d'un nouvel utilisateur.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
        return Response({'error': 'Veuillez fournir un nom d\'utilisateur, un mot de passe et un email.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Ce nom d\'utilisateur est déjà pris.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({'message': 'Utilisateur créé avec succès.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    """
    Endpoint pour la connexion d'un utilisateur.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Connexion réussie.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Nom d\'utilisateur ou mot de passe incorrect.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_user(request):
    """
    Endpoint pour la déconnexion d'un utilisateur.
    """
    logout(request)
    return Response({'message': 'Déconnexion réussie.'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_csrf_token(request):
    """
    Endpoint pour récupérer le token CSRF.
    """
    return Response({'csrf_token': get_token(request)})
