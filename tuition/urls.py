from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('admindashboard/', views.admindashboard, name='admindashboard')
    ]
