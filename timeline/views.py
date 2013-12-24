from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from timeline.forms import TimeLineForm
from timeline.models import TimeLine
# Create your views here.

def index(request):
    context = RequestContext(request)
    return render_to_response('timeline/index.html', {}, context)


def list(request, timeLineId):
    timeline = TimeLine.objects.get(id=timeLineId)
    context = RequestContext(request)

    return render_to_response('timeline/list.html', {'timeline':timeline}, context)


def create(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = TimeLineForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=True)
            url = reverse('list', kwargs={'timeLineId' : instance.id})
            return HttpResponseRedirect(url)
        else:
            print form.errors
    else:
        form = TimeLineForm()

    return render_to_response('timeline/create.html', {'form':form}, context)

def addEvent(request, timeLineId):
    #context = RequestContext(request)
    return HttpResponse("11111111111111111111")



