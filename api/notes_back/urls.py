from django.urls import path
from .views import *

urlpatterns = [
    path('notes/', notes_list),
    path('notes/<int:pk>/', notes_detail),
]
