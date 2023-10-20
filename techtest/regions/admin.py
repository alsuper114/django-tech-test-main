# Register your models here.
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin

from .models import Region

# Register your models here.
@register(Region)
class RegionAdmin(ModelAdmin):
    list_display = ["code", "name"]
    search_fields = ["code", "name"]
