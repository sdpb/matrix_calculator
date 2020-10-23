from django.urls import path

from . import views

urlpatterns = [
    path('dimensions/<n_rows>/<m_columns>/',
         views.enter_matrix_numbers, name='matrix_dimensions'),
    path('calculated/', views.calculate, name='calculated_matrix'),

]
