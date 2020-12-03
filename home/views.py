from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    #context = {
    #    "variable":"This is text"
    #}
    return render(request,'index.html')
    #return HttpResponse("this is my home ")

def about(request):
    return render(request,'about.html')
  #  return HttpResponse("this is my about ")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is my services ")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been Sent ')

    return render(request,'contact.html')
    #return HttpResponse("this is my contact page ")