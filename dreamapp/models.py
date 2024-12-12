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
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fname

class Payment(models.Model):
    number = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return self.amount








