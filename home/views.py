from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from client.models import UserProfile
from django.core.mail import send_mail
import random

def index(request):
    return render(request, 'home/index.html')

# Authentication APIs
def handleSignup(request):
    if request.method=="POST":
        use_referal_code = request.POST['referal_code']
        name = request.POST['name'].strip().split(" ")   # split the entire name in list.    
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['pass']
        repass = request.POST['repass']
        fname = name[0].capitalize()     # find first name.
        lname = name[-1].capitalize()    # find last name.
        uname = email.split("@")[0]    # find user name form first part of emailid.
        s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
        random.shuffle(s)
        my_referal_code = "".join(s[0:6])+mobile[6:]     # generate referal code.

        fetch_referal = UserProfile.objects.filter(my_referal_code=use_referal_code).first()
        
        if fname==lname:
            lname = ""
        
        if not fetch_referal:
            use_referal_code = "1Ae3F35586"

        if password != repass:
            messages.warning(request, 'Re-password not matched. Try again.')
            return redirect('Home')

        if not mobile.isnumeric():
            messages.error(request, 'Please enter valid mobile number')
            return redirect('Home')
        
        if len(mobile) != 10:
            messages.warning(request, 'Mobile number contain only 10 digits.')
            return redirect('Home')
        
        exist_uname = User.objects.filter(username=uname)
        exist_email = User.objects.filter(email=email)
        if exist_uname or exist_email:
            messages.warning(request, 'This email id is not allowed! Try another email id.')
            return redirect('Home')

        try:
            myuser = User.objects.create_user(uname, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            UserProfile.objects.filter(user_id=myuser).update(use_referal_code=use_referal_code, my_referal_code=my_referal_code, mobile=mobile)
            messages.success(request, '( USER_ID: '+uname+' ) Congratulations! Your EF3F account has been registred successfully.')
        except:
            messages.error(request, 'Something Wrong! Try again.')
        return redirect('Home')

    return render(request, 'home/index.html')

def signup_by_referal(request):
    if request.method=="POST":
        use_referal_code = request.POST['referal_code']
        name = request.POST['name'].strip().split(" ")   # split the entire name in list.    
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['pass']
        repass = request.POST['repass']
        fname = name[0].capitalize()     # find first name.
        lname = name[-1].capitalize()    # find last name.
        uname = email.split("@")[0]    # find user name form first part of emailid.
        s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
        random.shuffle(s)
        my_referal_code = "".join(s[0:6])+mobile[6:]     # generate referal code.

        fetch_referal = UserProfile.objects.filter(my_referal_code=use_referal_code).first()

        if fname==lname:
            lname = ""
        
        if not fetch_referal:
            use_referal_code = "1Ae3F35586"

        if password != repass:
            messages.warning(request, 'Re-password not matched. Try again.')
            return render(request, 'home/signup_by_referal.html', {'use_referal_code': use_referal_code})

        if not mobile.isnumeric():
            messages.error(request, 'Please enter valid mobile number')
            return render(request, 'home/signup_by_referal.html', {'use_referal_code': use_referal_code})
        
        if len(mobile) != 10:
            messages.warning(request, 'Mobile number contain only 10 digits.')
            return render(request, 'home/signup_by_referal.html', {'use_referal_code': use_referal_code})
        
        exist_uname = User.objects.filter(username=uname)
        exist_email = User.objects.filter(email=email)
        if exist_uname or exist_email:
            messages.warning(request, 'This email id is not allowed! Try another email id.')
            return render(request, 'home/signup_by_referal.html', {'use_referal_code': use_referal_code})

        try:
            myuser = User.objects.create_user(uname, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            UserProfile.objects.filter(user_id=myuser).update(use_referal_code=use_referal_code, my_referal_code=my_referal_code, mobile=mobile)
            messages.success(request, '( USER_ID: '+uname+' ) Congratulations! Your EF3F account has been registred successfully.')
            return redirect('Home')
        except:
            messages.error(request, 'Something Wrong! Try again.')
            return render(request, 'home/signup_by_referal.html', {'use_referal_code': use_referal_code})

    use_referal_code = request.GET.get('use_referal_code')
    return render(request, 'home/signup_by_referal.html', {'use_referal_code': use_referal_code})

def handleLogin(request):
    if request.method=='POST':
        user_id = request.POST['user_id'].split("@")[0]
        password = request.POST['password']

        user = authenticate(request, username=user_id, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have Successfully Loged In')
            return redirect('client/')
        else:
            messages.error(request, 'Invalid Credentials, Please try again.')
            return redirect('Home')
    else:
        messages.warning(request, 'Please fill valid information.')
        return redirect('Home')

    return render(request, 'home/index.html')
