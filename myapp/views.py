from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from FinalProject import settings
# Create your views here.


status = False
def index(request):
    global status
    if request.method == 'POST':
        if request.POST.get('signup') == 'signup':

            newuser = signupform(request.POST)

            if newuser.is_valid():
                newuser.save()
                print("Signup Successfull")
            else:
                print(newuser.errors)
        elif request.POST.get('login') == 'login':
            unm = request.POST['username']
            pas = request.POST['password']

            user = signupmaster.objects.filter(username = unm, password = pas)
            uid = signupmaster.objects.get(username = unm)
            print("UserId: ", uid.id)
            if user:

                print("Login Successfully!")
                request.session['user'] = unm
                request.session['uid'] = uid.id
                #msg = "Login Successfully!"
                status = True
                return redirect('notes')
            else:
                print("Login Failed")
    return render(request, "index.html")

def notes(request):
    #global status
    user = request.session.get('user')
    if request.method == 'POST':
        newnotes = notesform(request.POST, request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Submit Post Successfull")
                
        else:
            print(newnotes.errors)
    return render(request, "notes.html",{'user' : user})

def profile(request):
    user = request.session.get('user')
    uid = request.session.get('uid')
    cuser = signupmaster.objects.get(id = uid)
    if request.method == 'POST':
        newuser = updateform(request.POST, instance = cuser)
        if newuser.is_valid():
            newuser.save()
            print("Profile Updated!!!")
            return redirect('notes')
        else:
            print(newuser.errors)
    return render(request, "profile.html",{'user' : user, 'cuser' : cuser})

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        newfeedback = feedbackform(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Your Feedback has been Submitted!!")

            # Email Send
            sub = "Thank You!!"
            msg = f"Hello {request.POST['name']}!!\n\n We have recived you feedback.\n We will contact you in shortly.\n\n If any queries regarding, conatct us anytime on\n\n +919979131476 | dhrutidharkotadiya51@gmail.com\n\n Thnaks & Regards!\n Dhrutidhar Kotadiya\n8239430873"
            from_mail = settings.EMAIL_HOST_USER
            #to_mail = ["dhrutidharkotadiya51@gmail.com"]
            to_mail = [request.POST['email']]
            send_mail(subject=sub, message=msg, from_email=from_mail, recipient_list= to_mail)


        else:
            print(newfeedback.errors)
    return render(request, "contact.html")

def userlogout(request):
    logout(request)
    return redirect('/')