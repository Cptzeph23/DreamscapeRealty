from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email



class NewUser(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Payment(models.Model):
    number = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return self.amount

class Rating(models.Model):
    textarea = models.TextField(max_length=500)

    def __str__(self):
        return self.textarea

""""
class NewProperty(models.Model):
    title = models.CharField(max_length=100)  # Title of the property
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Property price
    beds = models.PositiveIntegerField()  # Number of bedrooms
    baths = models.PositiveIntegerField()  # Number of bathrooms
    garages = models.PositiveIntegerField()  # Number of garages
    location = models.CharField(max_length=255)  # Location of the property
    image = models.ImageField(upload_to='property_images/')  # Directory to save images
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Auto-set timestamp

    def __str__(self):
        return self.title if self.title else f"Property {self.id}"

"""


