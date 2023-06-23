from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from knuCCiIT import settings
from main.models import Kabinet, NamKabinet, Category, Edizm, Campus

SOSTOYANIE = (
    ('рабочий', 'рабочий'),
    ('не рабочий', 'не рабочий')
)


class NalichiTehniki(models.Model):
    Campus = models.ForeignKey(Campus, verbose_name="Корпус", on_delete=models.CASCADE, related_name='txst_key',
                                null=True, blank=True)
    kabinet = ChainedForeignKey(Kabinet,
                                chained_field="Campus",
                                chained_model_field="campus",
                                show_all=False,
                                auto_choose=True,
                                sort=True,
                                verbose_name="Кабинет",
                                on_delete=models.CASCADE,
                                null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, related_name='text_key')
    Edizm = models.ForeignKey(Edizm, verbose_name="ЕдИзм", on_delete=models.CASCADE, related_name='test_key')
    kodTMU = models.CharField(max_length=200, verbose_name="КодТМУ")
    Naimenovanie = models.CharField(max_length=255, verbose_name="Наименования", null=True)
    count = models.IntegerField(verbose_name="Количество", default=0)
    sostoyanie = models.CharField(choices=SOSTOYANIE, verbose_name='Состояние', max_length=20, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Наличие техники"
        verbose_name_plural = "Наличие техники"

    def __str__(self):
        return "Наличие техники"


