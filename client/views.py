from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # for reset password
from django.contrib.auth import authenticate, logout
from django.views.generic.edit import UpdateView, CreateView
from client.models import Contact, UserBank, UserProfile, Transaction, Membership, CompanyBankUPIQR
import random
from django.http.response import HttpResponseRedirect

# Create your views here.


def index(request):
    mbr_status = Membership.objects.filter(user_id=request.user.id).first()
    total_clients = User.objects.all().count()
    summary = {'total_clients': total_clients, 'mbr_status': mbr_status}
    return render(request, 'client/index.html', summary)

def profile(request):
    if request.method=="POST":
        my_referal_code = request.POST['my_referal_code']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        dob = request.POST['dob']
        address = request.POST['address']
        block = request.POST['block']
        district = request.POST['district']
        state = request.POST['state']
        pin_code = request.POST['pin_code']
        image = request.FILES['image']

        try:
            UserProfile.objects.filter(user_id=request.user).update(my_referal_code=my_referal_code, mobile=mobile, gender=gender, dob=dob, state=state, district=district, block=block, address=address, pin_code=pin_code, image=image)
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
        upi_id = request.POST['upi_id']
        bank_name = request.POST['bank_name']
        account_holder_name = request.POST['account_holder_name']
        account_number = request.POST['account_number']
        account_number2 = request.POST['account_number2']
        branch_name = request.POST['branch_name']
        ifsc_code = request.POST['ifsc_code']

        if(upi_id==""):
            if bank_name=="" or account_holder_name=="" or account_number=="" or account_number2=="" or branch_name=="" or ifsc_code=="":
                messages.error(request, 'All fields are required!.')
                return redirect('Bank')

            if account_number != account_number2:
                messages.error(request, 'Account Number not matched!, Try again.')
                return redirect('Bank')

        try:
            UserBank.objects.filter(user_id=request.user).update(upi_id=upi_id, bank_name=bank_name, account_holder_name=account_holder_name, account_number=account_number, branch_name=branch_name, ifsc_code=ifsc_code)
            messages.success(request, 'Your UPI or Bank Account Details Successfully Saved. Thank you.')
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

def transaction(request):
    user_id = request.user
    allTransactions = Transaction.objects.filter(user_id=user_id)
    return render(request, 'client/transaction.html',{"allTransactions": allTransactions})

def membership(request):
    upis = CompanyBankUPIQR.objects.all()
    if request.method=='POST':
        user_id = request.user
        transaction_id = request.POST['transaction_id']
        transaction_slip = request.FILES['transaction_slip']
        amount = request.POST['amount']
        txt_date = request.POST['txt_date']
        y, m, d = txt_date.split("-")
        exp_date = f"{str(int(y)+1)}-{m}-{d}"

        try:
            mbr = Membership(user_id=user_id, transaction_id=transaction_id, transaction_slip=transaction_slip, amount=amount, txt_date=txt_date, exp_date=exp_date)
            mbr.save()
            messages.success(request, 'Your Account will be Activated within 24 Hrs. Thank You.')
            return redirect('Client')
        except:
            messages.error(request, 'Something Wrong!, Try again.')
            return redirect('Membership')
    return render(request, 'client/membership.html', {'upis':upis})
 

def handleLogout(request):
    logout(request)
    messages.info(request, 'Logout Successfully. Thanks for spending some quality time with the Web site today')
    return redirect('/')