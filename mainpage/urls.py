from django.urls import path

from . import views

urlpatterns = [
    path('/blue', views.blue, name='blue'),
    path('', views.index, name='index'),
    path('JSON', views.json, name='json'),
    path('date', views.date_test, name='date')
]