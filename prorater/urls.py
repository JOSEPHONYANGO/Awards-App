from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('auth/login/', views.login_user,name='login'),
    path('auth/register/', views.register_user,name='register'),
    path('profile/', views.profile,name='profile'),
    path('project/<projectid>', views.profile,name='profile'),
    path('api/profiles/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectsList.as_view())
    
]
