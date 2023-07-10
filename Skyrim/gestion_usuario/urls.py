from django.contrib import admin
from django.urls import path
from skyapp.views import logIn, logOut, signUp

urlpatterns = [
    
    # log in
    path('login', logIn, name='login'),
    
    # log out
    path('logout/', logOut, name='logout'),
    
    # sign up
    path('signup', signUp, name='signup'),
    
]
