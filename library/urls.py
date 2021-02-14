from django.urls import path
from . import views
from .api.views import BookAPIView
urlpatterns = [
    path('', views.index, name="index"),
    path('api/books/', BookAPIView.as_view(), name="list-create-books")
]
