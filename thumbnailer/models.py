from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=250)
    title_en = models.CharField(max_length=250)
    title_ru = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

