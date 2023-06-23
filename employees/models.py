from django.db import models

class Employee(models.Model):
    Full_name = models.CharField(verbose_name="ФИО", max_length=100, null=True, blank=True)
    birthdate = models.DateField(verbose_name="День рождения" , null=True, blank=True)

