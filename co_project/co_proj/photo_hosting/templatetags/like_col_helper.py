from django import template
from django.db.models import Count, F, QuerySet

from photo_hosting.models import *

register = template.Library()


@register.simple_tag()
def is_col_liked_by_this_user(col: Collections, user: User, likes):
    for item in likes:
        if col.pk == item.col_id and user.pk == item.user_id:
            return True
    return False
