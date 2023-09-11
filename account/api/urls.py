from django.urls import path
from account.api import views

urlpatterns = [
    path("account-list-create/", views.AccountListCreateAPIView.as_view(), name="account-list-create"),
    path("account-retrieve-update-delete/<int:id>/", views.AccountRetrieveRetrieveDestroyAPIView.as_view(), name="account-retrieve=update-delete"),

]