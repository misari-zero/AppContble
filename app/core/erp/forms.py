from datetime import datetime
from django.forms import *

from core.erp.models import Client, Product, Categoria, Plancontable, Elemento, Diario, Tipocuenta, Mayor


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
        # self.fields['fecha'].widget.format = '%d/%m/%Y'

    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'name': 'Razon social'
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
            'fecha': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
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


class ElementoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Elemento
        fields = '__all__'
        widgets = {
            'nro': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese el código',
                    # 'autocomplete': 'off'
                }
            ),
            'name': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
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


class TipocuentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Tipocuenta
        fields = '__all__'
        widgets = {
            'codigo': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese el codigo',
                    # 'autocomplete': 'off'
                }
            ),
            'name': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
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


class PlancontableForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Plancontable
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
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


class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    # 'autocomplete': 'off'
                }
            ),
            'desc': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese descripción',
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


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    # 'autocomplete': 'off'
                }
            ),
            'desc': TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese descripción',
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


# class ComprobanteingresoForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = Comprobanteingreso
#         fields = '__all__'
#         widgets = {
#             'numero': TextInput(
#                 attrs={
#                     # 'class': 'form-control',
#                     'placeholder': 'Nro de comprobante',
#                     # 'autocomplete': 'off'
#                 }),
#             'cli': Select(attrs={
#                 'class': 'form-control select2',
#                 'style': 'width: 100%'
#             }),
#
#             'fecha': DateInput(format='%Y-%m-%d',
#                                attrs={
#                                    'value': datetime.now().strftime('%Y-%m-%d'),
#                                    'autocomplete': 'off',
#                                    'class': 'form-control datetimepicker-input',
#                                    'id': 'date_joined',
#                                    'data-target': '#date_joined',
#                                    'data-toggle': 'datetimepicker'
#                                }),
#             'iva': TextInput(attrs={
#                 'class': 'form-control',
#             }),
#             'subtotal': TextInput(attrs={
#                 'readonly': True,
#                 'class': 'form-control',
#             }),
#             'total': TextInput(attrs={
#                 'readonly': True,
#                 'class': 'form-control',
#             })
#         }


class DiarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs['autofocus'] = True

    class Meta:
        model = Diario
        fields = '__all__'
        widgets = {
            'ano': Select(),
            'mes': Select(),
            'date_joined': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'cuenta': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'desc': TextInput(attrs={
                'placeholder': 'Ingrese descripcion',
            }),
            'impuestos': TextInput(attrs={
                'placeholder': 'Ingrese impuesto',
            }),
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


class EgresoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs['autofocus'] = True

    class Meta:
        model = Diario
        fields = '__all__'
        widgets = {
            'ano': Select(),
            'mes': Select(),
            'date_joined': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'cuenta': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'desc': TextInput(attrs={
                'placeholder': 'Ingrese descripcion',
            }),
            'impuestos': TextInput(attrs={
                'placeholder': 'Ingrese impuesto',
            }),
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


class MayorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs['autofocus'] = True

    class Meta:
        model = Mayor
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Ingrese el tipo diario',
            }),
            'ano': Select(),
            'mes': Select(),
            'date_joined': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            # 'cuenta': Select(
            #     attrs={
            #         'class': 'select2',
            #         'style': 'width: 100%'
            #     }
            # ),
            'desc': TextInput(attrs={
                'placeholder': 'Ingrese descripcion',
            }),
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
