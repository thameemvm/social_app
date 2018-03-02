# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


CREATED_CHOICE = (
		(1, "admin"),
		(2, "user")
	)

class BadWordList(models.Model):

	word = models.CharField(max_length=128)
	active = models.BooleanField(default=True)
	created_by = models.PositiveIntegerField(
								choices=CREATED_CHOICE,
								default="1"
								)
	usercount = models.PositiveIntegerField(default=0)

	class Meta:
		db_table = "badwords_list"
		ordering = ["-id"]

	def __str__(self):
		return self.word

