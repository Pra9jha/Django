from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import  login_required
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForms
def registration(request):
    if request.method=='POST':
       # form=UserCreationForm(request.POST)
       form=UserRegisterForms(request.POST)
       if form.is_valid():
          form.save()
          username=form.cleaned_data.get('username')
          messages.success(request,f'Accout created for {username}!')
          return redirect('login')
    else:
       # form=UserCreationForm()
         form=UserRegisterForms()
    # request.session.set_expiry(60)
    return render(request,'users/register.html',{'form':form})

