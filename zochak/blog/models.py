from django.db import models
from django.conf import settings


class Zocbo(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
