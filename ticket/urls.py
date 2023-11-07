from django.urls import path
from . import views

urlpatterns = [
    path('ticket_details/<int:pk>/', views.TicketDetails, name='ticket_details'),
    path('create_ticket/', views.CreateTicket, name='create_ticket'),
    path('update_ticket/<int:pk>/', views.UpdateTicket, name='update_ticket'),
    path('all_tickets/', views.ListViewTicket, name='all_tickets'),
    path('ticket_queue/', views.TicketQueue, name='ticket_queue'),
    path('accept_ticket/<int:pk>/', views.AcceptTicket, name='accept_ticket'),
    path('close_ticket/<int:pk>/', views.CloseTicket, name='close_ticket'),
    path('workspace/', views.WorkSpace, name='workspace'),
    path('all_close_tickets/', views.AllCloseTickets, name='all_close_tickets'),
]