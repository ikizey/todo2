from django.shortcuts import render


def hello(request):
    return render(request, "todos/hello.html")
