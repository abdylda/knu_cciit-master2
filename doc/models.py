from django.db import models

# Create your models here.

class Documentation(models.Model):
    name = models.CharField(verbose_name="Название документ", max_length=100, null=True, blank=True)
    document = models.FileField(verbose_name="Документы", upload_to='document/', max_length=250, null=True, blank=True)


    class Meta:
        verbose_name = 'документы'
        verbose_name_plural = 'документы'
