# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from generic.decorators import login_required
from django.http import JsonResponse

from .forms import (
					PostForm,
					BlockForm
				) 
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

@login_required
def dashboard(request):

	template = "base.html"

	context = {}

	context["user"] = request.user

	context["posts"] = Post.objects.all()
	admin_user = User.objects.filter(is_superuser=True).values_list(
										"pk", flat=True
										)
	context["users"] = User.objects.all().exclude(
										pk=request.user.pk
										).exclude(
										pk__in=admin_user
										)

	context["post_count"] = Post.objects.all().count()
	context["user_count"] = User.objects.all().count()

	return render(request, template, context)


@login_required
def create_post(request):

	data = {}
	form = PostForm(request.POST)
	if form.is_valid():
		form_instance = form.save(commit=False)
		form_instance.user = request.user
		form.save()

		data["status"] = 1
		data["message"] = "Post successfuly created"

	else:
		data["status"] = -1
		data["errors"] = form.errors 
		data["message"] = "Please fix the errors."
	return JsonResponse(data)
