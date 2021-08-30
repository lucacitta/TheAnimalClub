from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user=authenticate(username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],)
            login(request,new_user)
            return redirect ('/')
    else:
        form=UserRegisterForm()
    context={'registerForm':form}
    return render(request, 'registro/register.html', context)
