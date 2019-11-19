from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")


def registerUser(request):
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    mobile = request.POST['mobile']
    email = request.POST['email']
    profilepic = request.FILES['image']

    newuser = User.objects.create(firstname=firstname,lastname=lastname,mobile=mobile,email=email,profilepic=profilepic)
    return HttpResponseRedirect(reverse('alldetail'))

def AllDetails(request):
    all_details = User.objects.all()
    return render(request,"app/sucess.html",{'all_details':all_details})