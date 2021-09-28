from django.db import models
from django.utils.safestring import mark_safe

class Country(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()
    pincode = models.PositiveIntegerField(null=True)
    city_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    def  City_Image(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.city_pic))

    City_Image.allow_tags = True





class Subject(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField()
    status = models.BooleanField()

