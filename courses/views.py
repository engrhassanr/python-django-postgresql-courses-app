from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Course
from .forms import CourseForm, UserForm

def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to user list page
    else:
        form = UserForm()
    
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Create User'})

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to user list page
    else:
        form = UserForm(instance=user)

    return render(request, 'users/user_form.html', {'form': form, 'title': 'Edit User'})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully.")
        return redirect('user_list')

    return render(request, 'users/user_list.html', {'users': User.objects.all()})

# Course Managements
def course_list(request):
    courses = Course.objects.all()  # Fetch all courses
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Redirect to course list
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Create Course'})

def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Redirect to course list after saving
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Edit Course'})


def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course deleted successfully.")
        return redirect('course_list')

    return render(request, 'courses/course_list.html', {'courses': Course.objects.all()})
