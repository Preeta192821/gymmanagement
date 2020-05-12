from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import*

# Create your views here.


def Gym(request):
    return render(request,'gym.html')


def About(request):
 	return render(request,'about.html')

def Contact(request):
	return render(request,'contact.html')



def Index(request):
    if not request.user.is_staff:
        return redirect('gym')
    if request.user.is_staff:
        return redirect('gym')             
    return render_to_response(request,'index.html')


def Adminlogin(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}    
    return render(request,'adminlogin.html',d)
  
def Logout(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    logout(request)
    return redirect('adminlogin')


def Add_Enquiry(request):
    error=""
    if not request.user.is_staff:
        return redirect('adminlogin')

    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        try:
            Enquiry.objects.create(name=n,contact=c,emailid=e,age=a,gender=g)
            error="no"
        except:
            error="yes"
    d = {'error':error}         
    return render(request,'add_enquiry.html',d)


def View_Enquiry(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
        
    enq = Enquiry.objects.all()
    d = {'enq':enq}
    return render(request,'view_enquiry.html',d)



def Delete_Enquiry(request,pid):
    if not request.user.is_staff:
        return redirect('adminlogin')
        
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('view_enquiry')


def Add_Equipment(request):
    error=""
    if not request.user.is_staff:
        return redirect('adminlogin')

    if request.method=="POST":
        en = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        de = request.POST['description']
        try:
            Equipment.objects.create(name=en,price=p,unit=u,date=d,description=de)
            error="no"
        except:
            error="yes"
    d = {'error':error}         
    return render(request,'add_equipment.html',d)


def View_Equipment(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
        
    equipment = Equipment.objects.all()
    d = {'equipment':equipment}
    return render(request,'view_equipment.html',d)



def Delete_Equipment(request,pid):
    if not request.user.is_staff:
        return redirect('adminlogin')
        
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('view_equipment')


def Add_Plan(request):
    error=""
    if not request.user.is_staff:
        return redirect('adminlogin')

    if request.method=="POST":
        nn = request.POST['name']
        am = request.POST['amount']
        du = request.POST['duration']
        try:
            Plan.objects.create(name=nn,amount=am,duration=du)
            error="no"
        except:
            error="yes"
    d = {'error':error}         
    return render(request,'add_plan.html',d)


def View_Plan(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    plan = Plan.objects.all()
    d = {'plan':plan}
    return render(request,'view_plan.html',d)



def Delete_Plan(request,pid):
    if not request.user.is_staff:
        return redirect('adminlogin')
        
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('view_plan')


def Add_Member(request):
    error=""
    if not request.user.is_staff:
        return redirect('adminlogin')

    if request.method=="POST":
        na = request.POST['name']
        co = request.POST['contact']
        eid = request.POST['emailid']
        ag = request.POST['age']
        ge = request.POST['gender']
        pl = request.POST['plan']
        j = request.POST['join date']
        ex = request.POST['expire date']
        ini = request.POST['initial amount']
        re = request.POST['remaining amount']
        try:
            Member.objects.create(name=na,contact=co,emailid=eid,age=ag,gender=ge,plan=pl,joindate=j,expiredate=ex,initialamount=ini,remainingamount=re)
            error="no"
        except:
            error="yes"
    d = {'error':error}         
    return render(request,'add_member.html',d)


def View_Member(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    member = Member.objects.all()
    d = {'member':member}
    return render(request,'view_member.html',d)



def Delete_Member(request,pid):
    if not request.user.is_staff:
        return redirect('adminlogin')
        
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('view_member')


