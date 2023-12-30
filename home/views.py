from django.shortcuts import render 
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable' : 'god or wot',
        'variable1': 'easy'
    }
    
    #return HttpResponse("this is home page")
    return render(request,'index.html',context)

def about(request):
    return render(request , "about.html")

def services(request):
    return render(request , "services.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = Contact(name=name,phone=phone,email=email,password=password,date = datetime.today())
        contact.save()
        messages.success(request,"your message has been sent to PUBG officials")

    return render(request , "contact.html")