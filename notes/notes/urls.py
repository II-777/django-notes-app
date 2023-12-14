from django.contrib import admin
from django.urls import path, include

app_name = "noteapp"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("noteapp.urls")),
    path('users/', include('users.urls')),
]