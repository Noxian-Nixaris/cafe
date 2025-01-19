from django import forms

from core.constants import STATUS
from orders.models import Dish, Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('table_number', 'items')
        widgets = {
            'items': forms.CheckboxSelectMultiple
        }


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('table_number', 'items', 'status')
        widgets = {
            'items': forms.CheckboxSelectMultiple
        }
