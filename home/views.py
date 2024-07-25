from django.shortcuts import render
from django.http import HttpResponse
# Create your view here.
# def home(request):
#     return HttpResponse("welcome to django ok")

def home(request):
    return render(request,"Home/index.html")

def contact(request):
    return render(request,"Home/contact.html")
    
def about(request):
    return render(request,"Home/about.html")





