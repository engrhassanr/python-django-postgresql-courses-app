# forms.py
from django import forms
from django.contrib.auth import get_user_model
from .models import Course

# CourseForm for creating or editing a course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'image', 'summary', 'description', 'price', 'category', 'duration', 'start_date', 'instructor', 'is_published']
        widgets = {
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'instructor': forms.Select(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# UserForm for managing User data
class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()  # Dynamically get the User model
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
