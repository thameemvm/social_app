from django.urls import re_path as url 

from . import views

app_name = 'posts' 


urlpatterns = [

		url(r'^$', views.dashboard, name="dashboard"),
		url(r'^create-post/$', views.create_post, name="create_post"),
		url(r'^block-user/$', views.block_user, name="block_user"),
		
		url(r'^blocked-user-alert/$', views.blocked_user_alert, name="blocked_user_alert"),
]