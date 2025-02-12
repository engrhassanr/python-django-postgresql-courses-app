from django.urls import path
from .views import course_list, course_detail, create_course, edit_course

urlpatterns = [
    path('', course_list, name='course_list'),  # Homepage (course list)
    path('<int:course_id>/', course_detail, name='course_detail'),  # Course details
    path('course/create/', create_course, name='create_course'),  # Create a course
    path('course/edit/<int:course_id>/', edit_course, name='edit_course'),  # Edit course
]
