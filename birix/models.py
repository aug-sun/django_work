# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CellOperator(models.Model):
    name = models.CharField(max_length=60, db_comment='Имя сотового оператора')
    ca_price = models.IntegerField(blank=True, null=True, db_comment='цена для клиентов')
    sun_price = models.IntegerField(blank=True, null=True, db_comment='Цена для Сантел')

    class Meta:
        managed = False
        db_table = 'Cell_operator'

    def __str__(self):
        return self.name


class Contragents(models.Model):
    ca_id = models.AutoField(primary_key=True)
    ca_holding = models.ForeignKey('Holdings', models.DO_NOTHING, blank=True, null=True, db_comment='ID холдинга')
    ca_name = models.CharField(max_length=255, blank=True, null=True, db_comment='Название контрагента')
    ca_shortname = models.CharField(max_length=250, blank=True, null=True)
    ca_inn = models.CharField(max_length=60, blank=True, null=True, db_comment='ИНН контрагента')
    ca_kpp = models.CharField(max_length=60, blank=True, null=True, db_comment='КПП контрагента')
    ca_bill_account_num = models.CharField(max_length=60, blank=True, null=True, db_comment='Расчетный счет')
    ca_bill_account_bank_name = models.CharField(max_length=60, blank=True, null=True, db_comment='Наименование банка')
    ca_bill_account_ogrn = models.CharField(max_length=60, blank=True, null=True, db_comment='ОГРН')
    ca_edo_connect = models.IntegerField(blank=True, null=True, db_comment='Обмен ЭДО')
    ca_field_of_activity = models.CharField(max_length=260, blank=True, null=True, db_comment='Сфера деятельности')
    ca_type = models.CharField(max_length=60, blank=True, null=True, db_comment='тип компании')
    unique_onec_id = models.CharField(max_length=100, blank=True, null=True, db_comment='уникальный id в 1С контрагента ')
    registration_date = models.DateField(blank=True, null=True, db_comment='Дата регистрации в 1С')
    key_manager = models.CharField(max_length=200, blank=True, null=True, db_comment='Основной менеджер ')
    actual_address = models.CharField(max_length=300, blank=True, null=True, db_comment='Фактический адрес ')
    registered_office = models.CharField(max_length=300, blank=True, null=True, db_comment='Юридический адрес ')
    phone = models.CharField(max_length=200, blank=True, null=True, db_comment='Телефон ')

    class Meta:
        managed = False
        db_table = 'Contragents'

    def __str__(self):
        return self.ca_name


class LoginUsers(models.Model):
    client_name = models.CharField(max_length=200, blank=True, null=True)
    login = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=60, blank=True, null=True)
    date_create = models.DateField(blank=True, null=True)
    system = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True)
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    comment_field = models.CharField(max_length=270, blank=True, null=True, db_comment='Поле с комментариями')
    ca_uid = models.CharField(max_length=100, blank=True, null=True, db_comment='Уникальный id контрагента')

    class Meta:
        managed = False
        db_table = 'Login_users'

    def __str__(self):
        return self.login


class CaContacts(models.Model):
    ca_contact_id = models.AutoField(primary_key=True)
    ca = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='id компании')
    ca_contact_name = models.CharField(max_length=255, blank=True, null=True, db_comment='Имя контактного лица')
    ca_contact_surname = models.CharField(max_length=255, blank=True, null=True, db_comment='Фамилия контактного лица')
    ca_contact_middlename = models.CharField(max_length=255, blank=True, null=True, db_comment='Отчество контактного лица')
    ca_contact_cell_num = models.CharField(max_length=255, blank=True, null=True, db_comment='Сотовый телефон контакт. лица')
    ca_contact_work_num = models.CharField(max_length=255, blank=True, null=True, db_comment='Рабочий телефон к.л.')
    ca_contact_email = models.CharField(max_length=255, blank=True, null=True, db_comment='Электр.почт. к.л')
    ca_contact_position = models.CharField(max_length=255, blank=True, null=True, db_comment='Должность к.л.')

    class Meta:
        managed = False
        db_table = 'ca_contacts'

    def __str__(self):
        return self.ca_contact_name


class CaContracts(models.Model):
    contract_id = models.AutoField(primary_key=True)
    ca = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    contract_type = models.CharField(max_length=50, blank=True, null=True, db_comment='Тип договора')
    contract_num_prefix = models.CharField(max_length=50, blank=True, null=True, db_comment='Префикс номера договора')
    contract_num = models.CharField(max_length=50, blank=True, null=True, db_comment='Номер договора')
    contract_payment_term = models.CharField(max_length=50, blank=True, null=True, db_comment='условия оплаты')
    contract_payment_period = models.CharField(max_length=50, blank=True, null=True, db_comment='Период оплаты')
    contract_start_date = models.DateField(blank=True, null=True, db_comment='Дата заключения договора')
    contract_expired_date = models.DateField(blank=True, null=True, db_comment='Дата завершения договора')

    class Meta:
        managed = False
        db_table = 'ca_contracts'


