from django.urls import path
from .views import (
    create_user, edit_user, user_list, delete_user,
    create_course, edit_course, course_list, course_detail, delete_course
)

urlpatterns = [
    path('', course_list, name='course_list'),  # Index/Home Page
    path('course/create/', create_course, name='create_course'),
    path('course/edit/<int:course_id>/', edit_course, name='edit_course'),
    path('course/delete/<int:course_id>/', delete_course, name='delete_course'),

    # User URLs
    path('users/', user_list, name='user_list'),
    path('users/create/', create_user, name='create_user'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),

    # Keep course detail at the bottom to prevent conflicts
    path('course/<int:course_id>/', course_detail, name='course_detail'),
]
