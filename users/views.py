from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method  == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Your are now able to login')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form': form,
        'title_page': 'Login'
    }

    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    context = {
        'title_page': 'Profile'
    }
    return render(request, 'users/profile.html', context)
