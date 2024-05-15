from django.urls import path
from . import views


urlpatterns=[
    path("", views.subscribeToNewsLetter, name="subscribeToNewsLetter"),
    path("success", views.success, name="success"),
    path("error", views.error, name="error"),
]