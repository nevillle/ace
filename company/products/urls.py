from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$', views.AddProduct.as_view()),
    url(r'^list/(?P<company_id>\d+)/$', views.GetProducts.as_view()),
]