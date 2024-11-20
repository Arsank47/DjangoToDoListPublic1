from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from tasks.views import task_list, task_create, task_update, task_delete
from tasks.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login page
    path('register/', register, name='register'),  # Register page
    path('tasks/', task_list, name='task_list'),  # Task list page
    path('tasks/create/', task_create, name='task_create'),  # Create task page
    path('tasks/update/<int:pk>/', task_update, name='task_update'),  # Update task page
    path('tasks/delete/<int:pk>/', task_delete, name='task_delete'),  # Delete task page
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Logout
]

