# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

	title = models.CharField(max_length=255)
	post = models.TextField()
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now=True)
	blocked = models.BooleanField(default=False)

	class Meta:
		db_table = "posts"
		ordering = ["-id"]

	def __str__(self):

		return self.title


class BlockedPost(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)

	class Meta:
		db_table = "blocked_post"
		ordering = ["-id"]

	def __str__(self):
		return self.post.title
