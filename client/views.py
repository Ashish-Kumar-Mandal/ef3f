from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # for reset password
from django.contrib.auth import authenticate, logout
from client.models import Contact, UserBank, UserProfile

# Create your views here.


def index(request):
    total_clients = User.objects.all().count()
    summary = {'total_clients': total_clients}
    return render(request, 'client/index.html', summary)

def profile(request):
    if request.method=="POST":
        my_referal_code = request.POST['my_referal_code']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        marital_status = request.POST['marital_status']
        dob = request.POST['dob']
        designation = request.POST['designation']
        address = request.POST['address']
        block = request.POST['block']
        district = request.POST['district']
        state = request.POST['state']
        pin_code = request.POST['pin_code']

        try:
            UserProfile.objects.filter(user_id=request.user).update(my_referal_code=my_referal_code, mobile=mobile, gender=gender, marital_status=marital_status, dob=dob, designation=designation, state=state, district=district, block=block, address=address, pin_code=pin_code)
            messages.success(request, 'Your Profile Details Successfully Saved. Thank you.')
        except:
            messages.error(request, 'Something Wrong!')

        return redirect('/client/profile')
    
    profileDetails = UserProfile.objects.filter(user_id=request.user).first()
    return render(request, 'client/profile.html', {'profileDetails': profileDetails})

def password(request):
    if request.method=="POST":
        username = request.user
        old_psw = request.POST['old_psw']
        psw = request.POST['psw']
        repsw = request.POST['repsw']
        
        if psw != repsw:
            messages.error(request, 'Confirm password not matched! Try again.')
            return redirect('/client/password')
        
        try:
            user_logedin = authenticate(username=username, password=old_psw)
            user = get_user_model().objects.get(username=username)

            if user != user_logedin:
                messages.error(request, 'Current password not matched!')
                return redirect('/client/password')
            else:
                user.set_password(psw)
                user.save()
                messages.success(request, 'Your Profile Password Successfully Changed. Now Login')
                return redirect('/')
        except:
            messages.error(request, 'Something Wrong!')
            return redirect('/client/password')

    return render(request, 'client/password.html')

def bank(request):
    if request.method=="POST":
        bank_name = request.POST['bank_name']
        account_holder_name = request.POST['account_holder_name']
        account_number = request.POST['account_number']
        account_number2 = request.POST['account_number2']
        branch_name = request.POST['branch_name']
        ifsc_code = request.POST['ifsc_code']

        if bank_name=="" or account_holder_name=="" or account_number=="" or account_number2=="" or branch_name=="" or ifsc_code=="":
            messages.error(request, 'All fields are required!.')
            return redirect('Bank')

        if account_number != account_number2:
            messages.error(request, 'Account Number not matched!, Try again.')
            return redirect('Bank')

        try:
            UserBank.objects.filter(user_id=request.user).update(bank_name=bank_name, account_holder_name=account_holder_name, account_number=account_number, branch_name=branch_name, ifsc_code=ifsc_code)
            messages.success(request, 'Your Bank Account Details Successfully Saved. Thank you.')
        except:
            messages.error(request, 'Something Wrong!')

        return redirect('/client/bank')

    bankDetails = UserBank.objects.filter(user_id=request.user).first()
    return render(request, 'client/bank.html', {'bankDetails': bankDetails})

def client_list(request):
    myProfileDetails = UserProfile.objects.filter(user_id=request.user).first()
    my_referal_code = myProfileDetails.my_referal_code
    myClientList = UserProfile.objects.filter(use_referal_code=my_referal_code)    
    return render(request, 'client/client_list.html', {'myClientList': myClientList})

def add_client(request):
    if request.method=="POST":
        use_referal_code = request.POST['refral_code']
        name = request.POST['name'].strip().split(" ")   # split the entire name in list.    
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['pass']
        repass = request.POST['repass']
        fname = name[0].capitalize()     # find first name.
        lname = name[-1].capitalize()    # find last name.
        uname = email.split("@")[0]    # find user name form first part of emailid.
        my_referal_code = fname[0]+lname[0]+email[0]+password[0]+mobile[4:]     # generate referal code.

        if password != repass:
            messages.warning(request, 'Re-password not matched. Try again.')
            return redirect('Add_client')

        if not mobile.isnumeric():
            messages.error(request, 'Please enter valid mobile number')
            return redirect('Add_client')
        
        if len(mobile) != 10:
            messages.warning(request, 'Mobile number contain only 10 digits.')
            return redirect('Add_client')
        
        exist_uname = User.objects.filter(username=uname)
        exist_email = User.objects.filter(email=email)
        if exist_uname or exist_email:
            messages.warning(request, 'This email id is not allowed! Try another email id.')
            return redirect('Add_client')

        try:
            myuser = User.objects.create_user(uname, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            UserProfile.objects.filter(user_id=myuser).update(use_referal_code=use_referal_code, my_referal_code=my_referal_code, mobile=mobile)
            messages.success(request, 'Congratulations! In EF3F have, your new Client account has been registred successfully.')
        except:
            messages.error(request, 'This mobile number is not allowed. Try another number!')
        return redirect('Add_client')

    my_referal_code = UserProfile.objects.filter(user_id=request.user).first().my_referal_code
    return render(request, 'client/add_client.html', {'my_referal_code': my_referal_code})

def my_referal_code(request):
    my_referal_code = UserProfile.objects.filter(user_id=request.user).first().my_referal_code
    return render(request, 'client/share_referal_code.html', {'my_referal_code': my_referal_code})

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        msg_title = request.POST['msg_title']
        msg_content = request.POST['msg_content']

        if len(msg_title)<4 or len(msg_content)<10:
            messages.error(request, 'Your message length is very short, try to write more content.')
        else:
            try:
                contact = Contact(name=name, mobile=mobile, email=email, title=msg_title ,message=msg_content)
                contact.save()
                messages.success(request, 'Your message has been successfully sent.')
            except:
                messages.error(request, 'Something Wrong!, Try again.')
    return redirect('/client')
    

def handleLogout(request):
    logout(request)
    messages.info(request, 'Logout Successfully. Thanks for spending some quality time with the Web site today')
    return redirect('/')