from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm, ClassroomCreationForm, JoinClassroomForm
from .models import Classroom, Membership

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    created_classrooms = request.user.teacher_classrooms.all()
    joined_classrooms = Membership.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {
        'created_classrooms': created_classrooms,
        'joined_classrooms': joined_classrooms
    })

@login_required
def create_classroom(request):
    if request.method == 'POST':
        form = ClassroomCreationForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.teacher = request.user
            classroom.save()
            return redirect('dashboard')
    else:
        form = ClassroomCreationForm()
    return render(request, 'create_classroom.html', {'form': form})

@login_required
def join_classroom(request):
    if request.method == 'POST':
        form = JoinClassroomForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                classroom = Classroom.objects.get(code=code)
                Membership.objects.get_or_create(user=request.user, classroom=classroom)
                return redirect('dashboard')
            except Classroom.DoesNotExist:
                form.add_error('code', 'Invalid Classroom Code')
    else:
        form = JoinClassroomForm()
    return render(request, 'join_classroom.html', {'form': form})
