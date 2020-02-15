from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
app_name='myapp'

urlpatterns=[
    path('add/',views.RegisterView.as_view()),
    path('show/',views.UserShowView.as_view(),name='show'),
    



]

