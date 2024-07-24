from django.urls import path, include

from FruitiPedia.fruits import views

urlpatterns = [
    path("", include("FruitiPedia.fruits.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create-fruit/", views.create_fruit, name="create-fruit"),
    path("<int:pk>/", include([
        path("details-fruit/", views.details, name="details fruit"),
        path("edit-fruit/", views.edit_fruit, name="edit fruit"),
        path("delete-fruit/", views.delete_fruit, name="delete fruit")
    ])),
    path("create-category/", views.create_category, name="create-category")
]
