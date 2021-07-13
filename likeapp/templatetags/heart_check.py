from likeapp.models import LikeRecord
from django import template
from django.contrib.auth.models import AnonymousUser

register = template.Library()


@register.simple_tag
def heart_check(target_article, user):
    if not user.is_authenticated or not LikeRecord.objects.filter(user=user, article=target_article).exists():
        return "favorite_border"
    else:
        return "favorite"
