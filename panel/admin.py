from csv import list_dialects
from django.contrib import admin

from .models import Subsidiary, Station

class StationAdmin(admin.ModelAdmin):
    list_display = ('title', 'subsidiary')


admin.site.register(Subsidiary)
admin.site.register(Station, StationAdmin)

