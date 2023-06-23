
from django.db import models
from main.models import Faculty


class Application(models.Model):
    name = models.CharField(verbose_name="Название заявка", max_length=100, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, verbose_name="Подразделение", on_delete=models.CASCADE,
                                related_name='faculty_key1')
    document = models.FileField(verbose_name="Документы", upload_to='document/', max_length=250, null=True, blank=True)
    accepted_application = models.BooleanField(default=False, verbose_name='Принял заявка')
    no_report = models.BooleanField(default=False, verbose_name='Без рапорт')


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявка'


class Tender(models.Model):
    name = models.CharField(verbose_name="Название заявка", max_length=100, null=True, blank=True)
    document = models.FileField(verbose_name="Документы", upload_to='document/', max_length=250, null=True, blank=True)
    purchase_order_is_ready = models.BooleanField(default=False, verbose_name='Заявка на закупку готова')
    in_stock = models.BooleanField(default=False, verbose_name='На складе')


    class Meta:
        verbose_name = 'Заявка на тендер'
        verbose_name_plural = 'Заявка на тендер'