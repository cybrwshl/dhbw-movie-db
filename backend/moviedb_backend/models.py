from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'


class Movie(models.Model):
    name = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=12, decimal_places=0)
    overview = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

class Keyword(models.Model):
    name = models.CharField(max_length=30)
    movie = models.ForeignKey(Movie)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords'

class Company(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Role(models.Model):
    ROLE_TYPES = (
        ('A', 'Actor'),
        ('P', 'Producer'),
        ('W', 'Writer'),
        ('D', 'Director'),
    )
    type = models.CharField(max_length=1, choices=ROLE_TYPES, blank=False)
    movie = models.ForeignKey(Movie)
    person = models.ForeignKey(Person)
    additional_info = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
