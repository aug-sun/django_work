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
        verbose_name = 'Сотовый оператор'
        verbose_name_plural = 'Сотовые операторы'

    def __str__(self):
        return self.name

class Contragents(models.Model):
    ca_id = models.AutoField(primary_key=True)
    ca_holding = models.ForeignKey(
            'Holdings', 
            models.DO_NOTHING, 
            blank=True, null=True, 
            db_comment='ID холдинга',
            verbose_name='Холдинг',
            )
    ca_name = models.CharField(
            max_length=255, 
            blank=True,
            null=True, 
            db_comment='Название контрагента',
            verbose_name='Название',
            )
    ca_shortname = models.CharField(
            max_length=250, 
            blank=True, 
            null=True,
            verbose_name='Короткое название',
            )
    ca_inn = models.CharField(
            max_length=60,
            blank=True,
            null=True, 
            db_comment='ИНН контрагента',
            verbose_name='ИНН',
            )
    ca_kpp = models.CharField(
            max_length=60,
            blank=True,
            null=True,
            db_comment='КПП контрагента',
            verbose_name='КПП',
            )
    ca_bill_account_num = models.CharField(
            max_length=60, 
            blank=True,
            null=True, 
            db_comment='Расчетный счет',
            verbose_name='Расчетный счет',
            )
    ca_bill_account_bank_name = models.CharField(
            max_length=60,
            blank=True, 
            null=True,
            db_comment='Наименование банка',
            verbose_name='Наименование банка',
            )
    ca_bill_account_ogrn = models.CharField(
            max_length=60, 
            blank=True,
            null=True,
            db_comment='ОГРН',
            verbose_name='ОГРН',
            )
    ca_edo_connect = models.IntegerField(
            blank=True, 
            null=True,
            db_comment='Обмен ЭДО',
            verbose_name='Обмен ЭДО',
            )
    ca_field_of_activity = models.CharField(
            max_length=260,
            blank=True,
            null=True, 
            db_comment='Сфера деятельности',
            verbose_name='Сфера деятельности',
            )
    ca_type = models.CharField(
            max_length=60, 
            blank=True, 
            null=True, 
            db_comment='тип компании',
            verbose_name='Тип',
            )
    unique_onec_id = models.CharField(
            max_length=100, 
            blank=True, 
            null=True,
            db_comment='уникальный id в 1С контрагента ',
            verbose_name='Уникальный id в 1С',
            )
    registration_date = models.DateField(
            blank=True,
            null=True, 
            db_comment='Дата регистрации в 1С',
            verbose_name='Дата регистрации',
            )
    key_manager = models.CharField(
            max_length=200, 
            blank=True,
            null=True, 
            db_comment='Основной менеджер ',
            verbose_name='Основной менеджер',
            )
    actual_address = models.CharField(
            max_length=300, 
            blank=True,
            null=True, 
            db_comment='Фактический адрес ',
            verbose_name='Фактический адрес',
            )
    registered_office = models.CharField(
            max_length=300, 
            blank=True, 
            null=True, 
            db_comment='Юридический адрес ',
            verbose_name='Юридический адрес',
            )
    phone = models.CharField(
            max_length=200,
            blank=True, 
            null=True,
            db_comment='Телефон ',
            verbose_name='Телефон',
            )

    class Meta:
        managed = False
        db_table = 'Contragents'
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

    def __str__(self):
        return self.ca_name

