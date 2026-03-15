# это пока затычка


import requests


BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

CHAT_ID = "YOUR_CHAT_ID"


def send_notification(text: str):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url, json=payload)