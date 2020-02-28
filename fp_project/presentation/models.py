from django.db import models

# Create your models here.

class Slide(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="The id the div will be given.")
    title = models.CharField(max_length=200, help_text="The title your slide will be given.")
    content = models.CharField(max_length=2000, help_text="The general content of your slide.")
    notes = models.CharField(max_length=2000, default="None", help_text="The hiddens notes for the slide.")
    display = models.BooleanField(default=True, help_text="If unchecked the slide will not be displayed.")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Slide"