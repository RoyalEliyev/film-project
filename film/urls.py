from django.urls import path
from film import views

urlpatterns = [
    path("detail/<int:id>/", views.DetailView.as_view(), name="detail"),
    path("liked_films/", views.LikedFilmsView.as_view(), name="like"),
    path("comment/", views.CommesFilmsView.as_view(), name="comment"),
    path("views_count/", views.ViewsCountView.as_view(), name="viewscount"),
    path("index/", views.IndexView.as_view() , name="index")
]