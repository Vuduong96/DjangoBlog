from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Step 1: Create Views -> Create form -> Create template -< Create url patterns
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # save password, hashed password
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

