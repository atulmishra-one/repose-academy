from django.db import models

from branches.models import Branches
from courses.models import Courses

# Create your models here.


class Batches(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    start_date = models.DateField()
    center = models.ForeignKey(Branches, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    active = models.BooleanField(default=True)
    show_on_home_page = models.BooleanField(default=False, help_text='This appear on home page widget')

    def __str__(self):
        return '{}'.format(self.course.name)

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'
