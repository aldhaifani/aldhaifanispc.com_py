import os
import requests

TOKEN = os.environ.get("fetch_orders_token")
chat_id = "360314133"


def send_message(msg):
    url = (
        f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    )

    print(requests.get(url).json())
