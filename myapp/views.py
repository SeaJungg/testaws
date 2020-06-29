from django.shortcuts import render
from .models import someModel

def index(request):
    names = someModel.objects.all()
    return render(request, 'index.html', {"names":names})