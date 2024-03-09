from django.shortcuts import redirect, render
from home.models import register
from django.contrib import messages
from django.contrib.auth import authenticate, login
from home.models import Vehical


# Create your views here.


def index(request):
      
      return render(request, 'index.html')
    # return HttpResponse("index")
    


def Login(request):
    
    if request.method=="POST":
             
        email=request.POST['email']
        pas=request.POST['pas']
        user = authenticate(username=email,passsword=pas)

        if user is not None:
                login(request,user)
                messages.success(request, "successfully logged In")
                return redirect('chargeslot')
        else:
                messages.error(request, "invalid cridentials, please try again")
                return redirect('Login')
             
            
    return render(request, 'Login.html')
    # return HttpResponse("Login")
   

def Logout(request):
          
    return render(request, 'Logout.html')
    # return HttpResponse("Login")


def home1(request):
     
     return render(request, 'home1.html')
    # return HttpResponse("Home")
   


def register1(request):
     messages.success(request, "your account has been successfull created")
     messages.error(request, "your account has been successfull created")
     messages.warning(request, "your account has been successfull created")
     
     if request.method=="POST":
              name=request.POST['name']
              email=request.POST['email']
              mono=request.POST['mono']
              pin=request.POST['pin']
              pas=request.POST['pas']
            
              ins = register(name=name, email=email, mono=mono, pin=pin, pas=pas)
              ins.save()
              
            
      
            
            
     return render(request, 'register1.html')
            #  return HttpResponse(" hallow i am working")
   


def chargeslot(request):
  
    return render(request, 'chargeslot.html')
    # return HttpResponse("Myaccount")
 


def station(request):
  
   return render(request, 'station.html')
    # return HttpResponse("Myaccount")
    


def admin1(request):
     
     return render(request, 'admin1.html')
    # return HttpResponse("Myaccount")
   


def vehical(request):
    if request.method=="POST":
             print("hellow omkesh ..............")
             c_name = request.POST['c_name']
             c_no = request.POST['c_no']
             
        
             ins = Vehical(c_name=c_name, c_no=c_no )
             ins.save()
             messages.success(request, "your account has been successfull created")
            
    return render(request, 'vehical.html')
            #  return HttpResponse('vehical.html')
    
 