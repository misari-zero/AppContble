from django.forms import *

from core.erp.models import Client


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'name': 'Nombre o Razon social'
        }
        widgets = {
            'name': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    # 'autocomplete': 'off'
                }
            ),
            'address': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese la dirección',
                    # 'autocomplete': 'off'
                }
            ),
            'ruc': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese el ruc',
                    # 'autocomplete': 'off'
                }
            ),
            'fecha': DateInput(
                attrs={
                    # 'class': 'form-control',
                    # 'placeholder': 'Ingrese la dirección',
                    # 'autocomplete': 'off'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data