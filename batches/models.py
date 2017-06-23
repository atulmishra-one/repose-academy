from django.db import models

from branches.models import Branches

# Create your models here.


class Batches(models.Model):
    course = models.CharField(max_length=255)
    start_date = models.DateField()
    center = models.ForeignKey(Branches, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'
