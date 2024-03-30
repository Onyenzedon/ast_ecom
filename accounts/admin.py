from django.contrib import admin
from .models import UserAccount

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_staff']
    list_display_links = []
    list_filter = []
    search_fields = []

admin.site.register(UserAccount, UserAdmin)