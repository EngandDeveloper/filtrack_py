from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main_filter/index.html')

def getData(request):
    userInput = []
    if request.GET.get('time'):
        userInput[0] = request.GET.get('time')
    if request.GET.get('artistName'):
        userInput[1] = request.GET.get('artistName')
    if request.GET.get('keyword'):
        userInput[2] = request.GET.get('keyword')
    if request.GET.get('acousticness'):
        userInput[3] = request.GET.get('acousticness')
    if request.GET.get('danceability'):
        userInput[4] = request.GET.get('danceability')
    if request.GET.get('energy'):
        userInput[5] = request.GET.get('energy')
    if request.GET.get('instrumentalness'):
        userInput[6] = request.GET.get('instrumentalness')
    if request.GET.get('liveleness'):
        userInput[7] = request.GET.get('liveleness')
    if request.GET.get('loudness'):
        userInput[8] = request.GET.get('artistName')
    if request.GET.get('speechiness'):
        userInput[9] = request.GET.get('speechiness')
    if request.GET.get('tempo'):
        userInput[10] = request.GET.get('tempo')
    if request.GET.get('valence'):
        userInput[11] = request.GET.get('valence')

    return 