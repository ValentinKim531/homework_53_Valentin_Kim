from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.models import To_do
from webapp.views.base import index_view


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'to_do_create.html')
    print(request.POST)
    if request.POST.get('status') == 'new':
        status = "new"
    elif request.POST.get('status') == 'in_progress':
        status = "in_progress"
    else:
        status = "finished"

    to_do_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'status': status,
        'execution_date': request.POST.get('execution_date'),
        'created_at': request.POST.get('created_at')
    }
    to_do = To_do.objects.create(**to_do_data)
    return redirect("/", f'/to_do/?pk={to_do.pk}')

def detail_view(request):
    to_do_pk = request.GET.get('pk')
    to_do = To_do.objects.get(pk=to_do_pk)
    context = {'to_do': to_do}
    return render(request, 'to_do.html', context=context)

def delete_task(request):
    to_do_pk = request.GET.get('pk')
    to_do = To_do.objects.get(pk=to_do_pk)
    to_do.delete()
    return redirect(index_view)