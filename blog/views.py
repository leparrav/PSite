from django.shortcuts import render, render_to_response
from django.template import RequestContext
from blog.models import Quote
from random import shuffle

def index(request):
	context = RequestContext(request)
	quotes = list(Quote.objects.all())
	shuffle(quotes)
	context_dict = {'quote': quotes[0]}
	return render_to_response('blog/index.html', context_dict, context)
