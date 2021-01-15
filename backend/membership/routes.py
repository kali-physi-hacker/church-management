from django.urls import path

from .views.ministry import MinistryListView, MinistryDetailView


urlpatterns = [
    path("ministry/", MinistryListView.as_view(), name="ministry_list"),    # List(GET) and Create(POST)
    path("ministry/<int:pk>/", MinistryDetailView.as_view(), name="ministry_detail"),
]

app_name = "membership"
