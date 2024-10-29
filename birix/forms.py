from django import forms
from django.db.models.expressions import fields
from birix.validators import validate_login, validate_password
from birix.models import *

class NewLoginForm(forms.ModelForm):
    class Meta:
        model = LoginUsers
        fields = [
                'client_name',
                'login',
                'email',
                'password',
                'date_create',
                'system',
                'contragent',
                'comment_field',
                'ca_uid',
                'account_status',
                ]

    def clean_form(self):
        login = self.cleaned_data.get("login")
        if self.instance.pk is None:
            validate_login(login)
        return login
