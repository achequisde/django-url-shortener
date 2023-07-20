from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result, name='result'),
    path('result/<str:link_id>', views.result_with_id, name='result_with_id'),
    path('<str:link_id>', views.detail, name='detail'),
]
