from django.shortcuts import render,HttpResponse, redirect
from .models import Task
from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


from .forms import TaskForm


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('/login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/all_task/')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('/login/')



@login_required(login_url='/login/')
# Create your views here.
def home(request):
    return render(request, 'home.html')




@login_required(login_url='/login/')
def all_task(request):
    task = Task.objects.all()
    context={
        'tasks': task
    }
    return render(request,'all_task.html',context)



@login_required(login_url='/login/')
def add_task(request):
    if request.method== "POST":
        name = request.POST['name']
        newtask= Task(name=name)
        newtask.save()
        return redirect('/all_task/')
    elif request.method =='GET':
            return render(request,'add_task.html')
        
    else:
            return HttpResponse("Error!")
    


@login_required(login_url='/login/')
def delete_task(request, task_id=0):
    if task_id:
          try:
               task_remove = Task.objects.get(id=task_id)
               task_remove.delete()
               return redirect("/all_task/")
          except:
               return HttpResponse("enter valid one")
    task = Task.objects.all()







@login_required(login_url='/login/')
def edit_task(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/all_task/')

	context = {'form':form}

	return render(request, 'edit_task.html', context)



