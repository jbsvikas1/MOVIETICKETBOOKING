from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class BookingappView(APIView):
    serializer_class=BookmyshowSerializer
    def get(self,request):
        allmovies=movies_ticketbooking.objects.all().values()
        return Response({"name" : "vikas",
	"language": "telugu","airingdate" : 22-12-2022,
	"theater" : "cnc",
	"city" : "kkd",  "rating" : "A",
	"casts" : "heror",
	"genre" : "horror",
	"language" : "telugu",
	"moviename" : "avatar",  "ticketid" : 5,
	"seatno" : 2,
	"moviename" : "avatar",
	"moviedate" : 12-12-2022,
	"showtime" : 4


	})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=BookmyshowSerializer(data=request.data)
        if(serializer_obj.is_valid()):
        	ticket_cancle.objects.create(cancle=serializer_obj.data.get("cancle")),
        	ticketbooking.objects.create(bookticket=serializer_obj.data.get("bookticket")),
        allmovies=ticket_cancle.objects.all().filter(cancle=request.data["cancle"]).values()
        allmovies=ticketbooking.objects.all().filter(bookticket=request.data["bookticket"]).values()
        return Response({"cancle":"yes","bookticket":"3"})