# CMS на Django для работы с БД MySQL suntel

## Неоходимые предварительные установки
* Docker
* Docker Compose
* Curl
* Neovim

## Запуск

### Самостоятельным контейнером
1. Контейнер докера: `jagernau/django_monitoring_cms:latest`
    * Как его запустить: `sudo docker run -d -p 8000:8000 --env-file .env jagernau/django_monitoring_cms:latest manage.py runserver 0.0.0.0:8000`

### Скриптом
Запустить скрипт `curl -s https://raw.githubusercontent.com/Jagernau/django_work/exp/django_app_install.sh | sh`
