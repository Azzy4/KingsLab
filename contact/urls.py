from django.urls import path
from .views import contact, success_view, include

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('success/', success_view, name='success_view'),
]
