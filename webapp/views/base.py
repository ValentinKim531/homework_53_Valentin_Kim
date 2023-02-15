from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import To_do


def index_view(request: WSGIRequest):
    tasks = To_do.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)

