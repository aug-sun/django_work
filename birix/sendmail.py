from django.core.mail import send_mail

def sendmail(email, username, password, client_name, system_url, proger):
    # Заголовок письма
    subject = f'Данные для входа в систему мониторинга для {client_name}'
    # Текст письма
    message = f'Учётную запись создал: {proger}\nЛогин: {username}\nПароль: {password}\nСсылка на систему мониторинга: {system_url}\nПисьмо отправлено автоматически.'
    # Отправитель
    from_email = 'y.kuftov@suntel-nn.ru'
    # Получатель
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
