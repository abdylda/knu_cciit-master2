from django.core.exceptions import ValidationError
from django.db import models

from main.models import Category, Edizm, Faculty, Kabinet, NamKabinet, Campus


class Network(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE,
                                 related_name='model_key')
    Edizm = models.ForeignKey(Edizm, verbose_name="ЕдИзм", on_delete=models.CASCADE,
                              related_name='model_key')
    count = models.IntegerField(verbose_name="Количество", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'


class Transfernetwork(models.Model):
    campus = models.ForeignKey(Campus, verbose_name="Корпус", on_delete=models.CASCADE, related_name='txst_key1', null=True, blank=True)
    network = models.ForeignKey(Network, verbose_name="Наименование материала", on_delete=models.CASCADE,
                                related_name='test_key')
    faculty = models.ForeignKey(Faculty, verbose_name="Подразделение", on_delete=models.CASCADE,
                                related_name='test_key', null=True, blank=True)
    kabinet = models.ForeignKey(Kabinet, verbose_name="Кабинет", on_delete=models.CASCADE, related_name='test_key',
                                null=True, blank=True)
    namKabinet = models.ForeignKey(NamKabinet, verbose_name="Название кабинета", on_delete=models.CASCADE,
                                   related_name='test_key', null=True, blank=True)
    count = models.IntegerField(verbose_name="Количество", default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    Report = models.ForeignKey('Report', verbose_name="Рапорт", on_delete=models.CASCADE,
                              related_name='test_key', null=True, blank=True)

    class Meta:
        verbose_name = 'Добавить материал'
        verbose_name_plural = 'Добавить материал'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.network.count = self.network.count - self.count
        self.network.save()
        super(Transfernetwork, self).save()


class Report(models.Model):
    reportitle = models.CharField(verbose_name="Рапорт на подразделение", max_length=255, null=True, blank=True)
    document = models.FileField(verbose_name="Рапорт", upload_to='document/', max_length=250, null=True, blank=True)
    is_done = models.BooleanField(default=False, verbose_name='Сделано')
    no_report = models.BooleanField(default=False, verbose_name='Без рапорт')

    class Meta:
        verbose_name = 'Списание по рапорту'
        verbose_name_plural = 'Списание по рапорту'
