from django.db import models

# Create your models here.


class Notes(models.Model):
    content = models.CharField('Note Text', max_length=250)
    check = models.BooleanField('Done', default=False)
