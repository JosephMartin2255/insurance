from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.loginpage,name='loginpage'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('logout',views.logout,name='logout'),

]