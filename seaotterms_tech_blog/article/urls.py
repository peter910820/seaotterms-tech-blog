from django.urls import path
from .views import index, main_page

urlpatterns = [
    path('', index),
    path('test/', main_page)
]
