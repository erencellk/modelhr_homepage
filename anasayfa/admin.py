from django.contrib import admin
from django.contrib.auth.models import User

from .models import InfoBox , RecruitmentStep

@admin.register(InfoBox)  #decarator
class InfoBoxAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(RecruitmentStep)
