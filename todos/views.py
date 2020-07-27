from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render

from .models import Todos


def hello(request):
    try:
        get_user_model().objects.get(username=str(request.user))
    except ObjectDoesNotExist:
        return redirect('login')

    return redirect('todo', str(request.user))


def todo(request, user_name):
    if str(request.user) != user_name:
        return redirect('hello')

    template = "todos/hello.html"

    user = get_user_model().objects.get(username=user_name)

    FormSet = inlineformset_factory(
        get_user_model(), Todos, fields=('todo',), extra=5)

    if request.method == 'POST':
        forms = FormSet(request.POST, instance=user)
        if forms.is_valid():
            forms.save()
        return redirect('hello', user_name=user_name)

    forms = FormSet(instance=user)
    context = {'form': forms}
    return render(request, template, context=context)
