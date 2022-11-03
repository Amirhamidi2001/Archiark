from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email')
    list_filter = ('email',)
    search_fields = ('name', 'message')


admin.site.register(Contact, ContactAdmin)
