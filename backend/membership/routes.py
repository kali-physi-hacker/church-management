from django.urls import path

from .views.ministry import MinistryListView, MinistryDetailView
from .views.member import MemberListView, MemberDetailView


urlpatterns = [
    path("ministry/", MinistryListView.as_view(), name="ministry_list"),  # List(GET) and Create(POST)
    path("ministry/<int:pk>/", MinistryDetailView.as_view(), name="ministry_detail"),

    path("member/", MemberListView.as_view(), name="member_list"),
    path("member/<int:pk>/", MemberDetailView.as_view(), name="member_detail"),
]

app_name = "membership"
