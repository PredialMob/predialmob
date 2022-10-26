from django.contrib import admin

from config.models import ConfigEdificio, ConfigGeral

admin.site.register(ConfigGeral)
admin.site.register(ConfigEdificio)