class LoginUsers(models.Model):
    class StatusChoices(models.IntegerChoices):
        if_active = 1, 'Не подверждена но активирована'
        inactive = 0, "Заблокирована"
        verified = 2, 'Подверждена и активирована'

    client_name = models.CharField(
            max_length=200, 
            blank=True,
            null=True,
            verbose_name='Название клиента',
            )
    login = models.CharField(
            max_length=60,
            blank=True, 
            null=False,
            verbose_name='Логин',
            )
    email = models.CharField(
            max_length=60, 
            blank=True, 
            null=True,
            )
    password = models.CharField(
            max_length=60,
            blank=True, 
            null=False,
            verbose_name='Пароль',
            )
    date_create = models.DateField(
            blank=True,
            null=False,
            verbose_name='Дата создания',
            )
    system = models.ForeignKey(
            'MonitoringSystem',
            models.DO_NOTHING, 
            blank=True,
            null=False,
            verbose_name='Система мониторинга',
            )
    contragent = models.ForeignKey(
            Contragents, 
            models.DO_NOTHING, 
            blank=True, 
            null=False, 
            db_comment='ID контрагента',
            verbose_name='Контрагент как в 1С',
            )
    comment_field = models.CharField(
            max_length=270, 
            blank=True, 
            null=True,
            db_comment='Поле с комментариями',
            verbose_name='Комментарии',
            )
    ca_uid = models.CharField(
            max_length=100,
            blank=True,
            null=True, 
            db_comment='Уникальный id контрагента',
            verbose_name='Уникальный id контрагента',
            )
    account_status = models.SmallIntegerField(
            blank=True,
            null=False,
            db_comment='Статус аккаунта',
            verbose_name='Статус аккаунта',
            choices=StatusChoices.choices,
            )


    class Meta:
        managed = False
        db_table = 'Login_users'
        verbose_name = 'Логин пользователя'
        verbose_name_plural = 'Логины пользователей'


    def __str__(self):
        return self.login

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CaContacts(models.Model):
    class PositionChoices(models.TextChoices):
        DIRECTOR = 'Директор', 'Директор'
        MANAGER = 'Менеджер', 'Менеджер'
        ACCOUNTANT = 'Бухгалтер', 'Бухгалтер'
        MONTAGER = 'Монтажник', 'Монтажник'
        IT_TECH = 'IT_специалист', 'IT_специалист'
        DISPETCHER = 'Диспетчер', 'Диспетчер'
        DRIVER = 'Водитель', 'Водитель'
        TECH_SUPPORT = 'Техподдержка', 'Техподдержка'



    ca_contact_id = models.AutoField(primary_key=True)
    ca = models.ForeignKey(
            Contragents,
            models.DO_NOTHING, 
            blank=True,
            null=True,
            db_comment='id компании',
            verbose_name='Компания как в 1С',
            )
    ca_contact_name = models.CharField(
            max_length=255,
            blank=True,
            null=True,
            db_comment='Имя контактного лица',
            verbose_name='Имя контактного лица',
            )
    ca_contact_surname = models.CharField(
            max_length=255, 
            blank=True, 
            null=True, 
            db_comment='Фамилия контактного лица',
            verbose_name='Фамилия контактного лица',
            )
    ca_contact_middlename = models.CharField(
            max_length=255, 
            blank=True, 
            null=True, 
            db_comment='Отчество контактного лица',
            verbose_name='Отчество контактного лица',
            )
    ca_contact_cell_num = models.CharField(
            max_length=255,
            blank=True,
            null=True,
            db_comment='Сотовый телефон контакт. лица',
            unique=True,
            verbose_name='Сотовый телефон контакт. лица',
            )
    ca_contact_work_num = models.CharField(
            max_length=255, 
            blank=True,
            null=True,
            db_comment='Рабочий телефон к.л.',
            verbose_name='Рабочий телефон к.л.',
            )
    ca_contact_email = models.CharField(
            max_length=255,
            blank=True,
            null=True,
            db_comment='Электр.почт. к.л',
            verbose_name='Электр.почт. к.л',
            )
    ca_contact_position = models.CharField(
            max_length=255,
            blank=True, 
            null=True,
            db_comment='Должность к.л.',
            verbose_name='Должность к.л.',
            choices=PositionChoices.choices,
            )

    class Meta:
        managed = False
        db_table = 'ca_contacts'
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

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
    sys_mon = models.ForeignKey(
            'MonitoringSystem', 
            models.DO_NOTHING, 
            blank=True,
            null=True,
            db_comment='ID системы мониторинга',
            verbose_name='Система мониторинга',
            )
    sys_mon_object_id = models.CharField(max_length=50, blank=True, null=True, db_comment='ID объекта в системе мониторинга')
    object_name = models.CharField(
            max_length=70,
            blank=True,
            null=True,
            db_comment='Название объекта',
            verbose_name='Название объекта',
            )
    object_status = models.ForeignKey(
            'ObjectStatuses',
            models.DO_NOTHING, 
            db_column='object_status',
            blank=True,
            null=True,
            db_comment='Статус объекта ссылается к статусам',
            verbose_name='Статус объекта',
            )
    object_add_date = models.DateTimeField(blank=True, null=True, db_comment='Дата добавления объекта')
    object_last_message = models.DateTimeField(
            blank=True,
            null=True,
            db_comment='Дата последнего сообщения',
            verbose_name='Дата последнего сообщения',
            )
    object_margin = models.IntegerField(blank=True, null=True, db_comment='Надбавка к базовой цене объекта')
    owner_contragent = models.CharField(
            max_length=200, 
            blank=True, 
            null=True, 
            db_comment='Хозяин контрагент',
            verbose_name='Контрагент в системе мониторинга',
            )
    owner_user = models.CharField(
            max_length=255,
            blank=True, 
            null=True, 
            db_comment='Хозяин юзер',
            verbose_name='Логин юзера в системе мониторинга',
            )
    imei = models.CharField(
            max_length=100, 
            blank=True, 
            null=True, 
            db_comment='идентификатор терминала',
            verbose_name='IMEI терминала',
            )
    updated = models.DateTimeField(blank=True, null=True, db_comment='Когда изменён')
    object_created = models.DateTimeField(blank=True, null=True, db_comment='Дата создания в системе мониторинга ')
    parent_id_sys = models.CharField(max_length=200, blank=True, null=True, db_comment='Id клиента в системе мониторинга')
    contragent = models.ForeignKey(
            Contragents, 
            models.DO_NOTHING, 
            blank=True, 
            null=True,
            verbose_name='Контрагент как в 1С',
            )
    ca_uid = models.CharField(max_length=100, blank=True, null=True, db_comment='Уникальный id контрагента')

    class Meta:
        managed = False
        db_table = 'ca_objects'
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


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
    device_serial = models.CharField(
            max_length=100,
            blank=False, 
            null=True, 
            db_comment='Серийный номер устройства',
            verbose_name='Серийный номер устройства'
            )
    device_imei = models.CharField(
            max_length=60, 
            blank=False,
            null=True, 
            db_comment='IMEI устройства',
            verbose_name='IMEI устройства'
            )
    client_name = models.CharField(
            max_length=300,
            blank=True,
            null=True,
            db_comment='Имя клиента',
            verbose_name='Имя клиента'
            )
    terminal_date = models.DateTimeField(
            blank=False,
            null=True, 
            db_comment='Дата программирования терминала',
            verbose_name='Дата программирования терминала',
            )
    devices_brand = models.ForeignKey(
            'DevicesBrands', 
            models.DO_NOTHING,
            blank=False, 
            null=True, 
            db_comment='ID Модели устройства ',
            verbose_name='Модель устройства '
            )
    name_it = models.CharField(
            max_length=50, 
            blank=True,
            null=True, 
            db_comment='Имя програмировавшего терминал',
            verbose_name='Имя програмировавшего терминал',
            )
    sys_mon = models.ForeignKey(
            'MonitoringSystem',
            models.DO_NOTHING,
            blank=False,
            null=True, 
            db_comment='ID системы мониторинга',
            verbose_name='Система мониторинга',
            )
    contragent = models.ForeignKey(
            Contragents, 
            models.DO_NOTHING,
            blank=False,
            null=True, 
            db_comment='ID контрагента',
            verbose_name='Контрагент',
            )
    coment = models.CharField(
            max_length=270,
            blank=True,
            null=True, 
            db_comment='Коментарии',
            verbose_name='Коментарии',
            )
    itprogrammer = models.ForeignKey(
            AuthUser, 
            models.DO_NOTHING, 
            blank=False, 
            null=True,
            verbose_name='Программист',
            )

    class Meta:
        managed = False
        db_table = 'devices'
        verbose_name = 'Терминал'
        verbose_name_plural = 'Терминалы'


    def __str__(self):
        return self.device_serial

