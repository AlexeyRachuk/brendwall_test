from rest_framework import serializers

from guitar.models.guitar import Guitar


class GuitarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guitar
        fields = ['name', 'text', 'price']
