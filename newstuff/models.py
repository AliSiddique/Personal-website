from django.db import models

class Vote(models.Model):
    title = forms.CharField(max_length=150),
