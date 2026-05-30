from django.contrib import admin
from django.urls import path, include

# Media files (images) ko display karne ke liye imports
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel ka path
    path('admin/', admin.site.urls),
    
    # Aapke App (Hotel) ki saari URLs ko include karna
    path('', include('Hotel.urls')),
]

# Development ke waqt uploaded images ko browser par dikhane ke liye
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)