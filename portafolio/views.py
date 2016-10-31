from django.http        import HttpResponse
from django.template    import RequestContext
from django.shortcuts   import render_to_response
from portafolio.models  import Job, Course, Project
from random             import shuffle

def decode(name_url):
	return name_url.replace('_', ' ')

def encode(name):
	return name.replace(' ','_')

'''
@brief: This view return the index page, it has a image gallery of jobs which is random and max = 6 jobs to be shown
'''
def index(request):
	context      = RequestContext(request)
	jobs_list    = list(Job.objects.order_by('end_date'))[::-1] # most recent first
	courses_list = list(Course.objects.order_by('end_date'))[::-1] # most recent first
	projects     = list(Project.objects.all())
	context_dict = {'jobs_list' : jobs_list, 'courses' : courses_list, 'projects' : projects}
	return render_to_response('portafolio/index.html', context_dict, context)

def courses(request):
	context      = RequestContext(request)
	courses_list = list(Course.objects.order_by('end_date'))[::-1] # most recent first
	context_dict = {'courses' : courses_list}
	return render_to_response('portafolio/courses.html', context_dict, context)

def jobs(request):
	context      = RequestContext(request)
	jobs_list    = list(Job.objects.order_by('end_date'))[::-1] # most recent first
	context_dict = {'jobs_list' : jobs_list}
	return render_to_response('portafolio/jobs.html', context_dict, context)

def roadmap(request):
	return render_to_response('portafolio/roadmap.html')

def projects(request):
	context = RequestContext(request)
	projects = list(Project.objects.all())
	shuffle(projects)
	context_dict = {'projects' : projects}
	return render_to_response('portafolio/projects.html', context_dict, context)




