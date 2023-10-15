
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages, auth


def home(request):
    return render(request,'Home.html')



def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return HttpResponse('''<script>alert("login compleated");window.location='/rediectpage'</script>''')
        else:
            messages.info(request,'invalid user')
            return redirect('Login')

    return render(request,'Login.html')


def rediectpage(request):
    return render(request,'third.html')



def lastform(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        branch = request.POST['courceselect']
        courceselect = request.POST['purpose']
        materials = request.POST['materials']

        return HttpResponse('<center><p>Application Accepted</p><p><a href="lastfile">Return to Home Page</a></p></center>')

    return render(request,'Lastform.html')

def lastfile(request):
    return render(request,'lastfile.html')


def logout(request):
    auth.logout(request)
    return redirect('/')





def Registration(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'already used')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                print('registration completed')
                return HttpResponse('''<script>alert("registration compleated");window.location='/Login'</script>''')
        else:
            return HttpResponse('''<script>alert("password not matching");window.location='/cred/Registration/'</script>''')
    return render(request,'Registration.html')
