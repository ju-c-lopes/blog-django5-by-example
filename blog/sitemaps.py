from django.contrib.sitemaps import Sitemap
from taggit.models import Tag
from django.urls import reverse

from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated


class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        # Retorna todas as tags que estão sendo usadas
        return Tag.objects.all()

    def location(self, obj):
        # Retorna a URL para a lista de postagens filtradas por uma tag específica
        return reverse('blog:post_list_by_tag', args=[obj.slug])
