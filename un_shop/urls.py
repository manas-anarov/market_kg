from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.CreateOrder.as_view(), name='create'),
	path('create-front/', views.CreateViewFront.as_view(), name='create'),
]