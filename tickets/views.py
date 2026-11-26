from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Ticket


# Create your views here.
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})


def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    return render(request, "tickets/ticket_detail.html", {"ticket": ticket})
