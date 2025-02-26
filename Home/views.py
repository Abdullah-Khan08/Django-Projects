from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):

    persons =[ 
        {'Name':'Abdullah','age':21},
        {'Name':'ali','age':22},
        {'Name':'usman','age':20},
        {'Name':'Abdulrehman','age':17}
    ]
      
    return render(request,"index.html" ,context={'persons': persons})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
