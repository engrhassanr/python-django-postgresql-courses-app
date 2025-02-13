from django.urls import path
from .views import create_user, edit_user, user_list, create_course, edit_course, course_list, course_detail, delete_user

urlpatterns = [
    path('', course_list, name='course_list'),  # Course list page
    path('<int:course_id>/', course_detail, name='course_detail'),  # Detail page
    path('course/create/', create_course, name='create_course'),
    path('course/edit/<int:course_id>/', edit_course, name='edit_course'),

    # New user URLs
    path('users/', user_list, name='user_list'),
    path('users/create/', create_user, name='create_user'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),  # Delete route
]
