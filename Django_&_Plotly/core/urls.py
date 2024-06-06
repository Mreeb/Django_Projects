from django.urls import path
from . import views

urlpatterns = [
    path("plot/", views.plot_view),
    path("hello/", views.hello)
]