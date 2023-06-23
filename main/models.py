from django.db import models

from django.contrib.auth.models import AbstractUser


class UserRole(models.Model):

    campus = models.ManyToManyField('Campus', verbose_name="Корпус", related_name='user_role_campus_key')
    title = models.CharField("Роль", max_length=100)
    description = models.TextField("Описания", null=True, blank=True)

    def __str__(self):
        return self.title + ' ' + self.description

    class Meta:
        verbose_name = "Роль пользователя"
        verbose_name_plural = "Роль пользователя"


class User(AbstractUser):
    role = models.ForeignKey(verbose_name="Роль", to=UserRole, on_delete=models.CASCADE, related_name='users', null=True, blank=True)


    def __str__(self):
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        else:
            return self.username

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"


class Campus(models.Model):
    Naimenovanie = models.CharField("Корпус", max_length=50)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Корпус"
        verbose_name_plural = "Корпус"


class NamKabinet(models.Model):
    Naimenovanie = models.CharField("Название кабинета", max_length=100)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Название кабинета"
        verbose_name_plural = "Название кабинета"


class Kabinet(models.Model):
    Naimenovanie = models.CharField("Кабинет", max_length=50)
    NamKabinet = models.ForeignKey(NamKabinet, verbose_name="Название кабинета", on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, verbose_name="Корпус", on_delete=models.CASCADE, related_name='txst_key11',
                                null=True, blank=True)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинет"


class Faculty(models.Model):
    title = models.CharField(verbose_name="Добавить Подразделение", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделение'


class Edizm(models.Model):
    Naimenovanie = models.CharField("ЕдИзм", max_length=50)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "ЕдИзм"
        verbose_name_plural = "ЕдИзм"


class Category(models.Model):
    Naimenovanie = models.CharField("Категория", max_length=50)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Категория"
        
        verbose_name_plural = "Категория"
