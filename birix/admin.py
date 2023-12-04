from django.contrib import admin
from birix.models import *

class ContragentsAdmin(admin.ModelAdmin):
    list_display = (
            "ca_name", 
            "ca_shortname",
            "ca_inn",
            "ca_kpp",
            "ca_field_of_activity",
            )
    list_filter = (
            "ca_type",
            "registration_date",
            "ca_field_of_activity",
            "key_manager",
            )
    search_fields = (
            "ca_name",
            "ca_inn",
            "ca_kpp",
            "ca_field_of_activity",
            )

    fieldsets = (
            (None, {
                'fields': (
                    'ca_name',
                    'ca_shortname',
                    'ca_inn',
                    'ca_kpp',
                    'ca_field_of_activity',
                )
            }),
        
        )
    list_per_page = 20

class LoginUsersAdmin(admin.ModelAdmin):
    list_display = (
            "client_name",
            "login",
            "email",
            "password",
            "date_create",
            "system",
            "contragent",
            "comment_field",
            )

    list_filter = (
            "system",
            "date_create",

            )
    search_fields = (
            "client_name",
            "login",
            "comment_field",
            "contragent__ca_name",
    )

    fieldsets = (
            (None, {
                'fields': (
                    'client_name',
                    'login',
                    'email',
                    'password',
                    'date_create',
                    'system',
                    'contragent',
                    'comment_field',
                )
            }),
    )

    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': (
                    'client_name',
                    'login',
                    'email',
                    'password',
                    'date_create',
                    'system',
                    'contragent',
                    'comment_field',
                )
            })
    )
    raw_id_fields = ('contragent',)
    list_per_page = 20

class CaObjectsAdmin(admin.ModelAdmin):
    list_display = (
            "sys_mon",
            "object_name",
            "object_status",
            "owner_contragent",
            "owner_user",
            "contragent",
            "imei",
            "get_device",
            "get_sim",
            )

    list_filter = (
            "object_status",
            "sys_mon",
#            "contragent",
#            "contragent",
            )
    search_fields = (
            "object_name",
            "contragent__ca_name",
#            "object_status__status_id",
            "owner_user",
            "owner_contragent",
            "imei",
    )

    fieldsets = (
            (None, {
                'fields': (
                    'sys_mon',
                    'object_name',
                    'object_status',
                    'owner_contragent',
                    'owner_user',
                    'contragent',
                    'imei',

                )
            }),
    )
    list_per_page = 20

    def get_device(self, obj):
        if Devices.objects.filter(device_imei=obj.imei).first():
            if obj.imei == Devices.objects.filter(device_imei=obj.imei).first().device_imei:
                return [
                        Devices.objects.filter(device_imei=obj.imei).first().device_serial,
                        Devices.objects.filter(device_imei=obj.imei).first().devices_brand,
                        ]
    def get_sim(self, obj):
        if SimCards.objects.filter(terminal_imei=obj.imei).first():
            if obj.imei == None:
                return "Сим не найден"
                
            if obj.imei == SimCards.objects.filter(terminal_imei=obj.imei).first().terminal_imei:
                return [SimCards.objects.filter(terminal_imei=obj.imei).first().sim_iccid,
                        SimCards.objects.filter(terminal_imei=obj.imei).first().sim_tel_number,
                        SimCards.objects.filter(
                            terminal_imei=obj.imei
                            ).first().sim_cell_operator.name
                        ]

    get_device.short_description = 'Терминал'
    get_sim.short_description = 'Симкарта'


class GlobalLogAdmin(admin.ModelAdmin):
    list_display = (
            "section_type",
            "get_obj_client",
            "field",
#            "old_value",
#            "new_value",
            "get_status_old",
            "get_status_new",
            "change_time",
            "sys_id",
            "action",
            )

    list_filter = (
            "section_type",
            "sys_id",
            "field",
            "change_time",
            "action",
            )
    search_fields = (
            "section_type",
            "edit_id",
            "field",
            "old_value",
            "new_value",
            "change_time",
            "sys_id",
            "action",
            )
    fieldsets = (
            (None, {
                'fields': (
                    'section_type',
                    'edit_id',
                    'field',
                    'old_value',
                    'new_value',
                    'change_time',
                    'sys_id',
                    'action',
                )
            }),
    )
    list_per_page = 20
    date_hierarchy = 'change_time'

    def get_obj_client(self, obj):
        if obj.section_type == 'object':
            if CaObjects.objects.filter(id=obj.edit_id).first():
                return CaObjects.objects.filter(id=obj.edit_id).first().owner_contragent

        if obj.section_type == '1С_client':
            if Contragents.objects.filter(ca_id=obj.edit_id).first():
                return Contragents.objects.filter(ca_id=obj.edit_id).first().ca_name

    def get_status_old(self, obj):
        if obj.section_type == 'object' and obj.field == 'object_status_id':
            if obj.old_value == "0":
                return 'Не было'
            if obj.old_value == "1":
                return 'Новый не на абонентке'
            if obj.old_value == "2":
                return 'Тестоввый не на абонентке'
            if obj.old_value == "3":
                return 'На абонентке'
            if obj.old_value == "4":
                return 'Ждёт перевода'
            if obj.old_value == "5":
                return 'Приостановлен'
            if obj.old_value == "6":
                return 'Переведённый в другую систему'
            if obj.old_value == "7":
                return 'Деактивирован'
            else:
                return obj.old_value
        else:
            return obj.old_value

    def get_status_new(self, obj):
        if obj.section_type == 'object' and obj.field == 'object_status_id':
            if obj.new_value == "0":
                return 'Не было'
            if obj.new_value == "1":
                return 'Новый не на абонентке'
            if obj.new_value == "2":
                return 'Тестоввый не на абонентке'
            if obj.new_value == "3":
                return 'На абонентке'
            if obj.new_value == "4":
                return 'Ждёт перевода'
            if obj.new_value == "5":
                return 'Приостановлен'
            if obj.new_value == "6":
                return 'Переведённый в другую систему'
            if obj.new_value == "7":
                return 'Деактивирован'
            else:
                return obj.new_value
        else:
            return obj.new_value

    get_obj_client.short_description = "Контрагент"
    get_status_old.short_description = "Старое значение"
    get_status_new.short_description = "Новое значение"




