from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import (
								authenticate, 
								login as dj_login,
								logout as dj_logout
							)

from .forms import LoginForm, SignUpForm

from django.http import JsonResponse
from django.core.urlresolvers import reverse

from django.contrib import messages


# def user_redirect(request):
# 	if request.user.is_authenticated:
# 		if request.user.is_superuser:
# 			return redirect("web_admin:dashboard")
# 		elif (request.user.is_active
# 			and 
# 			"operator" in request.user.groups.values_list("name", flat=True) ):
# 			return redirect("operators:dashboard")
# 		else:
# 			raise Http404
# 	else:
# 		return redirect("accounts:login")
		



def login(request):
	# import pdb; pdb.set_trace()
	context = {}
	template = "auth_base.html"
	form = LoginForm()
	next = request.GET.get('next', "")
	if request.method == "POST":
		data = {}
		remember = request.POST.get("remember", False)
		if not remember:
			request.session.set_expiry(0)

		form = LoginForm(request.POST)	
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username,password=password)
			dj_login(request, user)

			data["status"] = 1
			data["redirect"] = reverse('posts:dashboard')
			data["message"] = "User successfully login"
			if next:
				data["redirect"] = next
				
		else:

			data["status"] = -1
			data["message"] = "Please correct the errors"
			data["errors"] = form.errors
		return JsonResponse(data)
	context = {
		'next':next,
		'form': form,
	}

	return render(request, template, context)



def logout(request):
	if not request.user.is_authenticated:
		redirect("accounts:login")
	dj_logout(request)
	messages.success(request, 'Your are successfully signed out')
	return redirect('accounts:login')	


def signup(request):

	data = {}
	form = SignUpForm(request.POST)

	if form.is_valid():
		first_name = form.cleaned_data.get("first_name")
		last_name = form.cleaned_data.get("last_name")
		email = form.cleaned_data.get("email")
		password1 = form.cleaned_data.get("password1")

		user_obj = User.objects.create(
		username=email,
		first_name = first_name,
		last_name = last_name,
		email = email
		) 
		user_obj.save()
		user_obj.set_password(password1)
		user_obj.save()

		user = authenticate(username=user_obj.username, password=password1)
		dj_login(request, user)

		data["status"] = 1
		data["message"] = "Registration successfully done."
		data["redirect"] = reverse("posts:dashboard")

	else:
		data["status"] = -1
		data["errors"] = form.errors
		data["message"] = "Some errors occured"

	return JsonResponse(data)