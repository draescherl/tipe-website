from django.db import models

# Create your models here.

class Slide(models.Model):
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    notes = models.CharField(max_length=2000, default="None")
    display = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Slide"