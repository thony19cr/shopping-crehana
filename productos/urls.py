from django.conf.urls import url
from productos.views import (
    HomeView, ProductBuyView
)

urlpatterns = [
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"product/(?P<pk>\d+)/buy/$", ProductBuyView.as_view(), name="buy"),
]
