from django.shortcuts import render, redirect
from .models import Booking, Rooms, HotelGallery 
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# 1. HOME PAGE
def index(request):
    rooms = Rooms.objects.all()[:3] 
    gallery_items = HotelGallery.objects.filter(is_featured=True) 
    return render(request, 'index.html', {'rooms': rooms, 'gallery_items': gallery_items})

# 2. ROOMS PAGE
def room(request):
    rooms_data = Rooms.objects.all()
    context = {
        'rooms': rooms_data
    }
    return render(request, 'room.html', context)

# 3. FINALIZED BOOKING LOGIC (Email + Database)
def booking(request):
    if request.method == "POST":
        # Form se data nikalna
        v_name = request.POST.get('guest_name')
        v_email = request.POST.get('guest_email')
        v_mobile = request.POST.get('guest_mobile')
        v_room = request.POST.get('room_type')
        v_pay = request.POST.get('payment')
        v_arr = request.POST.get('arrival')
        v_dep = request.POST.get('departure')

        # Check karein ki zaroori fields bhari hain
        if v_name and v_email:
            # A. Database mein booking save karna
            try:
                Booking.objects.create(
                    name=v_name,
                    email=v_email,
                    mobile=v_mobile,
                    room_type=v_room,
                    payment_mode=v_pay,
                    arrival_date=v_arr,
                    departure_date=v_dep
                )
                
                # B. Email bhejne ka logic
                subject = f"Booking Confirmed - Hotel Stay"
                message = f"""
                Hi {v_name},

                Your booking has been successfully confirmed at our hotel!

                Booking Details:
                ---------------------------
                Room Type: {v_room}
                Arrival: {v_arr}
                Departure: {v_dep}
                Payment Mode: {v_pay}
                ---------------------------

                Thank you for choosing us. We look forward to seeing you!
                """
                
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [v_email],
                    fail_silently=False,
                )

                # C. Success page par bhej dena
                return render(request, 'success.html', {'name': v_name})

            except Exception as e:
                # Agar koi error aaye (jaise network issues)
                messages.error(request, f"Something went wrong: {e}")
                return redirect('booking')
        else:
            messages.error(request, "Please fill all required fields.")
            
    return render(request, 'booking.html')

# 4. GALLERY PAGE
def gallery(request):
    gallery_items = HotelGallery.objects.all()
    return render(request, 'gallery.html', {'gallery_items': gallery_items})

# 5. SIMPLE PAGES
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')