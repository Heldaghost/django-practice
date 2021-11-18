from django import template
from django.db.models import Count, F

from news.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return categories
