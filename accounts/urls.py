from django.urls import re_path as url 

from . import views


app_name = 'accounts' 

urlpatterns = [

	url(r'^login/$', views.login, name="login"),
	url(r'^logout/$', views.logout, name="logout"),
	url(r'^signup/$', views.signup, name="signup"),
]