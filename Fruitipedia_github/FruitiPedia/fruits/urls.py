from django.urls import path

from FruitiPedia.fruits import views

urlpatterns = (
    path("index/", views.index, name="index"),
)