import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.db import models
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tags
from .models import Valores


def index(request):
    tags = Tags.objects.order_by("tipo").all()
    datos = {"tags": tags, "ejemplo": datetime.datetime.now()}
    return render(request, "scada/index.html", datos)


@permission_required("scada.view_tags")
def prueba(request):
    tag = Tags.objects.get(id=1)
    valores = Valores.objects.filter(tag=tag)
    datos = {"uno": 111, "dos": 2222, "valores": valores}
    return render(request, "scada/kk.html", datos)


def info(request):
    print(request.path_info)
    print(request.method)
    print(request.GET)
    return HttpResponse("Mira en el terminal de Django")


@login_required()
def detalle_tag(request, pk):
    tag = get_object_or_404(Tags, pk=pk)
    return render(request, "scada/detalle_tag.html", {"tag": tag})


def seno(request):
    import math

    if "api_key" in request.GET:
        api_key = request.GET["api_key"]
        if api_key != "ari":
            return HttpResponseForbidden("Sin autorización")
    else:
        return HttpResponseBadRequest("Error")

    fecha = datetime.datetime.now()
    x = int(fecha.strftime("%s"))
    valor = math.sin(x) * 100
    datos = {"valor": valor, "fecha": fecha}
    return JsonResponse(datos)


def descargar(request):
    import os
    from django.conf import settings

    filename = os.path.join(
        settings.BASE_DIR, "scada", "static", "imagenes/logosantiagoapostol.gif"
    )
    response = FileResponse(open(filename, "rb"))
    return response


def tabla(request):
    tag_id = request.GET.get("tag", None)
    if tag_id:
        valores = Valores.objects.filter(tag_id=tag_id).all()
        tag_id = int(tag_id)
    else:
        valores = Valores.objects.all()

    tags = Tags.objects.all().order_by("nombre")

    datos = {"valores": valores, "tags": tags, "tag_id": tag_id}
    return render(request, "scada/tabla.html", datos)


def grafica(request):
    tags = Tags.objects.all().values("id", "nombre")
    datos = {"tags": tags}
    return render(request, "scada/grafica.html", datos)


@csrf_exempt
def datos_grafica(request):
    print(request.POST)

    inicio = request.POST.get("desde")
    fin = request.POST.get("hasta")
    valores = Valores.objects
    if inicio:
        valores = valores.filter(fecha__gte=inicio)
    if fin:
        valores = valores.filter(fecha__lt=fin)

    tag_id = request.POST.get("tag")
    if tag_id:
        tag_id = int(tag_id)
        valores = valores.filter(tag_id=tag_id)

    datos = {}
    valores = valores.all()
    for valor in valores:
        datos[valor.fecha.strftime("%Y-%m-%dT%H:%M:%S.%fZ")] = valor.valor
    return JsonResponse({"datos": datos})


    # Forma más elegante:
    # filtros = {}
    # if inicio:
    #     filtros["fecha__gte"] = inicio
    # if fin:
    #     filtros["fecha__lt"] = fin
    # if tag_id:
    #     filtros["tag_id"] = int(tag_id)

    # import json

    # valores = Valores.objects.filter(**filtros).all()
    # valores_json = serializers.serialize("json", valores)
    # datos = {
    #     k["fields"]["fecha"]: k["fields"]["valor"] for k in json.loads(valores_json)
    # }
    # return JsonResponse({"datos": datos})
