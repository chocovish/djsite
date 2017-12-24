from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
path("", views.IndexView.as_view(), name="index"),
path("<pk>/", views.DetailView.as_view(), name="detail"),
path("albums/add/", views.AlbumCreate.as_view(), name="add-album"),
path("albums/update/<pk>/", views.AlbumUpdate.as_view(), name="update-album"),
path("albums/delete/<pk>/", views.AlbumDelete.as_view(), name="delete-album"),


]