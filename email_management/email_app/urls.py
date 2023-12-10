from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_contact/', views.add_contact, name = 'add_contact'),
    path('see_contact/', views.see_contact, name = 'see_contact'),
    path('send_message/', views.send_message, name = 'send_message'),
    path('see_history/', views.see_history, name = 'see_history'),
    path('submit_contact/', views.submit_contact, name = 'submit_contact'),
]
