from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=10)
    course = models.CharField(max_length=255)
    message = models.TextField()
    date_received = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Enquiry / Contact us'
        verbose_name_plural = 'Enquiry / Contact us'

