from django.shortcuts import render
from django.http import HttpResponse
from .models import Teammate

def index(request):
    names = []
    for m in Teammate.objects.all().iterator():
        name = f"{m.id}. {m.title} {m.first_name} {m.last_name}"
        names.append(name)
    return HttpResponse("<br>".join(names))
