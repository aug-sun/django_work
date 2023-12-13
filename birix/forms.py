from django import forms
from birix.models import *


class LoginClientForm(forms.Form):
    status = forms.ChoiceField(choices=[(1, 'Не подверждена но активирована'), (0, 'Заблокирована'), (2, 'Подверждена и активирована')])

