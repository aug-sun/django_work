from django.urls import path
from .views import HomeView, CalendarView, ClientsView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('calendar', CalendarView.as_view(), name='calendar'),
    path('clients', ClientsView.as_view(), name='clients'),

]

