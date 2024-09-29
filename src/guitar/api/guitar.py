from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import generics
from rest_framework import status as st

from config.schema import StatusAndMessageSerializer

from guitar.models.guitar import Guitar
from guitar.serializers.guitar import GuitarSerializer

EXAMPLE_GUITAR = {
    "name": "Gibson",
    "text": "Les Paul",
    "price": 154000.00
}


@extend_schema(
    tags=["Guitar"],
    summary="Добавление новой гитары",
    description="Добавление новой гитары",
    examples=[
        OpenApiExample(
            "Пример",
            description="Пример",
            value=EXAMPLE_GUITAR,
            request_only=True,
        ),
    ],
    responses={
        st.HTTP_201_CREATED: StatusAndMessageSerializer,
        st.HTTP_400_BAD_REQUEST: StatusAndMessageSerializer,
    },
)
class GuitarCreateView(generics.CreateAPIView):
    queryset = Guitar.objects.all()
    serializer_class = GuitarSerializer


@extend_schema(
    tags=["Guitar"],
    summary="Список всех гитар",
    description="Список всех гитар",
)
class GuitarListView(generics.ListAPIView):
    queryset = Guitar.objects.all()
    serializer_class = GuitarSerializer
