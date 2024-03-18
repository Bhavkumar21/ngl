from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("remark/", views.remark, name="remark"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("profile/<str:username>", views.profile, name="profile"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)