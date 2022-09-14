# TODO: Implement Routings Here

from urllib.parse import urlparse
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
        path('', show_katalog, name='show_katalog'),
]