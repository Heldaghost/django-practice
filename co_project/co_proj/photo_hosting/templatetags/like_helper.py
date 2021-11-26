from django import template
from django.db.models import Count, F, QuerySet

from photo_hosting.models import *

register = template.Library()


@register.simple_tag()
def is_liked_by_this_user(post: Posts, user: User, likes):
    for item in likes:
        if post.pk == item.post_id and user.pk == item.user_id:
            return True
    return False
