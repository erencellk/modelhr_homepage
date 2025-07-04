from django.db import models

class InfoBox(models.Model):
    icon = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.title

class RecruitmentStep(models.Model):
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=7 , default="#1f4e79")
    icon = models.CharField(max_length=50 , blank=True)

    def __str__(self):
        return f"{self.step_number:02d} - {self.title}"

    class Meta:
        ordering = ['step_number']