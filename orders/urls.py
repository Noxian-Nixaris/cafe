from django.urls import path

from orders.views import (
    create,
    delete_order,
    edit_order,
    get_404,
    orders,
    search
)

app_name = 'orders'
urlpatterns = [
    path('', create, name='create'),
    path('<int:pk>/', orders, name='order'),
    path('<int:pk>/edit/', edit_order, name='edit_order'),
    path('<int:pk>/delete/', delete_order, name='delete_order'),
    path('search/', search, name='search'),
    path('get_404/', get_404, name='get_404')
]
