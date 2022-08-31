from rest_framework.viewsets import ModelViewSet

from core.models import Cachorro, Comedouro, Tag, Publicacoes
from core.serializers import CachorroSerializer, ComedouroSerializer, TagSerializer, PublicacoesSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect


class CachorroViewSet(ModelViewSet):
    queryset = Cachorro.objects.all()
    serializer_class = CachorroSerializer


class ComedouroViewSet(ModelViewSet):
    queryset = Comedouro.objects.all()
    serializer_class = ComedouroSerializer

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PublicacoesViewSet(ModelViewSet):
    queryset = Publicacoes.objects.all()
    serializer_class = PublicacoesSerializer

def signup(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('http://127.0.0.1:5173/cachorrada')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
   
def home(request): 
    return render(request, 'home.html')
   
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:5173/cachorrada') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
  
def profile(request): 
    return render(request, 'profile.html')
   
def signout(request):
    logout(request)
    return redirect('/profile')