class CaObjects(models.Model):
    sys_mon = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True, db_comment='ID системы мониторинга')
    sys_mon_object_id = models.CharField(max_length=50, blank=True, null=True, db_comment='ID объекта в системе мониторинга')
    object_name = models.CharField(max_length=70, blank=True, null=True, db_comment='Название объекта')
    object_status = models.ForeignKey('ObjectStatuses', models.DO_NOTHING, db_column='object_status', blank=True, null=True, db_comment='Статус объекта ссылается к статусам')
    object_add_date = models.DateTimeField(blank=True, null=True, db_comment='Дата добавления объекта')
    object_last_message = models.DateTimeField(blank=True, null=True, db_comment='Дата последнего сообщения')
    object_margin = models.IntegerField(blank=True, null=True, db_comment='Надбавка к базовой цене объекта')
    owner_contragent = models.CharField(max_length=200, blank=True, null=True, db_comment='Хозяин контрагент')
    owner_user = models.CharField(max_length=255, blank=True, null=True, db_comment='Хозяин юзер')
    imei = models.CharField(max_length=100, blank=True, null=True, db_comment='идентификатор терминала')
    updated = models.DateTimeField(blank=True, null=True, db_comment='Когда изменён')
    object_created = models.DateTimeField(blank=True, null=True, db_comment='Дата создания в системе мониторинга ')
    parent_id_sys = models.CharField(max_length=200, blank=True, null=True, db_comment='Id клиента в системе мониторинга')
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True)
    ca_uid = models.CharField(max_length=100, blank=True, null=True, db_comment='Уникальный id контрагента')

    class Meta:
        managed = False
        db_table = 'ca_objects'

    def __str__(self):
        return self.object_name


class ClientsInSystemMonitor(models.Model):
    id_in_system_monitor = models.CharField(max_length=200, blank=True, null=True, db_comment='Id клиента в системе мониторинга')
    name_in_system_monitor = models.CharField(max_length=200, blank=True, null=True, db_comment='Имя клиента в системе мониторинга ')
    owner_id_sys_mon = models.CharField(max_length=200, blank=True, null=True, db_comment='Id хозяина в системе мониторинга')
    system_monitor = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True, db_comment='Id системы мониторинга ')
    client = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='id клиента')

    class Meta:
        managed = False
        db_table = 'clients_in_system_monitor'


class Devices(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_serial = models.CharField(max_length=100, blank=True, null=True, db_comment='Серийный номер устройства')
    device_imei = models.CharField(max_length=60, blank=True, null=True, db_comment='IMEI устройства')
    client_name = models.CharField(max_length=300, blank=True, null=True, db_comment='Имя клиента')
    terminal_date = models.DateTimeField(blank=True, null=True, db_comment='Дата программирования терминала')
    devices_brand = models.ForeignKey('DevicesBrands', models.DO_NOTHING, blank=True, null=True, db_comment='ID Модели устройства ')
    name_it = models.CharField(max_length=15, blank=True, null=True, db_comment='Имя програмировавшего терминал')
    sys_mon = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True, db_comment='ID системы мониторинга')
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    coment = models.CharField(max_length=270, blank=True, null=True, db_comment='Коментарии')

    class Meta:
        managed = False
        db_table = 'devices'

    def __str__(self):
        return self.device_serial


class DevicesBrands(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    devices_vendor = models.ForeignKey('DevicesVendor', models.DO_NOTHING, blank=True, null=True, db_comment='Id Вендора терминалов')

    class Meta:
        managed = False
        db_table = 'devices_brands'

    def __str__(self):
        return self.name


class DevicesCommands(models.Model):
    command = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices_commands'


class DevicesVendor(models.Model):
    vendor_name = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices_vendor'

    def __str__(self):
        return self.vendor_name


class GlobalLogging(models.Model):
    section_type = models.CharField(max_length=50)
    edit_id = models.IntegerField()
    field = models.CharField(max_length=50)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)
    change_time = models.DateTimeField(blank=True, null=True)
    sys_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_logging'

    def __str__(self):
        return self.section_type


class GuaranteeTerms(models.Model):
    gt_id = models.AutoField(primary_key=True, db_comment='ID гарантийного срока')
    gt_term = models.IntegerField(blank=True, null=True, db_comment='Срок гарантии (дней)')
    gt_type = models.CharField(max_length=255, blank=True, null=True, db_comment='Тип гарантии')

    class Meta:
        managed = False
        db_table = 'guarantee_terms'


