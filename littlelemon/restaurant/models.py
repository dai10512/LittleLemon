from django.db import models
# Create your models here.


class Menu(models.Model):
    id = models.AutoField(primary_key=True, unique=True, max_length=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(max_length=5)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    id = models.AutoField(primary_key=True, unique=True, max_length=11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(max_length=6)
    booking_date = models.DateField()

    def __str__(self):
        return self.name + ' - ' + str(self.booking_date)