class SimCardsAdmin(admin.ModelAdmin):
    list_display = (
            "sim_iccid",
            "sim_tel_number",
            "sim_cell_operator",
            "sim_owner",
            "sim_date",
            "contragent",
            "terminal_imei",
            'itprogrammer',
            'get_device',

            )

    list_filter = (
            "sim_cell_operator",
            "sim_owner",
            "sim_date",
#            "contragent",
            'itprogrammer',

            )
    search_fields = (
            "sim_iccid",
            "sim_tel_number",
            "client_name",
            "sim_cell_operator__name",
            "sim_owner",
            "sim_date",
            "contragent__ca_name",
            "terminal_imei",
            )
    fieldsets = (
            (None, {
                'fields': (
                    'sim_iccid',
                    'sim_tel_number',
                    'client_name',
                    'sim_cell_operator',
                    'sim_owner',
                    'sim_date',
                    'contragent',
                    "terminal_imei",
                    'itprogrammer',
                )
            }),
    )
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': (
                    'sim_iccid',
                    'sim_tel_number',
#                    'client_name',
                    'sim_cell_operator',
                    'sim_owner',
                    'sim_date',
                    'contragent',
                    "terminal_imei",
                    'itprogrammer'

                )
            })
    )
    raw_id_fields = (
        'contragent',
    )
    list_per_page = 20
    date_hierarchy = 'sim_date'

    def get_device(self, obj):
        if Devices.objects.filter(device_imei=obj.terminal_imei).first():
            if obj.terminal_imei == Devices.objects.filter(device_imei=obj.terminal_imei).first().device_imei:
                return Devices.objects.filter(device_imei=obj.terminal_imei).first().device_serial

    get_device.short_description = 'Серийный номер устройства'
#    list_display_links = ('get_device',)

class DevicesAdmin(admin.ModelAdmin):
    list_display = (
            "device_serial",
            "device_imei",
            "client_name",
            "terminal_date",
            "devices_brand",
            "sys_mon",
            "contragent",
            'itprogrammer',
            'get_sim',
            )

    list_filter = (
            "devices_brand",
            "terminal_date",
            'itprogrammer',
            "devices_brand__devices_vendor",
            )
    search_fields = (
            "device_serial",
            "device_imei",
            "client_name",
            "name_it",
            "contragent__ca_name",

    )
    fieldsets = (
            (None, {
                'fields': (
                    'device_serial',
                    'device_imei',
                    'terminal_date',
                    'devices_brand',
                    'sys_mon',
                    'contragent',
                    'itprogrammer',
                )
            }),
    )
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': (
                    'device_serial',
                    'device_imei',
                    'terminal_date',
                    'devices_brand',
                    'sys_mon',
                    'contragent__ca_id',
                    'itprogrammer',
                )
            })

    )
    raw_id_fields = ['contragent']
    list_per_page = 20
    date_hierarchy = 'terminal_date'

    def get_sim(self, obj):
        if SimCards.objects.filter(terminal_imei=obj.device_imei).first():
            if obj.device_imei == SimCards.objects.filter(terminal_imei=obj.device_imei).first().terminal_imei:
                return SimCards.objects.filter(terminal_imei=obj.device_imei).first().sim_iccid

    get_sim.short_description = 'Симкарта на устройстве'
#    list_display_links = ('get_sim',)

admin.site.register(Contragents, ContragentsAdmin)
admin.site.register(LoginUsers, LoginUsersAdmin)
admin.site.register(GlobalLogging, GlobalLogAdmin)
admin.site.register(CaObjects, CaObjectsAdmin)
admin.site.register(SimCards, SimCardsAdmin)
admin.site.register(Devices, DevicesAdmin)
