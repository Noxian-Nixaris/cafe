from django.shortcuts import get_object_or_404, redirect, render

from orders.forms import OrderCreateForm, OrderForm
from orders.models import Dish, Order


def search(request):
    template_name = 'orders/search.html'
    order_id = request.GET.get('order_id')
    context = {}
    if order_id:
        try:
            Order.objects.get(pk=order_id)
            return redirect('orders:order', pk=order_id)
        except Order.DoesNotExist:
            message = f'Заказ c ID {order_id} не найден.'
            context = {'message': message}
    return render(request, template_name, context)


def create(request):
    template_name = 'orders/form.html'
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            total_price = sum(dish.price for dish in form.cleaned_data['items'])
            order.total_price = total_price
            form.save()
            print(order.id)
            return redirect(f'{order.id}/')
    else:
        form = OrderCreateForm()
    context = {'form': form}
    return render(request, template_name, context)


def orders(request, pk):
    template_name = 'orders/order.html'
    try:
        order = get_object_or_404(Order, id=pk)
        dishes = Dish.objects.filter(order=pk)
        context = {'order': order, 'dishes': dishes}
        return render(request, template_name, context)
    except Order.DoesNotExist:
        return redirect('orders:get_404')


def edit_order(request, pk):
    template_name = 'orders/form.html'
    try:
        order = Order.objects.get(pk=pk)
        if request.method == 'POST':
            form = OrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect('orders:order', pk=pk)
        else:
            form = OrderForm(instance=order)
            context = {'form': form}
            return render(request, template_name, context)
    except Order.DoesNotExist:
        return redirect('orders:get_404')


def delete_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        order.delete()
    except Order.DoesNotExist:
        return redirect('orders:get_404')
    return redirect('orders:create')


def get_404(request):
    template = 'orders/get_404.html'
    return render(request, template)
