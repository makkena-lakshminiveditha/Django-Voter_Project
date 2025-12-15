from django.shortcuts import render,redirect
from app.forms import Voter_form
from app.models import Voter_model
from datetime import date
import random
import string

# Create your views 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
def registration_form(request):
    message = ''
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_email = request.POST.get('useremail')
        user_password = request.POST.get('userpassword')
        user_repassword = request.POST.get('reuserpassword')

        if user_password != user_repassword:
            message = 'Passwords do not match'
        elif User.objects.filter(email=user_email).exists():
            message = 'User already exists'
        else:
            user = User.objects.create_user(
                username=user_name,
                email=user_email,
                password=user_password
            )
            user.save()
            return redirect('login101')

    return render(request,'register.html', {'message': message})
def login_form(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('login_name')
        password = request.POST.get('login_password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            message = 'login Succesfully'
            return redirect('myhomepage')   
        else:
            message = 'Invalid username or password'

    return render(request,'login1.html', {'message': message})


#--------------------------------------------------HOME-----------------------------------------------------------
def home_page(request):
    return render(request,'home.html')

def voter_table(request):
    voter = Voter_model.objects.all()
    return render(request,'listtable.html',{'voter':voter})
  
def generate_voter_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def voter_form(request):
    if request.method == 'POST':
        form = Voter_form(request.POST, request.FILES)
        if form.is_valid():
            voter = form.save(commit=False)

            if voter.age < 18:
                form.add_error('age', 'Age must be 18 or above')
                return render(request, 'voterform.html', {'form': form})

            voter.Voter_id = generate_voter_id()
            voter.save()
            return redirect('votercard',id=voter.id)
    else:
        form = Voter_form()

    return render(request, 'voterform.html', {'form': form})

def voter_card(request, id):
    voter = Voter_model.objects.get(id=id)
    return render(request, 'votercard.html', {'voter': voter})