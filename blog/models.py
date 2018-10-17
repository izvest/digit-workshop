from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class BlogPostQuerySet(models.QuerySet):
    
    def public(self):
        return self.fliter(date__lte=timezone.now())

class BlogPost(models.Model):
    title = models.CharField(
        max_length=160,
        blank=False,
        null=False)
    date = models.DateField(
        blank=False,
        null=False)
    content = models.TextField(
        blank=False)

    objects = BlogPostQuerySet.as_manager()

    class Meta:
        ordering = ['-date', 'title']

    def __str__(self):
        return self.title

    @property
    def detail_url(self):
        return reverse('blog-detail', kwargs={'post_id':self.pk})