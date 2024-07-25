
# Create your views here.
from django.shortcuts import render,redirect
from . models import *
from userapp . models import *
from django.contrib import messages

# Create your views here.

def delireg(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        address=request.POST.get("address")
        email=request.POST.get("email")
        district=request.POST.get("district")
        Location=request.POST.get("Location")
        Mincharge=request.POST.get("Mincharge")     
        number=request.POST.get("number")     
        Dproof=request.FILES.get("image")
        p1=request.POST.get("p1")
        p2=request.POST.get("p2")
        if p1==p2:
            if Delivery_TB.objects.filter(Name=name).exists():
                messages.info(request,'Username Already Exist')
            else:
                userdata=Delivery_TB(Name=name,Age=age,Address=address,number=number,Email=email,District=district,Location=Location,Password=p1,Mincharge=Mincharge,Dproof=Dproof)
                userdata.save()
                return redirect("delilog")
        else:
                messages.info(request,'password not match')
    return render(request,"delivery/delireg.html")

def delilog(request):
    if request.method=="POST":
        messages.info(request,'method')  

        try:
            messages.info(request,'method')  

            Email=request.POST.get("email")
            Password=request.POST.get("p1")
            log=Delivery_TB.objects.get(Email=Email,Password=Password)
            request.session['Email']=log.Email
            request.session['id']=log.id
            messages.info(request,Email,Password)  


            return redirect('delihome')
        except Delivery_TB.DoesNotExist as e :
            messages.info(request,'Invalid User')

    return render(request,"delivery/delilog.html")
  
def delihome(request):
    return render(request,"delivery/delihome.html")
def dprofile(request):
    id=request.session['id']
    ration=Delivery_TB.objects.get(id=id)
    return render(request,"delivery/dprofile.html",{'r':ration})



def deditprofile(request):
    ration=Delivery_TB.objects.get(id=request.session['id'])
    if request.method=="POST":
        if len(request.FILES)!=0:
            ration.Dproof=request.FILES['image']
          
        ration.Name=request.POST['name']
        ration.Address=request.POST['address']
        ration.Email=request.POST['email']
        ration.Age=request.POST['age']
        ration.Location=request.POST['Location']
        ration.District=request.POST['district']
        ration.Mincharge=request.POST['Mincharge']
        ration.number=request.POST['number']

        ration.Password=request.POST['password']

    
        # ration.Location=request.POST['location']

        ration.save()
        return redirect('dprofile')  
    return render(request,"delivery/deditprofile.html",{'r':ration})

def dBooking(request):
    db=Assign.objects.filter(boy=request.session['id'])
    return render(request,"delivery/dBooking.html",{'db':db})


# def neworder(request,pk):
#     notification.objects.filter(id=pk).update(neworderstatus=True)
#     D=notification.objects.filter(boy=request.session['id'])
#     return render(request,'delivery/deliverydetails.html',{'d':D})


def orderconf(request,id):
    Assign.objects.filter(id=id).update(order=True)
    return redirect("dBooking" )

def completedstatus(request,id):
    Assign.objects.filter(id=id).update(neworder=True)
    return redirect("dBooking" )