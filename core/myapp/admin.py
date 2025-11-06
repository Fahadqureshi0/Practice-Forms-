from django.contrib import admin
from .models import Application
# Register your models here.
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'linkedin_url', 'location', 'phone', 'email', 'Experience','uploaded_at']

