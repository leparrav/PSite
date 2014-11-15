from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Quote, Post
from blog.forms import CommentForm
from random import shuffle, randint
from django.db.models import Q

def get_search_list(max_results=10, query=''):
    post_list = []
    if query:
            post_list = Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).order_by('-date')
    else:
            post_list = None

    if post_list > 0:
            if len(post_list) > max_results:
                    post_list = post_list[:max_results]

    return post_list


def index(request, post_page):
	context = RequestContext(request)
	post_page = int(post_page) if int(post_page) >= 1 else 1
	quote = Quote.objects.get(pk=randint(1,Quote.objects.count()))
	post_len = Post.objects.count()
	posts_per_page = 5

	lower_bound = posts_per_page*(post_page-1) 
	upper_bound = posts_per_page*(1+(post_page-1))

	# Get post if any
	if upper_bound > post_len and lower_bound > post_len: # No more post to show, fix image when this happen
		post_list = None
	elif lower_bound < post_len and upper_bound > post_len: # Last posts...
		post_list = Post.objects.order_by('-date')[lower_bound:]
	else:	
		post_list = Post.objects.order_by('-date')[lower_bound:upper_bound]

	# Control pagers, next and previous
	lower_bound = posts_per_page*(post_page) 
	upper_bound = posts_per_page*(1+(post_page))
	# Next
	if upper_bound >= post_len and lower_bound >= post_len: # No more post to show, fix image when this happen
		next_present = False
	else:	
		next_present = True
	# Previous
	lower_bound = posts_per_page*(post_page-1) 
	upper_bound = posts_per_page*(1+(post_page-1))
	if post_page <= 1:
		previous_present = False
	elif upper_bound >= post_len and lower_bound >= post_len:
		previous_present = False
	else:
		previous_present = True

	context_dict = {'quote': quote, 
					'post_list': post_list, 
					'next': post_page +1,
					'next_present': next_present,
					'previous_present': previous_present,
					'previous': post_page-1}
	return render_to_response('blog/index.html', context_dict, context)

def post(request, post_pk):
	context = RequestContext(request)
	post_pk = int(post_pk)
	post = get_object_or_404(Post, pk=post_pk)
	post_count = Post.objects.count()
	quote = Quote.objects.get(pk=randint(1,Quote.objects.count()))
	next_present = True
	previous_present = True

	# Control for Next and Previous Button Appearance
	if post_pk <= 1:
		next_present = False
	if post_pk >= post_count:
		previous_present = False

	context_dict = {'post': post, 
					'quote': quote, 
					'next': post_pk-1, 
					'next_present': next_present,
					'previous': post_pk+1,
					'previous_present': previous_present}
	return render_to_response('blog/post.html', context_dict, context)

def search(request):
	context = RequestContext(request)
	post = get_object_or_404(Post, pk=randint(1,Post.objects.count()))
	quote = Quote.objects.get(pk=randint(1,Quote.objects.count()))
	context_dict = {'post': post, 
					'quote': quote }
	return render_to_response('blog/search.html', context_dict, context)

def search_suggest(request):
	context = RequestContext(request)
	posts = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	posts = get_search_list(8, starts_with)
	return render_to_response('blog/search_list.html', {'posts': posts }, context)