from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import To_do
from webapp.views.base import index_view


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'to_do_create.html')
    if request.POST.get('status') == 'new':
        status = "new"
    elif request.POST.get('status') == 'in_progress':
        status = "in_progress"
    else:
        status = "finished"

    to_do_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'text': request.POST.get('text'),
        'status': status,
        'execution_date': request.POST.get('execution_date'),
        'created_at': request.POST.get('created_at')
    }
    to_do = To_do.objects.create(**to_do_data)
    return redirect('to_do_detail', pk=to_do.pk)

def update_view(request: WSGIRequest, pk):
    to_do = get_object_or_404(To_do, pk=pk)
    if request.method == "GET":
        return render(request, 'to_do_update.html', context={'to_do': to_do})
    to_do.title = request.POST.get('title')
    to_do.description = request.POST.get('description')
    to_do.text = request.POST.get('text')
    to_do.status = request.POST.get('status')
    to_do.execution_date = request.POST.get('execution_date')
    to_do.save()
    return redirect('to_do_detail', pk=to_do.pk)

def detail_view(request, pk):
    to_do = get_object_or_404(To_do, pk=pk)
    return render(request, 'to_do.html', context={
        'to_do': to_do
    })

def delete_task(request, pk):
    to_do = get_object_or_404(To_do, pk=pk)
    to_do.delete()
    return redirect('index')
