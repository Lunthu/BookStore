from django.db import models


class Users(models.Model):

    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name

# Create your models here.
