from django.db import models

class someModel(models.Model):
    name = models.CharField(max_length=127)