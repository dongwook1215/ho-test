from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewmore/<int:diary_id>', views.viewmore, name='viewmore')
]
