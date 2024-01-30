from .models import MailingService, Client, Logs
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class MailingServiceListView(ListView):
    template_name = 'mailing/index.html'
    context_object_name = 'mailing_list'

    def get_queryset(self):
        return MailingService.objects.all()


class MailCreateView(CreateView):
    model = MailingService
    fields = '__all__'
    success_url = '/'


class MailDetailView(DetailView):
    model = MailingService
    template_name = 'mailing/mail_detail.html'


class MailUpdateView(UpdateView):
    model = MailingService
    fields = '__all__'
    success_url = '/'


class MailDeleteView(DeleteView):
    model = MailingService
    success_url = '/'


class ClientsListView(ListView):
    model = Client
    template_name = 'mailing/clients.html'
    context_object_name = 'clients_list'

    def get_queryset(self):
        return Client.objects.all()


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    success_url = '/'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mailing/client_detail.html'


class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    success_url = '/'


class ClientDeleteView(DeleteView):
    model = Client
    success_url = '/'


class LogsListView(ListView):
    model = Logs
    template_name = 'mailing/logs.html'
    context_object_name = 'logs_list'

    def get_queryset(self):
        return Logs.objects.all()
