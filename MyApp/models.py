from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    brand = models.CharField(max_length=100, verbose_name='Бренд')
    count = models.PositiveIntegerField(verbose_name='Количество')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.name} ({self.brand})"