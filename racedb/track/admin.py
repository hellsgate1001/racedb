from django.contrib import admin
from django.utils.html import format_html

from .models import Track


class Trackadmin(admin.ModelAdmin):
    list_display = ['name', 'download_as_link',]

    def download_as_link(self, obj):
        return format_html('<a href="{download}" target="dl_track">{download}</a>', download=obj.download)

admin.site.register(Track, Trackadmin)
