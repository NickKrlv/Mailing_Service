from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Client, Logs, Message, MailingService
from .forms import MailingServiceForm, ClientForm, MessageForm
from django.views.generic import ListView
from blog.models import BlogPost


class MailingServiceListView(ListView):
    template_name = 'mailing/index.html'
    context_object_name = 'mailing_list'

    def get_queryset(self):
        return MailingService.objects.all()

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['all'] = context_data['object_list'].count()
        context_data['active'] = context_data['object_list'].filter(status=MailingService.started).count()

        mailing_list = context_data['object_list'].prefetch_related('clients')
        clients = set()
        [[clients.add(client.email) for client in mailing.clients.all()] for mailing in mailing_list]
        context_data['clients_count'] = len(clients)

        random_posts = BlogPost.objects.order_by('?')[:3]
        context_data['random_posts'] = random_posts

        return context_data


class MailCreateView(LoginRequiredMixin, CreateView):
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


class MailDetailView(LoginRequiredMixin, DetailView):
    model = MailingService
    template_name = 'mailing/mail_detail.html'
    permission_required = 'mailing.view_mail'


class MailUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MailingService
    form_class = MailingServiceForm
    template_name = 'mailing/mail_form.html'
    success_url = reverse_lazy('mailing:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingService, Message, extra=1, form=MessageForm)

        if hasattr(self, 'object') and self.request.method == 'POST':
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

    def test_func(self):
        if self.request.user.has_perm('mailing.set_active'):
            return True
        return False


class MailDeleteView(LoginRequiredMixin, DeleteView):
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


@login_required
@permission_required('mailing.set_active', raise_exception=True)
def toggle_mailing_activity(request, pk):
    mailing = get_object_or_404(MailingService, pk=pk)
    mailing.is_active = not mailing.is_active
    mailing.save()
    return HttpResponseRedirect(reverse('mailing:index'))
