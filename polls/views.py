from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Context,loader
from polls.models import Poll

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = Context({
		'latest_poll_list':latest_poll_list,
	})
	return HttpResponse(template.render(context))

def detail(request,poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	#return HttpResponse("You're look at poll %s." % poll_id)
	return render(request,'polls/detail.html',{'poll':poll})

def results(request,poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request,poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)