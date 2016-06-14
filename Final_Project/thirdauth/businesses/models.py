from __future__ import unicode_literals

from django.db import models

class Business(models.Model):
    business_name = models.CharField(max_length=100)
    explanation = models.CharField(max_length=1000, blank=True, null=True, default = '')

    def __unicode__(self):
        return self.business_name



class Goal(models.Model):
    goal_name = models.CharField(max_length=100)
    business_name = models.ForeignKey(Business, blank=True, null=True)
    explanation = models.CharField(max_length=500)

    def __unicode__(self):
        return self.goal_name


class Goal_score(models.Model):
    goal_name = models.ForeignKey(Goal, blank=True, null=True)
    score = models.IntegerField(default=0)
    goal = models.IntegerField(default=0)
    school_year = models.IntegerField(default=0)




class Worker(models.Model):
    name = models.CharField(max_length=50)
    address =models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=50, blank=True, null=True, default = '')
    business_name = models.ForeignKey(Business, blank=True, null=True)
    department = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    major = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name



class Resource(models.Model):
    locations = models.ManyToManyField('Location')
    materials = models.ManyToManyField('Material')
    business_name = models.ForeignKey(Business, blank=True, null=True)

    def __unicode__(self):
        return 'Resource'



class Finance(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    business_name = models.ForeignKey(Business, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Finance_score(models.Model):
    finance_name = models.ForeignKey(Finance, blank=True, null=True)
    price = models.IntegerField(default=0)
    goal = models.IntegerField(default=0)
    year = models.IntegerField(default=2015)



class Location(models.Model):
    name = models.CharField(max_length=100)
    business_name = models.ForeignKey(Business, blank=True, null=True)
    address = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Room(models.Model):
    name = models.ForeignKey(Location, blank=True, null=True)
    number = models.IntegerField(default=0)
    reservation = models.CharField(max_length=50, default='')




class Material(models.Model):
    name = models.CharField(max_length=100)
    business_name = models.ForeignKey(Business, blank=True, null=True)
    number = models.IntegerField(default=0)
    unit = models.CharField(max_length=100, blank=True, null=True, default = '')
    standard = models.CharField(max_length=100, blank=True, null=True, default = '')
    used_number = models.IntegerField(blank=True, null=True, default=0)
    not_used_number = models.IntegerField(blank=True, null=True, default=0)

    def __unicode__(self):
        return self.name
