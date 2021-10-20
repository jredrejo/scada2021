import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import Tags
from .models import Valores


def index(request):
    tags = Tags.objects.order_by("tipo").all()
    datos = {"tags": tags, "ejemplo": datetime.datetime.now()}
    return render(request, "scada/index.html", datos)


def prueba(request):
    tag = Tags.objects.get(id=1)
    valores = Valores.objects.filter(tag=tag)
    datos = {"uno": 111, "dos": 2222, "valores": valores}
    return render(request, "scada/kk.html", datos)
