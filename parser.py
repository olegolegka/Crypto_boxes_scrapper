from telethon.sync import TelegramClient
import os
import asyncio
from telethon import events
import pyautogui as pag
from time import sleep
api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
phone_number = os.getenv("phone_number")
client = TelegramClient(phone_number,api_id,api_hash)
last = ""
@ client.on(events.NewMessage(pattern=r"[A-Za-z0-9]{8}"))
def message_handler(event):
        code = event.message.to_dict()["message"]
        if len(code) == 8 and last != code:

                print(code)
                pag.moveTo(1528,599)
                pag.click()
                pag.click()
                pag.hotkey("backspace")
                pag.typewrite(code)
                sleep(2)
                pag.moveTo(1548, 718)
                pag.click()
                pag.click()
                pag.click()
                sleep(2.5)
                pag.moveTo(1431, 796)
                pag.click()
                pag.click()
                pag.moveTo(1471, 776)
                pag.click()
                pag.moveTo(1431, 857)
                pag.click()
                sleep(0.5)
                pag.moveTo(1681, 231)
                sleep(0.5)
                pag.click()
                pag.moveTo(1700, 231)
                pag.click()







client.start()
client.run_until_disconnected()