from django.shortcuts import render,redirect
from django.contrib.auth import  logout,authenticate,login
from account.forms import RegistrationForm,AccountAuthenticationForm

def index(request):
   
    return render(request , 'pages/index.html')

def aboutus(request):
    return render(request,'pages/aboutus.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeuser') 
    else:
        form = RegistrationForm()
    return render(request, 'pages/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')
                else:
                    return redirect('index') 
        else:
            context = {'login_form': form, 'message': 'Invalid email or password.'}
            return render(request, 'pages/signin.html', context)
    else:
        
        form = AccountAuthenticationForm()
    context = {'login_form': form}
    return render(request, 'pages/signin.html', context)

def checkout(request):
    return render(request,'pages/checkout-order.html')

def paiment(request):
    return render(request,'pages/checkout-payment.html')

def panier(request):
    return render(request,'pages/panier.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def home_game(request):
    return render(request,'pages/homegames.html')