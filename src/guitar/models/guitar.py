from django.db import models
from django.core.validators import MinValueValidator


class Guitar(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=120
    )
    text = models.TextField(
        verbose_name="Описание",
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,  # Максимальное количество цифр в числе
        decimal_places=2,  # Количество знаков после запятой
        validators=[MinValueValidator(0.01)]  # Минимальное значение должно быть больше 0
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "guitar"
        verbose_name = "Гитара"
        verbose_name_plural = "Гитары"
