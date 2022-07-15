from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'is_building_new', 'construction_year', 'town')
    list_editable = ('is_building_new',)
    list_filter = ('is_building_new', 'rooms_number', 'has_balcony')
