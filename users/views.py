from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Category


def sign_up(request):
    """ Function to ctreate new user account """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('sign_in')
    else:
        form = UserRegisterForm()
        
    #Add category list to sidebar in sign_up view
    context = {
        'form': form,
        'categories': Category.objects.all(),
    }

    return render(request, 'users/sign_up.html', context)


@login_required
def profile(request):
    """ Function to create and update user profile """   
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    #Add category list to sidebar in profile view
    context["categories"] = Category.objects.all()    
    
    return render(request, 'users/profile.html', context=context)