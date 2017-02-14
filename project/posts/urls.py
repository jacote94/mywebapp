from django.conf.urls import url, include
from posts import views
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.PostListView.as_view(), name='list_posts'),



	] 