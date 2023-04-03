from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from pay.models import Paidusers, ContactData
from pay.forms import PaidingForm

from time import sleep

class payment(CreateView):
    template_name = 'payment.html'
    model = Paidusers
    success_url = '/'
    form_class = PaidingForm

    def form_valid(self, form=PaidingForm):
        sleep(8)
        # Place for pay
        return super().form_valid(form)

class contacts(ListView):
    template_name = 'contacts.html'
    context_object_name = 'contacts'
    model = ContactData
    queryset = ContactData.objects.all()
    fields = ['image', 'name', 'contact']