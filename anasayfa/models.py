from django.db import models

class InfoBox(models.Model):
    icon = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.title
