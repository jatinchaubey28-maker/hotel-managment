from django.contrib import admin
from .models import Rooms, Booking, HotelGallery

# 1. Rooms Admin
# Note: Humne models.py mein 'Rooms' (S ke saath) naam rakha hai
@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'price', 'is_available')
    list_filter = ('room_type', 'is_available')
    search_fields = ('room_type',)



# 3. Booking Admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'room_type', 'arrival_date', 'payment_mode', 'status')
    list_filter = ('room_type', 'payment_mode', 'status', 'arrival_date')
    search_fields = ('name', 'mobile', 'email')

# 4. Hotel Gallery Admin
@admin.register(HotelGallery)
class HotelGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured')
    list_editable = ('is_featured',) # Admin se hi direct tick mark kar sakte hain

# Admin Header Customization
admin.site.site_header = "Hotel Management Admin"
admin.site.site_title = "Hotel Admin Portal"
admin.site.index_title = "Welcome to Hotel Management System"