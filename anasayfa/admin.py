from django.contrib import admin
from .models import InfoBox

@admin.register(InfoBox)  #decarator
class InfoBoxAdmin(admin.ModelAdmin):
    list_display = ('title',)
