from django.db import models

# Create your models here.
class Proyecto(models.Model):
    title = models.CharField('Title', max_length=40)
    address = models.TextField()
    phone = models.TextField()

    def __str__(self):
        return self.title