# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from generic.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):

	template = "base.html"
	context = {}

	return render(request, template, context)