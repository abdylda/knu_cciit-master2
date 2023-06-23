from django.core.exceptions import ValidationError
from django.db import models

from main.models import Campus, Faculty, Kabinet, NamKabinet


class Cartridge(models.Model):
    title = models.CharField(verbose_name="Название картридж", max_length=255)
    model = models.ForeignKey('Model', verbose_name="Модель картридж", on_delete=models.CASCADE,
                              related_name='model_key')
    foruseonaprinter = models.CharField(verbose_name="Для использования на принтере", max_length=255)
    count = models.IntegerField(verbose_name="Количество", default=0)

    def __str__(self):
        return self.title + '  ' + self.model.title + ' \ Остаток ' +  str(self.count) + 'шт'

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'


class Model(models.Model):
    title = models.CharField(verbose_name="Модель картридж", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модель картридж'
        verbose_name_plural = 'Модель картридж'


class TransferCartridge(models.Model):
    campus = models.ForeignKey(Campus, verbose_name="Корпус", on_delete=models.CASCADE, related_name='campus_key')
    cartridge = models.ForeignKey(Cartridge, verbose_name="Название картридж", on_delete=models.CASCADE,
                                  related_name='cartridge_key')
    faculty = models.ForeignKey(Faculty, verbose_name="Подразделение", on_delete=models.CASCADE,
                                related_name='faculty_key')
    kabinet = models.ForeignKey(Kabinet, verbose_name="Кабинет", on_delete=models.CASCADE, related_name='kabinet_key')
    namKabinet = models.ForeignKey(NamKabinet, verbose_name="Название кабинета", on_delete=models.CASCADE,
                                   related_name='namKabinet_key')
    count = models.IntegerField(verbose_name="Количество", default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.cartridge.title

    class Meta:
        verbose_name = 'Передать картридж'
        verbose_name_plural = 'Передать картридж'

    def clean(self):
        if self.count > self.cartridge.count:
            raise ValidationError("Вы указали больше катриджов чем есть!")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.cartridge.count = self.cartridge.count - self.count
        self.cartridge.save()
        super(TransferCartridge, self).save()
