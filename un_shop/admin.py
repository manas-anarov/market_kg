from django.contrib import admin

from .models import OrderItem


class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'timestamp', 'first_name', 'last_name', 'telephone', 'whatsapp', 'address', 'on_way', 'stopped', 'ordered' ]
	search_fields = ['first_name', 'last_name', 'telephone', 'whatsapp', 'address']
	list_editable = ['on_way', 'ordered', 'stopped']
	list_filter = ['on_way', 'ordered', 'stopped']



admin.site.register(OrderItem, OrderAdmin)