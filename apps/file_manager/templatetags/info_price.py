from django import template
from apps.file_manager.models import FileInfo

register = template.Library()

@register.filter
def info_price(path):
    file_info = FileInfo.objects.filter(path=path)
    if file_info.exists():
        return file_info.first().Price
    else:
        return ""

