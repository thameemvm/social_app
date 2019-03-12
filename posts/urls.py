from django.conf.urls import url 

from . import views

urlpatterns = [

		url(r'^$', views.dashboard, name="dashboard"),
		url(r'^create-post/$', views.create_post, name="create_post"),
		url(r'^block-user/$', views.block_user, name="block_user"),
		
		url(r'^blocked-user-alert/$', views.blocked_user_alert, name="blocked_user_alert"),
]