from django.forms import modelformset_factory
from django.shortcuts import render

from .models import Todos


def hello(request):

    template = "todos/hello.html"

    FormSet = modelformset_factory(Todos, fields=['id', 'todo'], extra=5)
    context = {'form': FormSet()}

    if request.method == 'POST':
        form = FormSet(request.POST)
        if form.is_valid():
            instances = form.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()

    return render(request, template, context=context)
