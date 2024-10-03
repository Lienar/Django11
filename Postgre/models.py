from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    size = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    password = models.CharField(max_length=300)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Sets(models.Model):
    name = models.CharField(max_length=30)
    games_num = models.IntegerField()
    games_list = models.CharField(max_length=300)
    is_discont = models.BooleanField(default=False)

    def __str__(self):
        return self.name
