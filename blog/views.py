from django.shortcuts import render, render_to_response
from django.template import RequestContext
from blog.models import Quote
from random import shuffle, randint

def index(request):
	context = RequestContext(request)
	quote = Quote.objects.get(pk=randint(1,Quote.objects.count()))
	context_dict = {'quote': quote}
	return render_to_response('blog/index.html', context_dict, context)
