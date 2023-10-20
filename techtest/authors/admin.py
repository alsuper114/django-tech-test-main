# Register your models here.
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin

from .models import Author

# Register your models here.
@register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]
