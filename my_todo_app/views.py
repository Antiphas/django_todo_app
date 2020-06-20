from django.shortcuts import render, redirect
from .models import StaffBiodata
from .forms import StaffForm, CreateUser
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def index_page(request):
    return render(request, "my_todo_app/index_page.html")


@login_required(login_url='user_login')
def display_data(request):
    displays = StaffBiodata.objects.all().order_by('firstname')
    context = {
        'displays': displays,
    }
    return render(request, 'my_todo_app/display_data.html', context)


@login_required(login_url='user_login')
def insert_data(request):
    form = StaffForm()
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            phone = request.POST['phone']
            if StaffBiodata.objects.filter(email=email).exists():
                messages.warning(request, "Email Already Exist")
                return redirect("my_todo_app:insert_data")
            if StaffBiodata.objects.filter(phone=phone).exists():
                messages.warning(request, "Phone Number Already Exist")
                return redirect("my_todo_app:insert_data")
            else:
                form.save()
                messages.info(request, 'New record added Successfully...')
                return redirect("my_todo_app:display_data")
    return render(request, "my_todo_app/home.html", {'form': form})


@login_required(login_url='user_login')
def update_data(request, pk):
    get_data = StaffBiodata.objects.get(id=pk)
    get_all = StaffBiodata.objects.all()
    form = StaffForm(instance=get_data)
    if request.method == "POST":
        form = StaffForm(request.POST, instance=get_data)
        email = request.cleaned_data.get('email')
        if form.is_valid:
            if StaffBiodata.objects.filter(email=email).exists:
                messages.warning(request, "Email Already Used by another User")
                return redirect("my_todo_app:update_data")
            else:
                form.save()
                messages.success(request, "Record is successfully Updated..")
                return redirect("my_todo_app:display_data")
    else:
        context = {
            'form': form,
        }
        return render(request, 'my_todo_app/home.html', context)


@login_required(login_url='user_login')
def delete_data(request, pk):
    get_data = StaffBiodata.objects.get(id=pk)
    get_data.delete()
    messages.success(request, get_data.firstname + " Has been deleted Successfully")
    return redirect("my_todo_app:display_data")


def register(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User successfully created")
            redirect('my_todo_app:display_data')
    context = {
        'form': form,
    }
    return render(request, "my_todo_app/register.html", context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('my_todo_app:display_data')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"Login Successfully")
                return redirect("my_todo_app:display_data")
            else:
                messages.info(request, "Invalid Username or Pasword")
                return redirect("my_todo_app:user_login")
        form = AuthenticationForm()

        return render(request, "my_todo_app/login.html", {'form': form})


def user_logout(request):
    logout(request)
    return redirect("my_todo_app:index_page")