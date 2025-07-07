from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate
from .forms import *
# Create your views here.

def profile_view(request):
    profile = request.user.profile
    return render(request, 'users/profile.html', {'profile':profile})


def profile_edit(request):
    form = profileForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
        
        
    return render(request, 'users/profile_edit.html', {'form':form})
