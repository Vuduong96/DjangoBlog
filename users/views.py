from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Step 1: Create Views -> Create form -> Create template -< Create url patterns
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # save password, hashed password
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now be able to logout!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) # create instances
        p_form = ProfileUpdateForm(request.POST, 
                                request.FILES,  
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user) # create instances
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = { # create context as dictionary
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'users/profile.html', context) # pass context here

