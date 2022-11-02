from django.db import models

class ToDo(models.Model):
  title = models.CharField(max_length=25)
  completed = models.BooleanField(default=False, null=True)