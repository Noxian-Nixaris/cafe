from django.urls import path

from orders.views import (
    create,
    delete_order,
    edit_order,
    get_404,
    orders,
    list_order,
    search,
    shift,
    status_change
)

app_name = 'orders'
urlpatterns = [
    path('', shift, name='shift'),
    path('create/', create, name='create'),
    path('<int:pk>/', orders, name='order'),
    path('<int:pk>/edit/', edit_order, name='edit_order'),
    path('<int:pk>/status/', status_change, name='status_change'),
    path('<int:pk>/delete/', delete_order, name='delete_order'),
    path('list/', list_order, name='list'),
    path('search/', search, name='search'),
    path('get_404/', get_404, name='get_404')
]
