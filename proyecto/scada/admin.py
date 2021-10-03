from django.contrib import admin

# Register your models here.
from .models import Tags
from .models import Valores

admin.site.register(Tags)
admin.site.register(Valores)
