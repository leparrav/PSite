from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Quote, Post
from blog.forms import CommentForm
from random import shuffle, randint


def index(request):
	context = RequestContext(request)
	quote = Quote.objects.get(pk=randint(1,Quote.objects.count()))
	post_list = Post.objects.order_by('-date')[:5]
	context_dict = {'quote': quote, 'post_list': post_list}
	return render_to_response('blog/index.html', context_dict, context)

def post(request, post_pk):
	context = RequestContext(request)
	post = get_object_or_404(Post, pk=post_pk)
	quote = Quote.objects.get(pk=randint(1,Quote.objects.count()))
	print request.method
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
		else:
			print form.errors
	else:
		form = CommentForm()

	context_dict = {'post': post, 'quote': quote, 'form':form }
	return render_to_response('blog/post.html', context_dict, context)