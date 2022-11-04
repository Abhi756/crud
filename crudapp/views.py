from django.shortcuts import redirect, render
from .models import EmployeeDetails
from .forms import MyForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import json
import itertools

def index(request):
    if request.method =="POST":
        form=MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data/')  
        else:
            form=MyForm()
    else:
            form=MyForm()      
    return render(request,"home.html",{'form':form})
   
def data(request):
   
    emp=EmployeeDetails.objects.all()
   
      
     
    
        
    

    
    
    return render(request,"data.html",{'empr':emp})

def senddata(request):
    import pdb;pdb.set_trace()
    if request.method =='POST':
        dat=request.post['data']
        print(dat)
  
        
   

   
        

