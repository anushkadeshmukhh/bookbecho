from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1, name='index1'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('login/add_user/',views.add_user,name='add_user'),
    path('signup/check_user/',views.check_user,name='check_user'),
]