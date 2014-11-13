from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Quote, Post
from blog.forms import CommentForm
from random import shuffle, randint


def index(request, post_page):
	context = RequestContext(request)
	post_page = int(post_page)
	quote = Quote.objects.get(pk=randint(1,Quote.objects.count()))
	post_len = Post.objects.count()

	# Simple low value
	if post_page == 1:
		lower_bound = 0
	else:
		lower_bound = 1*post_page 
	upper_bound = 5*post_page

	if upper_bound >= post_len and lower_bound >= post_len: # I'm losing some post here, fix later
		no_more = True
		post_list = Post.objects.order_by('-date')[:5]
	elif lower_bound <= post_len: # Last posts...
		post_list = Post.objects.order_by('-date')[lower_bound:]
		no_more = False
	else:	
		post_list = Post.objects.order_by('-date')[lower_bound:upper_bound]
		no_more = False

	context_dict = {'quote': quote, 
					'post_list': post_list, 
					'next': post_page +1,
					'no_more': no_more}
	return render_to_response('blog/index.html', context_dict, context)

def post(request, post_pk):
	context = RequestContext(request)
	post = get_object_or_404(Post, pk=post_pk)
	quote = Quote.objects.get(pk=randint(1,Quote.objects.count()))
	context_dict = {'post': post, 'quote': quote}
	return render_to_response('blog/post.html', context_dict, context)