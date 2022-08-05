from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Client, Account, Credit


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        return Client.objects.all()


class DetailClientView(generic.DetailView):
    model = Client
    template_name = 'detail.html'


class DetailCreditView(generic.DetailView):
    model = Account
    template_name = 'detail_credit.html'
