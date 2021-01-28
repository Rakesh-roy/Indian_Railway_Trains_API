import json

from django.contrib import messages
from django.shortcuts import render, redirect
from Trains.utils import searchTrain

# Create your views here.
def home(request):
    if request.method == 'POST':
        train_name = request.POST.get('name')
        data = searchTrain('https://trains.p.rapidapi.com/',train_name)
        if data:
            data = json.loads(data)
            return render(request, 'home.html',{'data':data, 'train': train_name})
        else:
            return render(request, 'home.html',{'error':'Sorry..! No Results Found With Name : ', 'train': train_name})
    else:
        return render(request, 'home.html')