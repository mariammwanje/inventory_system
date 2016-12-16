from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=12, default='')
    description = models.TextField()
    amount = models.IntegerField()

    def __unicode__(self):
        return self.title


class Help(models.Model):
    Description = models.CharField(max_length=200)

class Users(models.Model):
     name = models.CharField(max_length=200)
     email = models.EmailField
     position=models.CharField
     telephone_number = models.IntegerField()
     department = models.CharField
     position=models.CharField

     def __unicode__(self):
         return self.name