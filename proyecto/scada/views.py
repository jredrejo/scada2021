import datetime

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.http import JsonResponse
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


def info(request):
    print(request.path_info)
    print(request.method)
    print(request.GET)
    return HttpResponse("Mira en el terminal de Django")


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
