from __future__ import annotations
from datetime import datetime

from django.db import models
from django.core.exceptions import ValidationError


class Division(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def parent_depth(self) -> int:
        """Returns the number of parents"""
        depth = 0
        if self.parent is not None:
            depth += 1
            model = self.parent
            while model.parent is not None:
                depth += 1
                model = model.parent
        return depth

    def clean(self):
        if self.parent_depth() > 5:
            raise ValidationError('Максимальная глубина иерархии подразделений - 5. Вы её превысили')

    def __str__(self):
        return f'{self.name}. id: {self.pk}'

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Список подразделений'


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Список должностей'


class Employee(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    employed_date = models.DateField(null=True, blank=True)
    position = models.ForeignKey(Position, null=True, on_delete=models.SET_NULL)
    division = models.ForeignKey(Division, null=True, on_delete=models.SET_NULL)
    salary = models.DecimalField(default=0, max_digits=9, decimal_places=2)

    # Adding today's date as employed date to an employee if it's not specified by admin
    def save(self, *args, **kwargs) -> None:
        if not self.employed_date:
            self.employed_date = datetime.today().strftime('%Y-%m-%d')
        super().save(*args, **kwargs)

    @classmethod
    def get_division_employees(
            cls,
            order: str | None = None,
            division_id: int | None = None
    ) -> models.QuerySet:
        """Returns all employees of certain division ordered by 'order' parameter if it's given"""
        if division_id is not None:
            to_return = cls.objects.filter(division=division_id)
            if order is not None:
                to_return.order_by(order)
            return to_return
        else:
            raise AttributeError('division_id is required for get_division_employees function')

    def __str__(self):
        return f'{self.surname} {self.name} {self.middle_name}. ' \
               f'Подразделение: {self.division.name} {self.division.id}. Должность: {self.position.name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Список сотрудников'
