from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('capture_student/', views.capture_student, name='capture_student'),
    path('students/attendance/', views.student_attendance_list, name='student_attendance_list'),
    path('selfie-success/', views.selfie_success, name='selfie_success'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('students/', views.student_list, name='student-list'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),
    path('students/<int:pk>/delete/', views.student_delete, name='student-delete'),
    path('capture-and-recognize/', views.capture_and_recognize, name='capture_and_recognize'),
]
