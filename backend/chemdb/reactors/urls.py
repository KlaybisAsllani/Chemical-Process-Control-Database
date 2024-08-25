from django.urls import path
from .views import ReactorList

urlpatterns = [
    path('reactors/', ReactorList.as_view(), name='reactor-list'),
]
