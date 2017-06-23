from django.db import models

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
