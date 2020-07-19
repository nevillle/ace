from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Company(models.Model):

    company_name = models.CharField(max_length=255)
    gst_no = models.CharField(max_length=255,validators=[
            RegexValidator(
                regex=r'^([0-9]{2})([a-zA-Z]{7})([0-9]{3})$',
                message='Gst no does not match',
            ),
        ])

    def __str__(self):
        return self.company_name
