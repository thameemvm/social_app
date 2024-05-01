# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	post = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now=True)
	blocked = models.BooleanField(default=False)

	class Meta:
		db_table = "posts"
		ordering = ["-id"]

	def __str__(self):

		return self.title


class BlockedPost(models.Model):
	id = models.AutoField(primary_key=True)
	blocked_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='blocked_by')
	blocked_whom = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='blocked_whom')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	is_user_blocked = models.BooleanField(default=False)

	class Meta:
		db_table = "blocked_post"
		ordering = ["-id"]

	def __str__(self):
		return str(self.pk)

