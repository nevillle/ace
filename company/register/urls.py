from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^company/$', views.Register.as_view()),
]