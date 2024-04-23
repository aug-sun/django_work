from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_sim_tel_number(value):
    if value is not None and (len(value) != 11 or '+' in value or ' ' in value):
        raise ValidationError(
            _('Неверно указан номер. Убедитесь, что номер содержит 11 символов, не содержит символ "+", и не содержит пробелов.'),
            code='invalid_sim_tel_number'
        )
