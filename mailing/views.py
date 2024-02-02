from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import MailingService, Client, Logs, Message
from .forms import MailingServiceForm, ClientForm, MessageForm


class MailingServiceListView(ListView):
    template_name = 'mailing/index.html'
    context_object_name = 'mailing_list'

    def get_queryset(self):
        return MailingService.objects.all()


class MailCreateView(CreateView):
    model = MailingService
    form_class = MailingServiceForm
    template_name = 'mailing/mail_form.html'
    success_url = reverse_lazy('mailing:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingService, Message, extra=1, form=MessageForm)

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
        return reverse('mailing:mail_detail', args=[self.object.pk])


class MailDetailView(DetailView):
    model = MailingService
    template_name = 'mailing/mail_detail.html'


class MailUpdateView(UpdateView):
    model = MailingService
    form_class = MailingServiceForm
    template_name = 'mailing/mail_form.html'
    success_url = reverse_lazy('mailing:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingService, Message, extra=1, form=MessageForm)

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


class MailDeleteView(DeleteView):
    model = MailingService
    template_name = 'mailing/mail_confirm_delete.html'
    success_url = reverse_lazy('mailing:index')


class ClientsListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:clients')


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mailing/client_detail.html'


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:clients')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mailing/client_confirm_delete.html'
    success_url = reverse_lazy('mailing:clients')


class LogsListView(ListView):
    model = Logs
    template_name = 'mailing/log_list.html'
