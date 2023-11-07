
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("users.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("ticket/", include("ticket.urls")),
]
