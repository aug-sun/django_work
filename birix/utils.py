import environ
from pathlib import Path
import os
import requests
from datetime import datetime

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
        return response.json()
    else:
        return []

def get_history(start, end):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    utc_start = start_date.strftime("%Y%m%d")+"T00"+"00"+"01"+"Z"

    end_date = datetime.strptime(end, "%Y-%m-%d")
    utc_end = end_date.strftime("%Y%m%d")+"T23"+"59"+"59"+"Z"

    url = URL_ATS
    payload = {
        "cmd": "history",
        "token": TOKEN_ATS,
        "start": str(utc_start),
        "end": str(utc_end),
    }

    response = requests.post(url, headers={}, json=payload)

    if response.status_code == 200:
        result = str(response.text).split("\n")
        return result

    else:
        return []


