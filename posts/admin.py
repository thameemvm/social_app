# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

class BlockedPostAdmin(admin.ModelAdmin):

	list_display = ["blocked_user"]

	search_fields = [
					"blocked_whom__first_name", 
					"blocked_whom__last_name",
					"blocked_whom__email",
					]

	def get_queryset(self, request):
		qs = super(BlockedPostAdmin, self).get_queryset(request)

		return qs.filter(blocked_by__isnull=True)

	def blocked_user(self, instance):
		return instance.blocked_whom.get_full_name()


admin.site.register(BlockedPost, BlockedPostAdmin)