from django.contrib import admin
from .models import Status, Favorite


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'posted_at']


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']

# Register your models here.
admin.site.register(Status, StatusAdmin)
admin.site.register(Favorite, FavoriteAdmin)
