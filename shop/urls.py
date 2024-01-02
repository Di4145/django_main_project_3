from django.urls import path

from shop.views import detail

urlpatterns = [
    path('detail/<int:id>/', detail, name='detail_shop'),
]
