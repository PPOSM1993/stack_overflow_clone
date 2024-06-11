from django.shortcuts import render

# Create your views here.


#def index(request):
#    return render(request, 'index.html')


def HomeView(request):
    return render(request, 'home.html')

def AboutView(request):
    return render(request, 'about.html')