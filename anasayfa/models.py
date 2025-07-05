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


class AboutSection(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"


class WhoWeAreSection(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama")
    image = models.ImageField(upload_to='/images', verbose_name="Görsel")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")

    class Meta:
        verbose_name = "Biz Kimiz İçeriği"
        verbose_name_plural = "Biz Kimiz İçerikleri"
        ordering = ['order']

    def __str__(self):
        return self.title

