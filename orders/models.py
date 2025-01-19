from django.db import models

from core.constants import STATUS


class Dish(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название блюда')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f'{self.name} цена {self.price}'


class Order(models.Model):
    table_number = models.SmallIntegerField(verbose_name='Номер стола')
    items = models.ManyToManyField(Dish, verbose_name='Блюда')
    total_price = models.IntegerField(verbose_name='Цена')
    status = models.PositiveSmallIntegerField(
        choices=STATUS,
        verbose_name='Статус заказа',
        default=1
    )

    class Meta:
        default_related_name = 'order'
