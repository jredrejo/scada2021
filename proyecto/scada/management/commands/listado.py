from django.core.management.base import BaseCommand, CommandError
from scada.models import Tags  # el modelo de mi aplicación

class Command(BaseCommand):
    help = 'Va a mostrar todas las tags"'

    def add_arguments(self, parser):
        """Aquí se ponen posibles opciones que se
        usen al ejecutar el comando.
        Esta función add_arguments no es obligatoria"""
        parser.add_argument('-t', '--tipo', type=str, default=None, required=False)

    def handle(self, *args, **options):
        # Aquí acaba la parte obligatoria de Django
        # A partir de aquí se pone el código que necesite mi aplicación en Python
        if options['tipo'] is None:
            mis_tags = Tags.objects.all()
        else:
            mis_tags = Tags.objects.filter(tipo=options['tipo'])

        for tag in mis_tags:
            print(tag.nombre, tag.tipo)