from django.urls import path

from . import views

urlpatterns = [
    path('blue', views.blue, name='blue'),
    path('class/<int:term>/<slug:class_name>', views.classfinder, name="classfinder"),
    path('', views.index, name='index'),
    path('account', views.success, name="account"),
    path('API', views.success, name="API"),
    path('contact', views.success, name="contact"),

]