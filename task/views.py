from django.shortcuts import render
from .models import TodoTask
from .forms import TaskCreateForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, redirect


def show_task(request):
    query = TodoTask.objects.all().order_by('created')

    # createform part
    form = TaskCreateForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Task is added successfuly")
        return HttpResponseRedirect('/')
    else:
        form = TaskCreateForm()

    dic = {
        'query': query,
        'form': form,
    }

    return render(request, 'task/index.html', dic)


class TaskDetail(DetailView):
    model = TodoTask
    template_name = 'task/detail.html'


def delete_task(request, id):
    task = get_object_or_404(TodoTask, id=id)
    task.delete()
    return redirect('show_task')
