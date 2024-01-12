from django import forms
from .models import Client, Distribution, Message


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'full_name', 'comment']


class DistributionForm(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = ['start_time', 'frequency', 'status', 'clients']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['distribution', 'title', 'body']
