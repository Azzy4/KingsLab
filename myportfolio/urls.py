
from django.contrib import admin
from django.urls import path, include, re_path
from .views import index_view 
from .api import ContactAPIView
from .api import contact_api
from .views import contact_inquiry_list_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),  
    path('success/', success_view, name='success_view'),  
    path('api/contact/', ContactAPIView.as_view(), name='api_contact'),
    re_path(r'^.*$', index_view, name='home'), 
    path('api/contact/', contact_api, name='api_contact'),
path('api/contact-inquiries/', contact_inquiry_list_create, name='contact-inquiries'),
]