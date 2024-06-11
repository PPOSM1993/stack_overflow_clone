from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
# Create your views here.


def Register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account successfully created for {username}! Login In now")
            return redirect('stack_overflow:home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def Profile(request):
        return render(request, 'user/profile.html')

@login_required
def ProfileUpdate(request):
     if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid():
             u_form.save()
             p_form.save()
             messages.success(request, f'Account Updated Successfully')
             return redirect('profile')
        else:
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
     context = {
          'u_form': u_form,
          'p_form': p_form
     }

     return render(request, 'user/profile_update.html', context)