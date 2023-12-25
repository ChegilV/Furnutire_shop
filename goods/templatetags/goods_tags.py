from django import template
from goods.models import *


register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()