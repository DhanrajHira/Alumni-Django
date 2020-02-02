from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.addRecord),
	path('', views.home),
	path('allrecords/', views.allRecords),
	path('delete/', views.deleteRecord)
]
