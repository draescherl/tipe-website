from django.contrib import admin

from .models import Slide

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    search_fields = ['name']