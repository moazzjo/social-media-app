from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from .models import Profile
from django.contrib.auth import authenticate, logout
from .forms import *
# Create your views here.

def profile_view(request, username = None):
    if username:
        profile = get_object_or_404(User, username=username)
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
    return render(request, 'users/profile.html', {'profile':profile})


def profile_edit(request):
    form = profileForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
        
        
    return render(request, 'users/profile_edit.html', {'form':form})



def profile_delete(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, "account deleted successfully")
        return redirect('home')
    return render(request, "users/profile_delete.html")
