from django.shortcuts import redirect
from django.http import Http404


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


