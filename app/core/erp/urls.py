from django.urls import path
from core.erp.views.client.views import *

app_name = 'erp'

urlpatterns = [
    path('client/list/', ClientListView.as_view(), name='client_list' ),
    path('client/list2/', client_list, name='client_list2' ),
    path('client/add/', ClientCreateView.as_view(), name='client_create' ),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
