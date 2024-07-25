from django.shortcuts import render,redirect
from . models import *
from userapp. models import *
from django.contrib import messages
# Create your views here.
def rationreg(request):
    if request.method=="POST":
        centername=request.POST.get("name")
        email=request.POST.get("email")
        district=request.POST.get("district")
        village=request.POST.get("village")
        ward=request.POST.get("ward")
        Contact=request.POST.get("phnumber")
        aadhar=request.POST.get("ad_card")
        location=request.POST.get("location")
        image=request.FILES.get("image")
        shopimage=request.FILES.get("shopimage")
        Landmark=request.POST.get("landmark")
        Working=request.POST.get("working")
        coordinator=request.POST.get("coordinator")
        Password=request.POST.get("p1")
        Confirmpassword=request.POST.get("p2")
        if Password==Confirmpassword:
            if Ration_DB.objects.filter(Name=centername).exists():
                messages.info(request,'Username Already Exist')
            else:
                userdata=Ration_DB(Name=centername,Email=email,District=district,Village=village,Ward=ward,Contact=Contact,
                                 Aadhar=aadhar,Location=location.upper(),Image=image,shopImage=shopimage,Landmark=Landmark,Working=Working,coordinator=coordinator,Password=Password)
                userdata.save()
                return redirect("rationlog")
        else:
                messages.info(request,'password not match')
    return render(request,"product/rationreg.html")

def rationlog(request):
    if request.method=="POST":
        messages.info(request,'method')  

        try:
            messages.info(request,'method')  

            Email=request.POST.get("email")
            Password=request.POST.get("password")
            log=Ration_DB.objects.get(Email=Email,Password=Password)
            request.session['Email']=log.Email
            request.session['id']=log.id
            messages.info(request,Email,Password)  


            return redirect('rationhome')
        except Ration_DB.DoesNotExist as e :
            messages.info(request,'Invalid User')  
    return render(request,"product/rationlog.html")
  
def rationhome(request):
    return render(request,"product/rationhome.html")


def rationproduct(request):
    if request.method=='POST':
        items=request.POST.get("item")
        quantity=request.POST.get("quantity")
        price=request.POST.get("price")
        card=request.POST.get("card")
        rid=request.POST.get("rid")
        addsave=Items_DB(Items=items,Quantity=quantity,Price=price,Cardtype=card.upper(),Ration_id_id=rid)
        addsave.save()
        return redirect('rationhome')
    return render(request,"product/rationproduct.html")


def rationprofile(request):
    id=request.session['id']
    ration=Ration_DB.objects.get(id=id)
    return render(request,"product/rationprofile.html",{'ration':ration})

def rationeditprofile(request):
    ration=Ration_DB.objects.get(id=request.session['id'])
    if request.method=="POST":
        if len(request.FILES)!=0:
            ration.Image=request.FILES['image']
            
        ration.Name=request.POST['name']
        ration.Email=request.POST['email']
        ration.District=request.POST['district']
        ration.Village=request.POST['village']
        ration.Ward=request.POST['ward']
        ration.Contact=request.POST['phnumber']
        ration.Aadhar=request.POST['ad_card']
        # ration.Location=request.POST['location']
        ration.Landmark=request.POST['landmark']
        ration.Working=request.POST['working']
        ration.coordinator=request.POST['coordinator']
        ration.save()
        return redirect('rationprofile')  
    return render(request,"product/rationeditprofile.html",{'ration':ration})
    
def viewitems(request):
    id=request.session['id']
    vitems=Items_DB.objects.filter(Ration_id=id)
    return render(request,"product/viewitems.html",{'vt':vitems})

def delitem(request,id):
    item=Items_DB.objects.get(id=id)
    item.delete()
    return redirect('viewitems')

def edit_item(request,id):
    edit=Items_DB.objects.get(id=id)
    if request.method=="POST":
        edit.Items = request.POST.get('item')
        edit.Quantity = request.POST.get('quantity')
        edit.Price=request.POST.get('price')
        # edit.Cardtype=request.POST.get('card')
        edit.save()
        return redirect('rationhome')
    return render(request,"product/edit_item.html",{'edit':edit})


def booking_information(request):
    id=request.session['id']
    od=Rationbook.objects.filter(rationid=id)
    return render(request,"product/booking_information.html",{'od':od})


