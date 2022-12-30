from django.contrib import admin

# Register your models here.
from bookingapp.models import movies_ticketbooking,movie_details,ticket_booking,ticket_cancle,booking_details,ticket_details,ticketbooking

# Register your models here.
admin.site.register(movies_ticketbooking)
admin.site.register(movie_details)
admin.site.register(ticket_booking)
admin.site.register(ticket_cancle)
admin.site.register(booking_details)
admin.site.register(ticket_details)
admin.site.register(ticketbooking)

