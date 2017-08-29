from django.db import models

# Create your models here.


class Cms(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = 'Cms'

