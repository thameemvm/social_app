# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import (
								authenticate, 
								login as dj_login,
								logout as dj_logout
							)

from .forms import LoginForm



# Create your views here.
def login(request):
	
	context = {}
	template = "auth_base.html"
	form = LoginForm()
	next = request.GET.get('next', "")
	if request.method == "POST":
		remember = request.POST.get("remember", False)
		if not remember:
			request.session.set_expiry(0)

		form = LoginForm(request.POST)	
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username,password=password)
			dj_login(request, user)
			if next:
				return redirect(next)
			return redirect('posts:dashboard')
	context = {
		'next':next,
		'form': form,
	}

	return render(request, template, context)



def logout(request):
	if not request.user.is_authenticated():
		redirect("accounts:login")
	django_logout(request)
	messages.success(request, 'Your are successfully signed out')
	return redirect('accounts:login')	