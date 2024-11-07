from django.core.mail import send_mail

def sendmailmanager(email, username, password, client_name, system_url, proger):
    # Заголовок письма
    subject = f'Данные для входа в систему мониторинга для {client_name}'
    # Текст письма
    message = f'Учётную запись создал: {proger}\nЛогин: {username}\nПароль: {password}\nСсылка на систему мониторинга: {system_url}\nПисьмо отправлено автоматически.'
    # Отправитель
    from_email = 'y.kuftov@suntel-nn.ru'
    # Получатель
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

def sendmailclient(email, username, password, mon_system, system_url):
    # Заголовок письма
    subject = f'Данные для входа в систему мониторинга {mon_system}'
    # Текст письма
    message = f'Для вашей учётной записи были обновлены данные для входа:\nЛогин: {username}\nПароль: {password}\nСсылка на систему мониторинга: {system_url}\n\nПисьмо отправлено автоматически.\nТелефон для справки: 8 (831) 218-03-16'
    # Отправитель
    from_email = 'y.kuftov@suntel-nn.ru'
    # Получатель
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
