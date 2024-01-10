from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('calendar', views.calendar_call, name='calendar'),
    path('not_present', views.not_present_accounts, name='not_present'),
    path('edit_login/<int:pk>', views.UpdateUserView.as_view(), name='edit_login'),
    path('download_excel', views.download_excel, name='download_excel'),
    path("contragents", views.get_contragents_data, name="contragents"),
    path("list_logins", views.ListLoginsView.as_view(), name="list_logins"),
    path("detail_login/<int:pk>", views.DetailLoginsView.as_view(), name="detail_login"),
]
