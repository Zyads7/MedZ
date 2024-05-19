from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home(request):
    isActive=True
    if request.method=='POST':
         check=request.POST.get("check")
         print(check)  
         if check is  None: isActive=False
         else: isActive=True


    date=datetime.datetime.now()  
   
    # return HttpResponse("<h1>Hello this is index page  </h1> "+str(date))
    data={
        'date':date,
        'isActive':isActive,
       
    }
    return render(request,"home.html",{})

def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})
