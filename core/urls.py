# -*- encoding: utf-8 -*-


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.authentication.urls")),  # Auth routes - login / register
    path("contacts/", include("apps.contacts.urls")),
    # ADD NEW Routes HERE
    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls")),
]
