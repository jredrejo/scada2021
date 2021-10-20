import random
import serial
import time

from django.core.management.base import BaseCommand, CommandError
from scada.models import Tags
from scada.models import Valores


class Command(BaseCommand):
    help = 'Va a conectar con Arduino'

    def handle(self, *args, **options):
        # aquí creo una conexión con arduion con pyserial

        # después, en un bucle infinito, cada 5 segundos
        # recorre todas las tags , lee sus valores y los guarda:
        while True:
            tags = Tags.objects.all()
            for tag in tags:
                # conecta con arduino, obtiene el dato del valor
                # de tag.dirección y lo guarda en la variable dato
                dato = random.randint(0, 100)  # en este caso es un valor aleatorio, no el de Arduino
                nuevo_valor = Valores(valor=dato, tag=tag)
                nuevo_valor.save()

            time.sleep(5)  # espera 5 sg para volver a leer los valores desde Arduino