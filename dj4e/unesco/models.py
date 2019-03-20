from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=800)
    justification = models.CharField(max_length=800)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area = models.FloatField(null=True)
    year = models.PositiveIntegerField(null=True)
    iso = models.ForeignKey('Iso', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)


    def __str__(self) :
        return self.name
