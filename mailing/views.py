from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.forms import inlineformset_factory

from .forms import ClientForm, DistributionForm, MessageForm
from .models import Client, Distribution, Message, DistributionLog


def index(request):
    return render(request, 'mailing/index.html')


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('mailing:client_list')


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'


class DistributionDetailView(DetailView):
    model = Distribution
    template_name = 'distribution_detail.html'


class DistributionListView(ListView):
    model = Distribution
    template_name = 'distribution_list.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['all'] = self.object_list.count()
        context_data['active'] = self.object_list.filter(status='started').count()  # Исправление здесь

        clients = set()
        [clients.add(client.email) for mailing in self.object_list.prefetch_related('clients') for client in
         mailing.clients.all()]
        context_data['clients_count'] = len(clients)
        return context_data


class DistributionCreateView(CreateView):
    model = Distribution
    form_class = DistributionForm
    template_name = 'distribution_form.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(Distribution, Message, extra=1, form=MessageForm)

        if self.request.method == 'POST':
            context_data['formset'] = MessageFormset(self.request.POST)
        else:
            context_data['formset'] = MessageFormset()

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailing:distribution_list')


class DistributionDeleteView(DeleteView):
    model = Distribution

    def get_success_url(self):
        return reverse('mailing:distribution_list')


class DistributionUpdateView(UpdateView):
    model = Distribution
    form_class = DistributionForm
    template_name = 'distribution_form.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(Distribution, Message, extra=1, form=MessageForm)

        if self.request.method == 'POST':
            context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MessageFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailing:distribution_detail', args=[self.object.pk])


class DistributionLogListView(ListView):
    model = DistributionLog
    template_name = 'distributionlog_list.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['all'] = context_data['object_list'].count()
        context_data['success'] = context_data['object_list'].filter(status=True).count()
        context_data['error'] = context_data['object_list'].filter(status=False).count()

        return context_data
