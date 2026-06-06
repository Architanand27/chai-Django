from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Archit..!, This is home page..")
    return render(request, 'index.html')
def about(request):
    # return HttpResponse("Hello Archit..!, This is about page..")
    return render(request, 'about.html')
def contact(request):
    # return HttpResponse("Hello Archit..!, This is contact page..")
    return render(request, 'contact.html')