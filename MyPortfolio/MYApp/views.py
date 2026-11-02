from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from Services.models import services_model
from contacts.models import contact_model


def home_view(request):
    servicedata=services_model.objects.all()
    data={
        'servicedata': servicedata
    }
    
    
    if request.method =="POST":
        v1=request.POST.get('name')
        v2=request.POST.get('email')
        v3=request.POST.get('message')
        vres=contact_model(Name=v1,Email=v2,Message=v3)
        vres.save()
        return render(request,"main/thankyouu.html")
    
    
    
    return render(request,"main/index.html",data)


# def mydetails_view(request):
#     return render(request,"main/mydetails.html")



# Create your views here.
