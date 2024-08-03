from django.urls import path
from .views import *
urlpatterns = [
    path('post/',first_function,name='post'),
    path('get/',first_get, name='get'),
    path('register/',registation, name='register'),
    path('first_class/', first_class.as_view(), name='first_class'),
    path('second_class/<int:id>/', second_class.as_view(), name='second_class'),
    path('thirth_class/', thirth_class_generic.as_view(), name='thirth_class'),
    path('fourth_class/<int:id>/', fourth_class_generic.as_view(), name='fourth_class')
]
