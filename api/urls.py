from django.urls import path
from .views import LinksView

app_name = 'api'

urlpatterns = [
    path('', LinksView.as_view(), name='links'),
]