class DevicesBrands(models.Model):
    name = models.CharField(
            max_length=200, 
            blank=True, 
            null=True,
            verbose_name='Модель устройства',
            )
    devices_vendor = models.ForeignKey(
            'DevicesVendor', 
            models.DO_NOTHING, 
            blank=True, 
            null=True,
            db_comment='Id Вендора терминалов',
            verbose_name='Фирма',
            )

    class Meta:
        managed = False
        db_table = 'devices_brands'
        verbose_name = 'Модель устройства'
        verbose_name_plural = 'Модели устройств'

    def __str__(self):
        return self.name

class DevicesCommands(models.Model):

    class Methods(models.TextChoices):
        SMS = 'SMS'
        TCP = 'TCP'
        ANY = 'Любой'

    command = models.CharField(max_length=100, blank=True, null=True)
    device_brand = models.ForeignKey(
            DevicesBrands,
            models.RESTRICT,
            blank=True, 
            null=True,
            db_comment='Id Модели устройства',
            verbose_name='Модель устройства',
            db_column='device_brand'
            )
    method = models.CharField(
            max_length=10, 
            blank=True, 
            null=True,
            choices=Methods.choices,
            verbose_name='Метод отправки',
            )
    description = models.CharField(
            max_length=300,
            blank=True,
            null=True,
            verbose_name='Описание',
    )


    class Meta:
        managed = False
        db_table = 'devices_commands'
        verbose_name = 'Команда терминала'
        verbose_name_plural = 'Команды терминалов'

    def __str__(self):
        return self.command





