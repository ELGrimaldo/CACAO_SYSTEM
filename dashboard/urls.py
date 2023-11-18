from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("boxes/", views.boxes, name="boxes"),
    path("connection/", views.connection, name="connection"),
    path("base/", views.base, name="base"),
    path("receive_data/", views.receive_data, name="receive_data"),
    path("get_box_data/<int:start>/<int:end>/", views.get_box_data, name="get_box_data"),
    path('streamlit/', views.streamlit_view, name='streamlit'),
]
