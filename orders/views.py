from django.shortcuts import redirect, render

from core.constants import STATUS
from orders.forms import OrderCreateForm
from orders.models import Order, Shift


def shift(request):
    template_name = 'orders/shift.html'
    message = None
    shifts = Shift.objects.all().order_by('-id')
    current_shift = shifts.filter(is_open=True).last()
    if request.method == 'POST':
        if 'open' in request.POST:
            try:
                Shift.objects.get(is_open=True)
                message = 'Смена уже открыта'
            except Shift.DoesNotExist:
                Shift.objects.create()
                message = 'Смена открыта'
        elif 'close' in request.POST:
            try:
                shift = Shift.objects.get(is_open=True)
                shift.is_open = False
                shift.save()
                message = 'Смена закрыта'
            except Shift.DoesNotExist:
                message = 'Нет открытой смены'
    elif request.method == 'GET':
        if 'calculate' in request.GET:
            try:
                shift_id = request.GET.get('shift_id')
                shift = Shift.objects.get(pk=shift_id)
                orders = Order.objects.filter(shift=shift)
                earnings = sum(order.total_price for order in orders)
                message = f'Выручка {earnings}'
            except Shift.DoesNotExist:
                message = 'Такой смены нет'
            except ValueError:
                message = 'Номер смены не задан'

    context = {
        'shifts': shifts,
        'message': message,
        'current_shift': current_shift
    }
    return render(request, template_name, context)


def search(request):
    template_name = 'orders/search.html'
    order_id = request.GET.get('order_id')
    message = None
    if order_id:
        try:
            Order.objects.get(pk=order_id)
            return redirect('orders:order', pk=order_id)
        except Order.DoesNotExist:
            message = f'Заказ c ID {order_id} не найден.'
        except ValueError:
            message = 'Некорректно задан номер стола'

    context = {'message': message}
    return render(request, template_name, context)


def list_order(request):
    template_name = 'orders/list.html'
    orders = Order.objects.all()
    message = None
    query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')

    if query:
        try:
            if int(query) > 0:
                print(type(query))
                orders = orders.filter(table_number=query)
            else:
                message = 'Некорректно задан номер стола'
        except ValueError:
            message = 'Некорректно задан номер стола'

    if status_filter:
        if status_filter in [str(st[0]) for st in STATUS]:
            orders = orders.filter(status=status_filter)
        else:
            message = 'Некорректно задан статус'

    context = {
        'orders': orders,
        'search_query': query,
        'statuses': STATUS,
        'selected_status': status_filter,
        'message': message}
    return render(request, template_name, context)


def create(request):
    template_name = 'orders/form.html'

    shift = Shift.objects.get_or_create(is_open=True)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            total_price = sum(dish.price for dish in form.cleaned_data['items'])
            order.total_price = total_price
            form.save()
            shift[0].orders.add(order)
            return redirect('orders:order', pk=order.id)
    else:
        form = OrderCreateForm()

    context = {'form': form}
    return render(request, template_name, context)


def orders(request, pk):
    template_name = 'orders/order.html'
    try:
        order = Order.objects.get(pk=pk)
        context = {'order': order}
        return render(request, template_name, context)
    except Order.DoesNotExist:
        return redirect('orders:get_404')


def edit_order(request, pk):
    template_name = 'orders/form.html'
    try:
        order = Order.objects.get(pk=pk)
        if request.method == 'POST':
            form = OrderCreateForm(request.POST, instance=order)
            if form.is_valid():
                total_price = sum(dish.price for dish in form.cleaned_data['items'])
                order.total_price = total_price
                form.save()
                return redirect('orders:order', pk=pk)
        else:
            form = OrderCreateForm(instance=order)
            context = {'form': form}
            return render(request, template_name, context)
    except Order.DoesNotExist:
        return redirect('orders:get_404')


def status_change(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        if order.status < 3:
            order.status += 1
        order.save()
        return redirect('orders:order', pk=pk)
    except Order.DoesNotExist:
        return redirect('orders:get_404')


def delete_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        order.delete()
    except Order.DoesNotExist:
        return redirect('orders:get_404')
    return redirect('orders:list')


def get_404(request):
    template = 'orders/get_404.html'
    return render(request, template)
