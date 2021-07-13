from django.http.response import HttpResponseRedirect
from likeapp.models import LikeRecord
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import RedirectView
from articleapp.models import Article


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    context_object_name = 'target_like'
    template_name = 'likeapp/like.html'

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        if LikeRecord.objects.filter(user=user, article=article).exists():
            LikeRecord.objects.filter(user=user, article=article).delete()
            article.like -= 1
            article.save()

            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            LikeRecord(user=user, article=article).save()

        article.like += 1
        article.save()

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)
