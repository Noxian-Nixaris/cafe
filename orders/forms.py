from django import forms
from django.core.exceptions import ValidationError

from orders.models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('table_number', 'items')
        widgets = {
            'items': forms.CheckboxSelectMultiple
        }

    def clean_table_number(self):
        table_number = self.cleaned_data.get('table_number')

        if table_number is not None and table_number < 0:
            raise ValidationError('Номера стола не может быть отрицательным.')

        return table_number
