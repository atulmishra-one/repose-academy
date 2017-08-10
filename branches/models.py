from django.db import models

# Create your models here.


class Branches(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=15, default=None)
    alternate_contact = models.CharField(max_length=15, default=None)
    email = models.EmailField(default=None)
    active = models.BooleanField()
    is_main_branch = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
