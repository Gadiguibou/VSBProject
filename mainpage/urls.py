from django.urls import path

from . import views

urlpatterns = [
    path('/blue', views.index, name='blue'),
    path('', views.index, name='index'),
    path('JSON', views.index, name='json'),
]