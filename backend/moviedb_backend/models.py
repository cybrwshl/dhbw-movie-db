from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()


class Movie(models.Model):
    name = models.CharField(max_length=50)
    budget = models.DecimalField()
    overview = models.CharField(max_length=500)


class Keyword(models.Model):
    name = models.CharField(max_length=30)
    movie = models.ForeignKey(Movie)


class Role(models.Model):
    ROLE_TYPES = (
        ('A', 'Actor'),
        ('P', 'Producer'),
        ('W', 'Writer'),
    )
    type = models.CharField(max_length=1, choices=ROLE_TYPES, blank=False)
    movie = models.ForeignKey(Movie)
    person = models.ForeignKey(Person)
    additional_info = models.CharField(max_length=30)