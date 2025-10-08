from django.contrib import admin
from django.urls import path, include  # <-- MUST ADD 'include' HERE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.coreurls')),  # <-- ADD THIS LINE
]