from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("boxes", views.boxes, name="boxes"),
    path("connection", views.connection, name="connection"),
    path("base", views.base, name="base"),
]