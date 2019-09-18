from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, 'welcome/index.html', context)

def login(request):
    context = {}
    return render(request, 'welcome/login.html', context)

def register(request):
    context = {}
    return render(request, 'welcome/register.html', context)