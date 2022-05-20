from django.shortcuts import render

def home(request):
    return render (request, 'core/home.html')
def history(request):
    return render (request, 'core/history.html')
def characters(request):
    return render (request, 'core/characters.html')


