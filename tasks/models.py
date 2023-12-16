from django.db import models

from employees.models import Employee

NULLABLE = {'blank': True, 'null': True}


class Task(models.Model):
    """Модель задач"""
    METODS = [
        ("waiting", "в ожидании"),
        ("work", "в работе"),
        ("finished", "завершена")
    ]

    name = models.CharField(max_length=100, verbose_name='Наименование')
    related_task = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная задача', **NULLABLE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='исполнитель', **NULLABLE)
    time_limit_hours = models.IntegerField(verbose_name='срок выполнения часов')
    status = models.CharField(max_length=150, choices=METODS, default="waiting", verbose_name='статус')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
