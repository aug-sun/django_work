from django.shortcuts import render
from birix.utils import get_accouns, get_history
from datetime import datetime
from django.contrib import admin
import birix.models as models
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.http import HttpResponse


@login_required
def calendar_call(request):
    if request.method == 'POST':
        start = request.POST['start_date']
        end = request.POST['end_date']
        duration_user = request.POST['duration']
        detes = get_history(start, end)
        officers = get_accouns()
        result = []
        ofice_users = models.AuthUser.objects.all()
        list_last_names = []
        view_user = request.user.username
        concrete_user = models.AuthUser.objects.filter(username=view_user).first()
        for i in ofice_users:
            list_last_names.append(f"{i.last_name} {i.first_name}")

        for i in detes:
            count = len(str(i).split(","))
            if count >= 8:
                if int(str(i).split(",")[7]) >= int(duration_user):
                    clear_date = str(str(i).split(",")[5]).replace("T", " ").replace("Z", "")
                    clear_type = "Входящий звонок" if str(i).split(",")[1] == "in" else "Исходящий звонок"
                    duration = str(i).split(",")[7]
                    h = int(duration) // 3600
                    m = int(duration) % 3600 // 60
                    s = int(duration) % 60

                    clear_duration = f"{h:02d}:{m:02d}:{s:02d}"
                    clear_name = ""
                    name = str(str(i).split(",")[3]).split("@")[0]
                    for o in officers:
                        if name == o["name"]:
                            clear_name = o["realName"]

                    link_head = str(i).split(",")[8]
                

                    if clear_name in list_last_names:

                        result.append(
                                {
                                    'date': clear_date,
                                    'type': clear_type,
                                    'number': str(i).split(",")[2],
                                    'name': clear_name,
                                    'duration': clear_duration,
                                    "link": link_head,
                                }
                                )
                
        return render(request, 'calendar.html', {'results': result})
    else:
        return render(request, 'calendar.html')

@login_required
def not_present_accounts(request):
    not_present = models.LoginUsers.objects.filter(
       account_status=1,
    ).all()
    results = []
    for i in not_present:
        if i.contragent == None:
            client = "Нет привязки к клиенту 1с"
        else:
            client = i.contragent.ca_name

        results.append(
                {
                    'login': i.login,
                    'client': client,
                    'id': i.id
                }
                )
    return render(request, 'not_present.html', {'results': results})


@login_required
def home(request):
    return render(request, 'home.html')

class UpdateUserView(UpdateView):
    model = models.LoginUsers
    success_message = 'Учётка успешно обновлена'
    fields = ['account_status']
    template_name = 'edit_login.html'
    success_url = '../not_present'


