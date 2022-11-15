from django.contrib import admin
from .models import User

# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'date_joined']
    readonly_fields = ['date_joined']
    list_display_links = ['username']
    search_fields = ['first_name', 'last_name', 'email', 'username']
    ordering = ['-date_joined']
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name',)
        }),
        ('Login Details', {
            'fields': ('email', 'username', 'date_joined')
        }),
    )

admin.site.register(User, UserAdmin)
