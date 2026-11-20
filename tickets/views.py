from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket


# Create your views here.
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})
