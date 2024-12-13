from django.contrib import admin

from .models import Property

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    model = Property
    list_display = ("name", "propertyType", "available",)


admin.site.register(Property, PropertyAdmin)
