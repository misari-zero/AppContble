from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import ClientForm
from core.erp.models import Client


def client_list(request):
    data = {
        'title': 'Listado de Clientes',
        'clients': Client.objects.all()
    }
    return render(request, 'client/list.html', data)


class ClientListView(ListView):
    model = Client
    template_name = 'client/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Client.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['create_url'] = reverse_lazy('erp:client_create')
        context['list_url'] = reverse_lazy('erp:client_list')
        context['entity'] = 'Clientes'
        return context


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/create.html'
    success_url = reverse_lazy('erp:client_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             if form.is_valid():
    #                  form.save()
    #             else:
    #                 data['error'] = form.errors
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opcion'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    #     print(request.POST)
    #     form = ClientForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de clientes'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        context['action'] = 'add'
        return context


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/create.html'
    success_url = reverse_lazy('erp:client_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        # print(self.object)
        # print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de clientes'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        context['action'] = 'edit'
        return context


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/delete.html'
    success_url = reverse_lazy('erp:client_list')

    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de clientes'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        context['action'] = 'edit'
        return context
