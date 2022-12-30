# Generated by Django 4.1.4 on 2022-12-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='movie_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('U', 'U'), ('UA', 'U/A'), ('A', 'A'), ('R', 'R')], max_length=2)),
                ('casts', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=30)),
                ('moviename', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='movies_ticketbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('language', models.CharField(choices=[('ENGLISH', 'English'), ('BENGALI', 'Bengali'), ('HINDI', 'Hindi'), ('TAMIL', 'Tamil'), ('TELUGU', 'Telugu')], max_length=30)),
                ('airingdate', models.DateField()),
                ('theater', models.CharField(max_length=30)),
                ('city', models.CharField(choices=[('KAKINADA', 'Kakinada'), ('VIZAG', 'Vizag'), ('DELHI', 'Delhi'), ('KOLKATA', 'Kolkata'), ('MUMBAI', 'Mumbai'), ('CHENNAI', 'Chennai'), ('BANGALORE', 'Bangalore'), ('HYDERABAD', 'Hyderabad')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='ticket_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnum', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('payment_type', models.CharField(choices=[('Credit Card', 'Credit Card')], default='Credit Card', max_length=11)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='ticket_cancle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancle', models.CharField(default='YES', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ticket_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketid', models.IntegerField()),
                ('seatno', models.IntegerField()),
                ('moviename', models.CharField(max_length=10)),
                ('moviedate', models.DateField()),
                ('showtime', models.TimeField()),
            ],
        ),
    ]
