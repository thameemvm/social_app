from django.shortcuts import redirect
from django.http import Http404
from posts.models import BlockedPost
from django.http import JsonResponse


def login_required(func):
	def wrap(request, *args, **kwargs):
		# import pdb; pdb.set_trace()
		if request.user.is_authenticated:
			return func(request, *args, **kwargs)
		else:
			response =  redirect("accounts:login")
			response['Location'] += '?next=%s'%(request.get_full_path())
			return response
		
	return wrap


def blocked_user_alert(func):
	def wrap(request, *args, **kwargs):

		current_user = request.user
		blocked_user = BlockedPost.objects.filter(
										blocked_by__isnull=True,
										blocked_whom=request.user
										)

		if request.user.is_authenticated and not blocked_user.exists():
			return func(request, *args, **kwargs)
		else:
			if request.is_ajax:
				# data = {}
				# data["refresh_page"] = -1
				# data["status"] = -1
				# return JsonResponse(data)
				return redirect("posts:blocked_user_alert")

			else:
				
				return redirect("posts:blocked_user_alert")
		
	return wrap
