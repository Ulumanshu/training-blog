from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    public = models.BooleanField(default=False, verbose_name="Should post be public?")
    chart_type = models.CharField(max_length=30, default='piechart', verbose_name="Chart Type")
    title = models.CharField(max_length=35)
    text = models.TextField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    date_from = models.DateTimeField(default=timezone.now, verbose_name="Show From")
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs ={'pk': self.pk})   


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)    
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text         