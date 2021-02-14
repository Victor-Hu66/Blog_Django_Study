from django.urls import path
from .views import home, post_list, post_create

app_name = "blog"
urlpatterns = [
    # path("", home),
    path("", post_list, name="list"),
    path("create/", post_create, name="create")
]