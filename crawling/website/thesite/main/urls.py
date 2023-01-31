from django.urls import path 
from . import views


urlpatterns = [
    path('index/', views.index),
    path('archive/', views.archive),
    path('archive/<number_of_months>/', views.archive),
    path('dbtest/', views.db_test),
    path('dbtest/<keyword>/', views.db_test),
    path('key words/', views.key_words),
    path('statistics/', views.statistics),
    path('index2/', views.index2),
    path('api/', views.api),
    path('api/<keyword>/', views.api)
 

]