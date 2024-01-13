#!/usr/bin/python3

import requests 
import signal, sys
from colorama import Style, Fore, init

init(autoreset=True) 

def def_handler(sig, frame):
    print(f"{Fore.RED}{Style.BRIGHT}\n\n[!] Leaving...\n")
    sys.exit(1)

# Cntrl + C

signal.signal(signal.SIGINT, def_handler)

# Variables globales 

colors = f"{Style.BRIGHT}{Fore.GREEN}"

print(f"\n{colors}[!] {Fore.WHITE}This application is used to retrieve the location through a public ip.\n")

ip = input(f'{colors}[?] {Fore.YELLOW}Enter the public ip ={colors} ')

print(f"\n{Fore.WHITE}(In case you don't have a token, when you create an account on ipinfo.io you will be given one)\n")

token = input(f'{colors}[?] {Fore.YELLOW}Enter your token ={colors} ')

main_url = (f"http://ipinfo.io/{ip}?token={token}")

r = requests.get(main_url)
data = r.json()

ip = (data["ip"])
hostname = (data["hostname"])
city = (data["city"])
region = (data["region"])
country = (data["country"])
loc = (data["loc"])
org = (data["org"])
postal = (data["postal"])
timezone = (data["timezone"])


print(f"\n{colors}[?] {Fore.YELLOW}This is the information for the IP: {colors}{ip}\n")
print(f"➤ The name of the host is: {colors}{hostname}")
print(f"➤ The city is: {colors}{city}")
print(f"➤ The country is: {colors}{country}")
print(f"➤ The org is: {colors}{loc}")
print(f"➤ The region is: {colors}{org}")
print(f"➤ The postal code is: {colors}{postal}")
print(f"➤ The timezone in {city} is: {colors}{timezone}\n")
