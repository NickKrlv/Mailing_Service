from django.urls import path
from django.views.decorators.cache import cache_page

from .views import MailingServiceListView, MailCreateView, MailDetailView, MailUpdateView, MailDeleteView, \
    ClientsListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, LogsListView, \
    toggle_mailing_activity

app_name = 'mailing'

urlpatterns = [
    path('', MailingServiceListView.as_view(), name='index'),
    path('mailing/', MailingServiceListView.as_view(), name='mail_list'),
    path('create_mailing/', MailCreateView.as_view(), name='create_mailing'),
    path('mailing/<int:pk>/', MailDetailView.as_view(), name='mail_detail'),
    path('mailing/<int:pk>/update/', MailUpdateView.as_view(), name='mail_update'),
    path('mailing/<int:pk>/delete/', MailDeleteView.as_view(), name='mail_delete'),
    path('clients/', ClientsListView.as_view(), name='clients'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('logs/', LogsListView.as_view(), name='logs'),
    path('mailing/toggle-activity/<int:pk>/', toggle_mailing_activity, name='toggle_mailing_activity'),
]
