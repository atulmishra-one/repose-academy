from django.db import models

# Create your models here.


class Cms(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = 'Cms'


class News(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateField()
    description = models.TextField(default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'


class SelectedStudent(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True)
    details = models.TextField()

    def __str__(self):
        return self.name


class StudentTestimonial(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name



