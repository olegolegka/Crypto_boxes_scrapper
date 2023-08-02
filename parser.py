from telethon.sync import TelegramClient
import os
from telethon import events
from credits import cookies, headers
import requests
import json
from time import sleep


api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
phone_number = os.getenv("phone_number")
client = TelegramClient(phone_number, api_id, api_hash)
last = ""
unscсsful_atmps = 0


@client.on(events.NewMessage(pattern=r"[A-Za-z0-9]{8}"))
def message_handler(event):
    grab_flag = True
    code = event.message.to_dict()["message"]
    global last, unscсsful_atmps
    if len(code) == 8 and last != code:
        print(code)
        last = code
        data = json.dumps({"grabCode": code, "channel": "DEFAULT"})
        response = requests.post(
            'https://www.binance.com/bapi/pay/v1/private/binance-pay/gift-box/code/query',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        print(response.json())
        sleep(0.1)
        try:
            grab_flag = response.json()["data"]["grabbed"]
        except KeyError:
            unscсsful_atmps += 1
            return
        if unscсsful_atmps == 8:
            sleep(30)
            unscсsful_atmps = 0
        if not grab_flag:

            response = requests.post(
                'https://www.binance.com/bapi/pay/v1/private/binance-pay/gift-box/code/grabV2',
                cookies=cookies,
                headers=headers,
                data=data,
            )
            print(response.json())
            print("C", code, "получено:", response.json()["data"]["grabAmountStr"], response.json()["data"]["currency"])
            unscсsful_atmps = 0
        else:
            print(code, " уже забран!")


if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
