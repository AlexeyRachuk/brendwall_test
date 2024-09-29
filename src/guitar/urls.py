from django.urls import path
from guitar.api.guitar import GuitarCreateView, GuitarListView
from guitar.views import index

urlpatterns = [
    path('api/guitars/create/', GuitarCreateView.as_view(), name='guitar-create'),
    path('api/guitars/', GuitarListView.as_view(), name='guitar-list'),
    path('', index, name='index')
]
