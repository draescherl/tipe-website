from django.db import models

# Create your models here.

class Slide(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="A unique ID for your slide.")
    content = models.TextField(help_text="The HTML content of your slide.")
    notes = models.TextField(default="None", help_text="The hiddens notes for the slide.")
    display = models.BooleanField(default=True, help_text="If unchecked the slide will not be displayed.")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Slide"