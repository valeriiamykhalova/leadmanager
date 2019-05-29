from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('frontend.urls')),
    re_path(r'', include(('leads.urls', 'leads'), namespace='leads')),
    re_path(r'', include(('accounts.urls', 'accounts'), namespace='accounts')),
]
