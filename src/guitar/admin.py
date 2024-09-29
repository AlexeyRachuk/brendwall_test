from django.contrib import admin

from guitar.models.guitar import Guitar


@admin.register(Guitar)
class GuitarAdmin(admin.ModelAdmin):
    """
    Модель для админки
    """
    pass
