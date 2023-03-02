from django.contrib import admin

from web.models import VeichleDetails


class VeichleDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'veichle_type', 'model', 'description')
    search_fields = ('id', 'number')

admin.site.register(VeichleDetails, VeichleDetailsAdmin)
