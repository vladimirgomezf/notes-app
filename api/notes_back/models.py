from django.db import models


class Notes(models.Model):
    content = models.CharField('Note Text', max_length=250)
    hecho = models.BooleanField('Done', default=False)
