from django import template
from django.db.models import Count, F

from photo_hosting.models import *

register = template.Library()


@register.simple_tag()
def is_liked_by_this_user(post: Posts, user: User):
    return set(post.likes_set.all()) & set(user.userprofile.likes_set.all())
