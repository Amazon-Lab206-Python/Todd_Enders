# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, POST):
        errors = []
        if len(POST['first_name']) == 0:
            errors.append('First Name is required')
        if len(POST['last_name']) == 0:
            errors.append('Last Name is required')
        if len(POST['email']) == 0:
            errors.append('Email is required')
        if len(POST['age']) == 0:
            errors.append('Age is required')
        if len(errors) > 0:
            return (False, errors) # return the list of errors
        else: 
            # save the information
            new_user = User.objects.create(
                first_name = POST['first_name'],
                last_name = POST['last_name'],
                email_address = POST['email'],
                age = POST['age'],
            )
            # then what?
            return (True, new_user)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    age = models.IntegerField()
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name