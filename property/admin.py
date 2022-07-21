from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatInline(admin.TabularInline):
    raw_id_fields = ('owner',)
    model = Flat.owners.through
    extra = 1


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = (
        'address', 'price', 'is_building_new', 'construction_year', 'town', 'owner_normalized_phone',
    )
    list_editable = ('is_building_new',)
    list_filter = ('is_building_new', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by', )
    inlines = (FlatInline,)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
