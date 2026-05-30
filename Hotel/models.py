from django.db import models
from django.core.validators import RegexValidator


# 2. ROOMS MODEL (Combined for your Template)
class Rooms(models.Model):
    ROOM_TYPES = (
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('DELUXE', 'Deluxe'),
        ('SUITE', 'Suite'),
    )
    room_type = models.CharField(max_length=100, choices=ROOM_TYPES)
    room_image = models.ImageField(upload_to='room_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - {self.price}"

# 3. BOOKING MODEL
class Booking(models.Model):
    ROOM_TYPES = [
        ('Deluxe', 'Deluxe Room'),
        ('Luxury', 'Luxury Suite'),
        ('Queen', 'Queen Room'),
    ]
    PAYMENT_MODES = [
        ('Online', 'Online Payment'),
        ('Cash', 'Cash at Hotel'),
    ]
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CHECKED_IN', 'Checked In'),
        ('CHECKED_OUT', 'Checked Out'),
        ('CANCELLED', 'Cancelled'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODES)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} - {self.name}"

# 4. HOTEL GALLERY (Single instance)
class HotelGallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    is_featured = models.BooleanField(default=False) # Ab admin error nahi dega

    def __str__(self):
        return self.title