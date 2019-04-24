# accounts/urls.py
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
]
