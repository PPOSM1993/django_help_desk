from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ticket
import datetime
from .form import CreateTicketForm, UpdateTicketForm
from users.models import User

# Create your views here.

#View Ticket Details

def TicketDetails(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    t = User.objects.get(username=ticket.created_by)
    tickets_per_user = t.created_by.all()
    context = {'ticket': ticket, 'tickets_per_user': tickets_per_user}
    return render(request, 'ticket/ticket_details.html', context)

# create a ticket

# For Customer

def CreateTicket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.ticket_status = 'Pending'
            var.save()
            messages.info(
                request, 'Your Ticket has been successfully submitted. An engineer would be assigned soon.')
            return redirect('dashboard')
        else:
            messages.warning(
                request, 'Something went wrong. Please check form input')
    else:
        form = CreateTicketForm()
        context = {'form': form}
        return render(request, 'ticket/create_ticket.html', context)

# update a ticket

# For Customer


def UpdateTicket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateTicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request, 'Your Ticket has been successfully updated.')
            return redirect('dashboard')
        else:
            messages.warning(
                request, 'Something went wrong. Please check form input')
    else:
        form = UpdateTicketForm(instance=ticket)
        context = {'form': form}
        return render(request, 'ticket/update_ticket.html', context)


def ListViewTicket(request):
    tickets = Ticket.objects.filter(created_by=request.user).order_by('-date_created')
    context = {'tickets': tickets}
    return render(request, 'ticket/all_tickets.html', context)


# For Engineers
def TicketQueue(request):
    tickets = Ticket.objects.filter(ticket_status='Pending')
    context = {'tickets': tickets}
    return render(request, 'ticket/ticket_queue.html', context)

# Accepted Ticket


def AcceptTicket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.assigned_to = request.user
    ticket.ticket_status = 'Active'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(
        request, 'Ticket has been accepted. Please resolve as soon as possible')
    return redirect('workspace')

# Close Ticket


def CloseTicket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.ticket_status = 'Completed'
    ticket.is_resolved = True
    ticket.close_date = datetime.datetime.now()
    ticket.save()
    messages.info(
        request, 'Ticket has been resolved. Thank you brilliant Support Engineer!')
    return redirect('ticket-queue')


# Ticket Engineer is Working on
def WorkSpace(request):
    tickets = Ticket.objects.filter(
        assigned_to=request.user, is_resolved=False)
    context = {'tickets': tickets}
    return render(request, 'ticket/workspace.html', context)


#All Close/Resolved Tickets
def AllCloseTickets(request):
    tickets = Ticket.objects.filter(assigned_to=request.user, is_resolved=True)
    context = { 'tickets': tickets }
    return render(request, 'ticket/all_close_tickets.html', context)
