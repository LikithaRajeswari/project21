from django.shortcuts import render

# Create your views here.

def bulit_filters(request):
    data='HeLLo hOW aRE YOU'
    d={'data':data}
    
    return render(request,'bulit_filters.html',d)

def custom_filters(request):
    return render(request,'custom_filters.html')