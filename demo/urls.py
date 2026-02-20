from django.contrib import admin
from django.urls import path,include
from.import views
app_name="demo"
urlpatterns = [
    path('',views.index,name="index"),
    path('validate',views.add,name="add"),
   # path('/result',views.result,name="result")
]