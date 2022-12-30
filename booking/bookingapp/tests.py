from django.test import TestCase

# Create your tests here.
from bookingapp.models import movies_ticketbooking,movie_details

class MyTest(TestCase):
	def test_record(self):
		try:
			obj = product(rating = "A",
	casts = "sam",
	genre = "action",
	language = "telugu",
	moviename = "avatar")
			obj.save()
			self.assertEquals(obj.language,telugu,"languagemismatch")
			self.assertEquals(obj.moviename,avatar,"moviename mismatch")
			
		except Exception as e:
			print('unable to insert request response')

class MyTest(TestCase):
	def test_record(self):
		try:
			obj = product(name = "vikas",
	
	language = "english",
	airingdate = 23-12-2022,
	theater = "cnc",
	city="kkd")
			obj.save()
			self.assertEquals(obj.language,english,"languagemismatch")
			self.assertEquals(obj.city,kakinada,"city mismatch")
			
		except Exception as e:
			print('unable to insert request response')