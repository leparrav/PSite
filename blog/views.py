from django.shortcuts import render, render_to_response
from django.template import RequestContext
from blog.models import Quote, Post
from random import shuffle, randint

def index(request):
	context = RequestContext(request)
	quote = Quote.objects.get(pk=randint(1,Quote.objects.count()))
	post_list = Post.objects.order_by('-date')[:5]
	context_dict = {'quote': quote, 'post_list': post_list}
	return render_to_response('blog/index.html', context_dict, context)

def post(request):
	context = RequestContext(request)
	post = Post.objects.get(pk=1)
	quote = Quote.objects.get(pk=randint(1,Quote.objects.count()))
	context_dict = {'post': post, 'quote': quote}
	return render_to_response('blog/post.html', context_dict, context)