# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import uuid

# Create your models here.


class UserModel(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=120)
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=40)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.username

class LoginModel(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=40)

class SessionToken(models.Model):
	user = models.ForeignKey(User)
	session_token = models.CharField(max_length=255)
	last_request_on = models.DateTimeField(auto_now=True)
	created_on = models.DateTimeField(auto_now_add=True)
	is_valid = models.BooleanField(default=True)

	def create_token(self):
		self.access_token = uuid.uuid4()






