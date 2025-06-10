from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-payment/', views.payment_form, name='payment-form'),
]
