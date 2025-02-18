# courses/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Course, Profile
from .forms import CourseForm, UserForm
from .forms import ProfileUpdateForm 

def register(request):
    roles = Profile.ROLE_CHOICES
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        role = request.POST.get('role', 'student')  # Ensure a default role
        if form.is_valid():
            user = form.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.role = role
            profile.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form, 'roles': roles})

@login_required
def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Create User'})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  
    else:
        form = UserForm(instance=user)

    return render(request, 'users/user_form.html', {'form': form, 'title': 'Edit User'})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully.")
        return redirect('user_list')
    return render(request, 'users/user_list.html', {'users': User.objects.all()})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Create Course'})

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Edit Course'})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course deleted successfully.")
        return redirect('course_list')
    return render(request, 'courses/course_list.html', {'courses': Course.objects.all()})

# user login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # Check if the profile exists and set the role in the session
                try:
                    profile = user.profile
                    request.session['role'] = profile.role  # Set the role in session
                except Profile.DoesNotExist:
                    request.session['role'] = 'student'  # Fallback to 'student' if no profile

                messages.success(request, "Login successful!")
                return redirect('course_list')  # Redirect after successful login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


@login_required
def update_role(request, user_id):
    user = User.objects.get(id=user_id)
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect after updating role
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, "update_role.html", {"form": form, "title": "Update Role"})

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session["role"] = user.profile.role  # Store role in session
            return redirect("dashboard")  # Redirect after login

    return render(request, "login.html", {"form": form})
