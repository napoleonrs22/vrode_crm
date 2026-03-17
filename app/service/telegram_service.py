import asyncio
import requests

from app.config import settings


def _send_notification_sync(text: str) -> None:
    if not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHAT_ID:
        return

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": text,
    }
    requests.post(url, json=payload, timeout=10)


async def send_notification(text: str) -> None:
    await asyncio.to_thread(_send_notification_sync, text)
