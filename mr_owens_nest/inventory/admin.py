from django.contrib import admin
from .models import InventoryItems

# @admin.site.register(InventoryItems)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['item_code', 'name', 'stock', 'date_added', 'date_updated']
    readonly_fields = ['date_added', 'date_updated']
    list_display_links = ['item_code']
    search_fields = ['item_code', 'name']
    ordering = ['-date_updated']
    fieldsets = (
        ('Image Thumbnail', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('thumbnail',),
        }),
        (None, {
            'classes': ('wide', 'extrapretty',),
            'fields': ('item_code', 'name', 'slug', 'stock'),
        }),
        ('More Details', {
            'classes': ('collapse',),
            'fields': ('date_added', 'date_updated'),
        }),
    )

admin.site.register(InventoryItems, InventoryItemAdmin)