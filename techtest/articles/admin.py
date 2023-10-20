# Register your models here.
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin

from .models import Article

# Register your models here.
@register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ["title", "content"]
    search_fields = ["title", "content"]
