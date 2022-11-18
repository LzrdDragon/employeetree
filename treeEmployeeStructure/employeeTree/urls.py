from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('divisions/<int:division_id>', views.get_employees, name='get_employees'),
]
