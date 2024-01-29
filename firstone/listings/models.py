from django.db import models

# listings/models.py

class Band(models.Model):
    name = models.fields.CharField(max_length=100)