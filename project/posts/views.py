from django.shortcuts import render
from django.views.generic.list import ListView
from posts.models import Post


class PostListView(ListView):

	model = Post 
	

# Create your views here.
