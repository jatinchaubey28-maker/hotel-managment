from django.urls import path
from . import views

urlpatterns = [
    # 1. Home Page
    path('', views.index, name="index"),

    # 2. Booking Page (Jahan form submit hota hai)
    path('booking/', views.booking, name='booking'),

    # 3. Dynamic Pages (Inke liye views.py mein function hona chahiye)
    path('room/', views.room, name="room"),
    path('gallery/', views.gallery, name="gallery"),
    
    # 4. Static Pages
    path('about-us/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
]