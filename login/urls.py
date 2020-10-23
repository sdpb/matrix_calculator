from django.urls import path
from calculator.views import get_matrix_dimensions

urlpatterns = [
    path('', get_matrix_dimensions, name='home')
]

