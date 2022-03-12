from .models import Message
from django.contrib import admin

class MessageAdmin(admin.ModelAdmin):
    fields = ('text','created_at', 'author', 'receiver')
    list_display = ('created_at', 'author', 'text', 'receiver')
    search_fields = ('text',)

# Register your models here.
admin.site.register(Message, MessageAdmin)