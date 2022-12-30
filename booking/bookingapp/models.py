from django.db import models

# Create your models here.
class movies_ticketbooking(models.Model):
	 city_choice=(
	 	('KAKINADA','Kakinada'),
	 	('VIZAG','Vizag'),
        ('DELHI','Delhi'),
        ('KOLKATA','Kolkata'),
        ('MUMBAI','Mumbai'),
        ('CHENNAI','Chennai'),
        ('BANGALORE','Bangalore'),
        ('HYDERABAD','Hyderabad'),

    )
	 language_choice=(
        ('ENGLISH', 'English'),
        ('BENGALI', 'Bengali'),
        ('HINDI', 'Hindi'),
        ('TAMIL', 'Tamil'),
        ('TELUGU', 'Telugu'),
    )
	 name = models.CharField(max_length = 100)
	 language = models.CharField(max_length=30,choices=language_choice)
	 airingdate = models.DateField()
	 theater = models.CharField(max_length = 30)
	 city = models.CharField(max_length=9,choices=city_choice,null=False)
	 def __str__(self):
	 	return self.name 


class movie_details(models.Model):
	rating_choice = (
        ('U', 'U'),
        ('UA', 'U/A'),
        ('A', 'A'),
        ('R', 'R'),
    )

	rating =  models.CharField(max_length=2, choices=rating_choice)
	casts = models.CharField(max_length = 30)
	genre = models.CharField(max_length = 30)
	language = models.CharField(max_length = 30)
	moviename = models.CharField(max_length = 30)

	def __str__(self):
		return self.moviename


class ticket_booking(models.Model):
     payment_choice = (
        ('Credit Card', 'Credit Card'),
    )
     idnum = models.CharField(max_length=100)
     payment_type = models.CharField(max_length=11, choices=payment_choice,default='Credit Card')
     paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
     def __str__(self):
     	return str(self.idnum)



class ticket_cancle(models.Model):
	cancle = models.CharField(max_length = 30,default='YES')
	
	def _str_(self):
		return self.cancel


class booking_details(models.Model):
	details = models.CharField(max_length = 30)

	def __str__(self):
		return self.details

class ticket_details(models.Model):
	ticketid = models.IntegerField()
	seatno = models.IntegerField()
	moviename = models.CharField(max_length = 10)
	moviedate = models.DateField()
	showtime = models.TimeField()

	def __str__(self):
		return self.moviename

class ticketbooking(models.Model):

	bookticket = models.IntegerField(max_length =5,default='max 5 tickets for each booking')
