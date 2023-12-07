from django.shortcuts import render
from birix.utils import get_accouns, get_history
from datetime import datetime


def calendar_call(request):
    if request.method == 'POST':
        start = request.POST['start_date']
        end = request.POST['end_date']
        duration = request.POST['duration']
        detes = get_history(start, end)
        officers = get_accouns()
        result = []
        for i in detes:
            count = len(str(i).split(","))
            if count >= 8:
                if int(str(i).split(",")[7]) >= int(duration):
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

                    result.append(
                            {
                                'date': clear_date,
                                'type': clear_type,
                                'number': str(i).split(",")[2],
                                'name': clear_name,
                                'duration': clear_duration,
                            }
                            )
                
        return render(request, 'calendar.html', {'results': result})
    else:
        return render(request, 'calendar.html')



