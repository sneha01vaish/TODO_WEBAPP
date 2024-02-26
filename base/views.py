from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from base.forms import TODOForm
from base.models import TODO
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority')
        return render(request, 'index.html', context={"form":form, 'todos': todos})

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context={
        "form": form
          }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password= password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context= {
                "form" : form
            }
            return render(request, 'login.html', context= context)
        
def signup(request):
   if request.method=='GET':
        form=UserCreationForm()
        context={
        "form" : form
           }
        return render(request, 'signup.html', context=context)
   else:

       form=UserCreationForm(request.POST)
       context={
             "form" : form }
       if form.is_valid():  # Corrected condition: form.is_valid() instead of form.is_valid
            user = form.save()
            if user is not None:
                return redirect('login')  # Redirect to the 'home' page if signup is successful
       return render(request, 'signup.html', context=context)
@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form =TODOForm(request.POST, request.FILES)
        if form.is_valid():
        #   print(form.cleaned_data)
          todoo=form.save(commit=False)
          todoo.user=user
          todoo.save()
        #   print(todoo)
          return redirect('home')
        else:
          return render(request, 'index.html', context={"form": form} )

def signout(request):
    logout(request)
    return redirect('login')

def delete_todo(request, id):
    print(id)    
    TODO.objects.get(pk=id).delete()
    return redirect('home')

def change_todo(request, id, status):
    print(id)    
    todo=TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')
    
