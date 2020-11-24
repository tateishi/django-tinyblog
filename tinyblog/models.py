from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    entry = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
