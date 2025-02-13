from django import forms
from django.contrib.auth.models import User
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['image', 'summary']
        widgets = {
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
