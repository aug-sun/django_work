import environ
from pathlib import Path
import os
import requests

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


URL_ATS = env("URL_ATS")
TOKEN_ATS = env("TOKEN_ATS")


def get_accouns():
    url = URL_ATS
    payload = {
        "cmd": "accounts",
        "token": TOKEN_ATS
    }

    response = requests.post(url, headers={}, json=payload)

    if response.status_code == 200:
        print("ОК")
        print(response.json())
    else:
        print(f"Ошибка {response.status_code}: {response.text}")

def get_history(start, end):

    url = URL_ATS
    payload = {
        "cmd": "history",
        "token": TOKEN_ATS,
        "start": str(start),
        "end": str(end),
    }

    response = requests.post(url, headers={}, json=payload)

    if response.status_code == 200:
        print("ОК")
        print(response.json())
    else:
        print(f"Ошибка {response.status_code}: {response.text}")