class DevicesVendor(models.Model):
    vendor_name = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices_vendor'

    def __str__(self):
        return self.vendor_name

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GlobalLogging(models.Model):
    class SysChoices(models.IntegerChoices):
        glonass = 1, "Glonasssoft"
        fort = 2, "Fort monitor"
        wialonhost = 3, "Wialon hosting"
        wialonlocal = 4, "Wialon local"
        era = 5, "Era"
        scout = 6, "Scout"
        null = 0, "В 1с"

    class ActionChoices(models.TextChoices):
        create = "add", "Создание"
        update = "update", "Изменение"
        delete = "delete", "Удаление"

    class ValuesChoices(models.TextChoices):
        no_name = "0", "Небыло такого"
        new = "1", "Новый не на абонентке"
        test = "2", "Тесовый не на абонентке"
        abon = "3", "На абонентке с госномером"
        vait_abon = "4", "Ждёт перевода не на абонентке"
        stop_abon = "5", "Приостановлен не на абонентке"
        perev = "6", "Переведенный не на абонентке"
        deact = "7", "Деактивирован"



    section_type = models.CharField(
            max_length=50,
            verbose_name='Тип секции',
            )
    edit_id = models.IntegerField()
    field = models.CharField(
            max_length=50,
            verbose_name='Поле',
            )
    old_value = models.CharField(
            max_length=255, 
            blank=True,
            null=True,
            verbose_name='Старое значение',
            )
    new_value = models.CharField(
            max_length=255, 
            blank=True,
            null=True,
            verbose_name='Новое значение',
            )
    change_time = models.DateTimeField(
            blank=True, 
            null=True,
            verbose_name='Время изменения',
            )
    sys_id = models.IntegerField(
            blank=True,
            null=True,
            verbose_name='ID системы',
            choices=SysChoices.choices
            )
    action = models.CharField(
            max_length=100, 
            blank=True, 
            null=True, 
            choices=ActionChoices.choices,
            verbose_name='Действие',
            )

    class Meta:
        managed = False
        db_table = 'global_logging'
        verbose_name = 'Лог изменений'
        verbose_name_plural = 'Логи изменений'

    def __str__(self):
        return self.section_type

    #если sys_id = 1 - система мониторинга
    def get_sys_name(self):
        if self.sys_id == 1:
            return 'Глонасс'
        if self.sys_id == 2:
            return 'Форт'
        if self.sys_id == 3:
            return 'ВиалонХост'
        if self.sys_id == 4:
            return 'ВиалонЛокал'
        if self.sys_id == 5:
            return 'Эра'
        if self.sys_id == 6:
            return 'Скаут'
        else:
            return 'Изменения в 1С'

    def get_action(self):
        if self.action == 'update':
            return 'Изменено'
        if self.action == 'add':
            return 'Добавлено'
        if self.action == 'delete':
            return 'Удалено'


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
    mon_sys_name = models.CharField(
            max_length=60,
            blank=True,
            null=True,
            db_comment='Название системы мониторинга',
            verbose_name='Название системы мониторинга',
            )
    mon_sys_obj_price_suntel = models.IntegerField(
            blank=True,
            null=True,
            db_comment='Стоимость объекта для Сантел',
            verbose_name='Стоимость объекта для Сантел',
            )
    mon_sys_ca_obj_price_default = models.IntegerField(
            blank=True,
            null=True,
            db_comment='Базовая стоимость объекта для Контрагента',
            verbose_name='Базовая стоимость объекта для Контрагента',
            )

    class Meta:
        managed = False
        db_table = 'monitoring_system'
        verbose_name = 'Система мониторинга'
        verbose_name_plural = 'Системы мониторинга'

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
    status = models.CharField(
            max_length=50,
            blank=True,
            null=True,
            verbose_name='Статус',
            )
    abon_bool = models.IntegerField(db_comment='На абонентке или нет')

    class Meta:
        managed = False
        db_table = 'object_statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

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
    class Owner(models.IntegerChoices):
        ME = 1, 'Мы'
        CLIENT = 0, 'Клиент'
    class Status(models.IntegerChoices):
        ACTIVE = 1, 'Активна'
        DELETE = 0, 'Списана'
        STOP = 2, 'Приостановлена'

    sim_id = models.AutoField(primary_key=True)
    sim_iccid = models.CharField(
            max_length=40, 
            blank=True,
            null=True, 
            db_comment='ICCID',
            verbose_name='ICCID'
            )
    sim_tel_number = models.CharField(
            max_length=40, 
            blank=True, 
            null=True, 
            db_comment='телефонный номер сим',
            verbose_name='Телефонный номер сим'
            )
    client_name = models.CharField(
            max_length=270, 
            blank=True,
            null=True, 
            db_comment='Имя клиента',
            verbose_name='Имя клиента'
            )
    sim_cell_operator = models.ForeignKey(
            CellOperator, 
            models.DO_NOTHING,
            db_column='sim_cell_operator',
            blank=True,
            null=True,
            db_comment='Сотовый оператор(надо по ID)',
            verbose_name='Сотовый оператор'
            )
    sim_owner = models.IntegerField(
            blank=True,
            null=True,
            db_comment='Владелец сим (мы или клиент)',
            verbose_name='Мы или клиент',
            choices=Owner.choices
            )
    sim_device = models.ForeignKey(Devices, models.DO_NOTHING, blank=True, null=True, db_comment='ID к девайсам(devices)')
    sim_date = models.DateTimeField(
            blank=True, 
            null=True, 
            db_comment='Дата регистрации сим',
            verbose_name='Дата регистрации сим',
            )
    status = models.IntegerField(
            blank=True,
            null=True, 
            db_comment='Активность симки',
            verbose_name='Активность симки',
            choices=Status.choices
            )
    terminal_imei = models.CharField(
            max_length=25, 
            blank=True,
            null=True,
            db_comment='IMEI терминала в который вставлена симка',
            verbose_name='IMEI терминала в котором симка',
            )
    contragent = models.ForeignKey(
            Contragents, 
            models.DO_NOTHING, 
            blank=True,
            null=True, 
            db_comment='ID контрагента',
            verbose_name='Контрагент в 1С',
            )
    ca_uid = models.CharField(max_length=100, blank=True, null=True, db_comment='Уникальный id контрагента')
    itprogrammer = models.ForeignKey(
            AuthUser, 
            models.DO_NOTHING, 
            blank=True,
            null=True, 
            db_comment='ID сотрудника програмировавшего терминал',
            verbose_name='Сотрудник активировавший СИМ',
            )

    class Meta:
        managed = False
        db_table = 'sim_cards'
        verbose_name = 'Симкарта'
        verbose_name_plural = 'Симкарты'

    def __str__(self):
        return self.sim_iccid
