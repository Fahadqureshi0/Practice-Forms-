from django.urls import path
from .import views

urlpatterns = [
    path("application/",views.app_view,name="user_profile"),
]
