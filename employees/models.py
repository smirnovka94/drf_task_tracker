from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Employee(models.Model):
    """
    Модель сотрудников.
    """
    first_name = models.CharField(max_length=20, verbose_name='имя')
    second_name = models.CharField(max_length=20, verbose_name='фамилия')
    patronymic_name = models.CharField(max_length=20, verbose_name='отчество', **NULLABLE)
    position = models.CharField(max_length=20, verbose_name='должность')

    def __str__(self):
        return f'{self.first_name} {self.first_name}: {self.position}'

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
