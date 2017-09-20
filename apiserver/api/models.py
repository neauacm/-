# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Semester(models.Model):
    name = models.CharField(max_length=20)
    status = models.IntegerField()

    def __unicode__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=20)
    class_time = models.IntegerField()
    week = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.ForeignKey(User)
    classroom = models.CharField(max_length=20)
    cost = models.IntegerField()
    limit = models.IntegerField()
    start_date = models.DateField()
    status = models.IntegerField()
    semester = models.ForeignKey(Semester)

    def __unicode__(self):
        return self.name


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    phone = models.IntegerField()
    family = models.CharField(max_length=20)
    family_phone = models.CharField(max_length=20)
    education = models.CharField(max_length=20)
    job_title = models.CharField(max_length=20)
    political = models.CharField(max_length=20)
    user_type = models.IntegerField()
    class_list = models.ManyToManyField(Class)
    user_info = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user
