from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("admin/", admin.site.urls),
    path("api/", include("membership.routes")),
    path("api/", include("authentication.routes")),
    re_path(r"^.*/$", TemplateView.as_view(template_name="index.html")),
]
