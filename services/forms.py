from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        total_float = self.request.session.get('total_float')
        super().__init__(*args, **kwargs)
        self.fields['total'].initial = total_float

    class Meta:
        model = Pedido
        fields = ['correo', 'nombre', 'direccion', 'colonia', 'total']
        widgets = {
            'correo':forms.EmailInput(
                attrs={'class':'form-control', 'place.holder':'Email'}),
            'nombre':forms.TextInput(
                attrs={'class':'form-control', 'place.holder':'Nombre'}),
            'direccion':forms.TextInput(
                attrs={'class':'form-control', 'place.holder':'Calle y numero'}),
            'colonia':forms.TextInput(
                attrs={'class':'form-control', 'place.holder':'Colonia'}),
            'total':forms.TextInput(
                attrs={'class':'form-control', 'readonly':'readonly'}),
        }