from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
# Create your models here.
class job(Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    pay = models.IntegerField()
    Contact = models.EmailField()
    Website = models.TextField(max_length=200)


    def __str__(self):
        return self.title



class contactStuff(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=200)
    def __str__(self):
        return self.name
