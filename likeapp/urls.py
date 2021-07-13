from likeapp.views import LikeArticleView
from django.urls import path

app_name = 'likeapp'

urlpatterns = [
    path('article/like/<int:pk>', LikeArticleView.as_view(), name='article_like'),
]
