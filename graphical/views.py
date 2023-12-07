from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q, Case, When, Value, CharField
from bitrix.models import Tdata, Tagat, Temail, Tklient, Twialon100, Ttarif
from django.http import HttpResponse
import pandas as pd
from django.http import JsonResponse

class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage.html'
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    def get(self, request):
        return Response()


class CalendarView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'calendar.html'
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self, request):
        return Response()

    def post(self, request):
        selected_date = request.POST.get('selected_date')
        filter_object = request.POST.get('filter_object')
        tdata = Tdata.objects.filter(Q(dimport__date=selected_date), Q(object__icontains=filter_object)).values('login', 'idsystem', 'object', 'idobject', 'isactive', 'dimport')

        system_names = {
            11: 'WHosting',
            12: 'Fort',
            13: 'GSoft',
            14: 'Scout',
            15: 'ERA',
            16: 'Wlocal',
        }
        for data in tdata:
            data['idsystem'] = system_names.get(data['idsystem'], data['idsystem'])

        if 'download' in request.POST:
            df = pd.DataFrame(tdata)
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
            df.to_excel(response, index=False)
            return response

        return render(request, 'calendar.html', {'tdata': tdata})


class ClientsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'calendar.html'
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self, request):
        return Response()

    def post(self, request):
        selected_date = request.POST.get('selected_date')
        filter_object = request.POST.get('filter_object')

        tdata = Tdata.objects.filter(isactive='Да')
        tdata = tdata.exclude(object__icontains='ТЕСТ')
        tdata = tdata.exclude(Q(object__icontains='TEST') & ~Q(object__icontains='MICROTEST'))
        tdata = tdata.exclude(object__icontains='ПРИОСТ')
        tdata = tdata.exclude(object__icontains='ППРО')
        tdata = tdata.exclude(object__icontains='НОВТ')
        tdata = tdata.exclude(Q(object__icontains='ПЕРЕ') & Q(idsystem__in=[11, 16]))
        tdata = tdata.exclude(Q(login__icontains='ТЕСТ') & Q(idsystem=15))
        tdata = tdata.filter(dimport=Tdata.objects.latest('dimport').dimport)

        twialon100 = Twialon100.objects.filter(logintd__in=tdata.values_list('login', flat=True))
        tklient = Tklient.objects.filter(id__in=twialon100.values_list('tkid', flat=True))
        ttarif = Ttarif.objects.filter(tkid__in=tklient)
#    tagat = Tagat.objects.filter(idsystem__in=tdata.values_list('idsystem', flat=True), idobject__in=tdata.values_list('idobject', flat=True), dbeg__lte=tdata.values_list('dimport', flat=True), dend__gte=tdata.values_list('dimport', flat=True))

        system_names = {
            11: 'WHost',
            12: 'Fort',
            13: 'GSoft',
            14: 'Scout',
            15: 'Era',
            16: 'WLocal',
        }

    # tdata = tdata.annotate(
    #     kontragent=Case(
    #         When(idsystem__in=[11, 12, 13, 14, 15, 16], then=tagat.values('name')),
    #         When(idsystem=15, then=ttarif.values('tkid__name')),
    #         default=Value(''),
    #         output_field=CharField(),
    #     ),
    #     system_name=Case(
    #         When(idsystem__in=[11, 12, 13, 14, 15, 16], then=Value(system_names)),
    #         default=Value(''),
    #         output_field=CharField(),
    #     ),
    # )

        results = []
        for data in tdata:
            result = {
                'kontragent': data.kontragent,
                'system_name': system_names.get(data.idsystem, ''),
                'object': data.object,
            }
            results.append(result)

        return render(request, 'calendar.html', {'tdata': tdata})
