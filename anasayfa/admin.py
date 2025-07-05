from django.contrib import admin
from django.contrib.auth.models import User

from .models import InfoBox, RecruitmentStep, AboutSection, WhoWeAreSection


@admin.register(InfoBox)  #decarator
class InfoBoxAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)


@admin.register(WhoWeAreSection)
class WhoWeAreSectionAdmin(admin.ModelAdmin):
    list_display = ('title','order')
    list_filter = ('order',)



admin.site.register(RecruitmentStep)

