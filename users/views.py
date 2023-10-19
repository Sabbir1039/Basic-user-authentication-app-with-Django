from django.shortcuts import render, redirect
from users.forms import UserRegiterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
# from users.models import Profile

# Create your views here.
def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        forms = UserRegiterForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            messages.success(request,f"Successfully account created for {username}")
            return redirect('/')
        else:
            messages.error(request,'Error! Can not create account. Try agin!')
            return redirect('/')
    else:
        context = {
            'title': 'Register',
            'forms': UserRegiterForm(),
        }
        return render(request, 'users/register.html', context)
    
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(request, f'Your account can not be updated!')
            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/profile.html', context)