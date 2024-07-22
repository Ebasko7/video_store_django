from django.db import models

class Client(models.Model):
     account_type = models.CharField(255)
     email = models.EmailField()
     active = models.BooleanField()
    
class Video(models.Model):
     title = models.CharField(255)
     in_stock = models.BigIntegerField()
     rating = models.CharField()

class Person(models.Model):
     first_name = models.CharField(255)
     last_name = models.CharField(255)
     middle_init = models.CharField(2)
     age = models.IntegerField()
    
class Address (models.Model):
     street = models.CharField(255)
     zipcode = models.BigIntegerField(6)
     state = models.CharField(2)
     appt_num = models.BigIntegerField()

class Store (models.Model):
     name = models.CharField()
     number_of_employees = models.IntegerField()
     rating = models.FloatField()
     owner = models.CharField(255)