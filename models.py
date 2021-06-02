from django.db import models

class Member(models.Model):
       email = models.EmailField(max_length=30)
       name = models.CharField(max_length=20)
       password = models.IntegerField(default=8)
       phone_number = models.IntegerField()
     


