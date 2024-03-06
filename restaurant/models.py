from django.db import models

# Create your models here.
class Menu(models.Model):
  ID = models.AutoField(primary_key=True,null=False,unique=True)
  Title = models.CharField(max_length=255)
  Price = models.DecimalField(max_digits=10,decimal_places=2,null=False)
  Inventory = models.IntegerField(default=5)

  def __str__(self):
    return self.Title

class Booking(models.Model):
  ID = models.AutoField(primary_key=True,null=False,unique=True)
  Name = models.CharField(max_length=255)
  No_of_guests = models.IntegerField(default=6)
  BookingDate = models.DateField()

  def __str__(self):
    return self.Name