class Holdings(models.Model):
    holding_id = models.AutoField(primary_key=True)
    holding_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'holdings'


class MonitoringSystem(models.Model):
    mon_sys_id = models.AutoField(primary_key=True)
    mon_sys_name = models.CharField(max_length=60, blank=True, null=True, db_comment='Название системы мониторинга')
    mon_sys_obj_price_suntel = models.IntegerField(blank=True, null=True, db_comment='Стоимость объекта для Сантел')
    mon_sys_ca_obj_price_default = models.IntegerField(blank=True, null=True, db_comment='Базовая стоимость объекта для Контрагента')

    class Meta:
        managed = False
        db_table = 'monitoring_system'

    def __str__(self):
        return self.mon_sys_name


class ObjectRetranslators(models.Model):
    retranslator_id = models.AutoField(primary_key=True)
    retranslator_name = models.CharField(max_length=50, blank=True, null=True)
    retranslator_suntel_price = models.IntegerField(blank=True, null=True)
    retranslator_ca_price = models.IntegerField(blank=True, null=True)
    retr_object = models.ForeignKey(CaObjects, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'object_retranslators'


class ObjectSensors(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    sensor_object = models.ForeignKey(CaObjects, models.DO_NOTHING, blank=True, null=True, db_comment='На каком объекте стоит по ID объекта')
    sensor_name = models.CharField(max_length=255, blank=True, null=True, db_comment='Имя датчика в СМ')
    sensor_type = models.CharField(max_length=255, blank=True, null=True, db_comment='Тип датчика(ДУТ, Температуры, наклона)')
    sensor_vendor = models.CharField(max_length=255, blank=True, null=True, db_comment='производитель')
    sensor_vendor_model = models.CharField(max_length=255, blank=True, null=True, db_comment='Модель датчика')
    sensor_serial = models.CharField(max_length=255, blank=True, null=True, db_comment='Серийный номер датчика')
    sensor_mac_address = models.CharField(max_length=255, blank=True, null=True, db_comment='Мак адрес датчика')
    sensor_technology = models.CharField(max_length=255, blank=True, null=True, db_comment='Подтип датчика(аналоговый, цифровой, частотный)')
    sensor_connect_type = models.CharField(max_length=255, blank=True, null=True, db_comment='Тип подключения')

    class Meta:
        managed = False
        db_table = 'object_sensors'


class ObjectStatuses(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    abon_bool = models.IntegerField(db_comment='На абонентке или нет')

    class Meta:
        managed = False
        db_table = 'object_statuses'

    def __str__(self):
        return self.status


class ObjectVehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_object = models.ForeignKey(CaObjects, models.DO_NOTHING, blank=True, null=True)
    vehicle_ca = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True)
    vehicle_vendor_name = models.CharField(max_length=255, blank=True, null=True)
    vehicle_vendor_model = models.CharField(max_length=255, blank=True, null=True)
    vehicle_year_of_manufacture = models.CharField(max_length=255, blank=True, null=True)
    vehicle_gos_nomer = models.CharField(max_length=255, blank=True, null=True)
    vehicle_gos_nomer_region = models.CharField(max_length=255, blank=True, null=True)
    vehicle_type = models.CharField(max_length=255, blank=True, null=True)
    vehicle_vin = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'object_vehicles'


class SimCards(models.Model):
    sim_id = models.AutoField(primary_key=True)
    sim_iccid = models.CharField(max_length=40, blank=True, null=True, db_comment='ICCID')
    sim_tel_number = models.CharField(max_length=40, blank=True, null=True, db_comment='телефонный номер сим')
    client_name = models.CharField(max_length=270, blank=True, null=True, db_comment='Имя клиента')
    sim_cell_operator = models.ForeignKey(CellOperator, models.DO_NOTHING, db_column='sim_cell_operator', blank=True, null=True, db_comment='Сотовый оператор(надо по ID)')
    sim_owner = models.IntegerField(blank=True, null=True, db_comment='Владелец сим (мы или клиент)')
    sim_device = models.ForeignKey(Devices, models.DO_NOTHING, blank=True, null=True, db_comment='ID к девайсам(devices)')
    sim_date = models.DateTimeField(blank=True, null=True, db_comment='Дата регистрации сим')
    name_it = models.CharField(max_length=100, blank=True, null=True, db_comment='Имя активировавшего')
    status = models.IntegerField(blank=True, null=True, db_comment='Активность симки')
    terminal_imei = models.CharField(max_length=25, blank=True, null=True, db_comment='IMEI терминала в который вставлена симка')
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    ca_uid = models.CharField(max_length=100, blank=True, null=True, db_comment='Уникальный id контрагента')

    class Meta:
        managed = False
        db_table = 'sim_cards'

    def __str__(self):
        return self.sim_iccid
