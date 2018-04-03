# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from generic.decorators import login_required
from django.http import JsonResponse

from generic.models import BadWordList

from .forms import (
					PostForm,
					BlockForm
				) 
from .models import Post, BlockedPost
from django.contrib.auth.models import User

# Create your views here.

@login_required
def dashboard(request):

	template = "base.html"

	context = {}

	
	blocked_user_pks = BlockedPost.objects.filter(
											blocked_by=request.user,
											blocked_whom_id__isnull=False
										).values_list(
											'blocked_whom_id',
											flat=True
										)

	blocked_post_pks = BlockedPost.objects.filter(
											blocked_by=request.user,
											post__isnull=False
										).values_list(
											'post_id',
											flat=True
										)


	posts = Post.objects.all()
	posts = posts.exclude(
						user_id__in=blocked_user_pks
					).exclude(
						id__in=blocked_post_pks
					)
	
	admin_users = User.objects.filter(is_superuser=True).values_list(
										"pk", flat=True
										)
							
	users = User.objects.all().exclude(
										pk=request.user.pk
										).exclude(
										pk__in=admin_users
										)
	
	
	users = users.exclude(pk__in=blocked_user_pks)


	context["user"] = request.user
	context["posts"] = posts
	context["users"] = users
	context["post_count"] = posts.count()
	context["user_count"] = users.count()

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


@login_required
def block_user(request):
	data = {}
	form = BlockForm(request.POST)
	if form.is_valid():
		
		words = form.cleaned_data.get("words")
		post_id = form.cleaned_data.get("post_id")
		is_user_blocked = form.cleaned_data.get("is_user_blocked")
		is_post_blocked = form.cleaned_data.get("is_post_blocked")

		post_obj = get_object_or_404(Post, pk=post_id)

		words_list = words.split(",")
		for word in words_list:
			word = word.strip()
			word = word.lower()
			if not BadWordList.objects.filter(word__iexact=word).exists():
				BadWordList.objects.create(word=word, created_by=2)

		blocked_obj = BlockedPost.objects.create(
				blocked_by=request.user
			)
		if is_user_blocked:
			blocked_obj.is_user_blocked= True
			blocked_obj.blocked_whom = post_obj.user
		if is_post_blocked:
			blocked_obj.post = post_obj

		blocked_obj.save()


		data["status"] = 1
		data["message"] = "Post successfuly blocked"

	else:
		data["status"] = -1
		data["errors"] = form.errors 
		data["message"] = "Please fix the errors."
	return JsonResponse(data)