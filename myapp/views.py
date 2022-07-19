import email
from unicodedata import name
from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from rest_framework import viewsets
from .serializers import UserSerializer

# Create your views here.

def add_show(request):

    if request.method == 'POST':
        data = UserForm(request.POST)
        if data.is_valid():
            nm = data.cleaned_data['name']
            em = data.cleaned_data['email']
            pas = data.cleaned_data['password']
            user = User(name=nm, email=em, password=pas)
            user.save()
            return redirect('home')
    else:
        form = UserForm()
        user = User.objects.all()
    return render(request, 'myapp/addshow.html', {'fm':form, 'user':user})

def update_data(request,id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        fm = UserForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        data = User.objects.get(pk=id)
        form = UserForm(instance=data)
        return render(request, 'myapp/update.html', {'fm':form})


def delete(request,id):
    data = User.objects.get(pk=id)
    data.delete()
    return redirect('home')


class UserApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

