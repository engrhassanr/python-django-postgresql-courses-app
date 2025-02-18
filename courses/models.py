from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'

    def ready(self):
        try:
            import courses.signals  # Ensure signals are loaded
        except ImportError:
            logger.warning("courses.signals module not found. Ensure it's present for signal handling.")

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    summary = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    start_date = models.DateField(null=True, blank=True)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.user.username} - {self.role} ({self.user.email})"
