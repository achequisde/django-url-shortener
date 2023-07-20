from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse

from api.models import Link

def index(request):
    return render(request, 'page/index.html')

def result(request):
    if not 'url' in request.POST:
        return HttpResponseBadRequest("There's no POST data.", status=400)

    l = Link.objects.filter(url=request.POST['url'])

    if not l.exists():
        l = Link.objects.create(url=request.POST['url'])
        l.save()
    else:
        l = l[0]

    return HttpResponseRedirect(reverse("page:result_with_id", args=(l.id,)))

def result_with_id(request, link_id):
    new_url = "localhost:8000/" + link_id

    return render(request, 'page/index.html', { 'url': new_url })

def detail(request, link_id):
    l = get_object_or_404(Link, pk=link_id)
    l.clicked = F("clicked") + 1
    l.save()
    
    return render(request, 'page/detail.html', { 'redirect_url': l.url })