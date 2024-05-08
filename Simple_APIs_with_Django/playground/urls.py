from django.urls import path
from . import views


#URLConf

urlpatterns = [
    path("hello/", views.Hello_world),
    path("greetings/", views.greetings),
    path("sum/", views.sum),
    path("List/", views.List),
    path("sum_post/", views.sum_post),
    path("name_con/", views.name_con),
    path("sum_list/", views.sum_list),
    path("clus/", views.clustering_Algo),
    path("img/", views.sending_img),

]
