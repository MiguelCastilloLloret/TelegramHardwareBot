import telebot
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
import re

TOKEN = '245381199:AAG30qtFzCQB_5kqx9rQ5Ev2O_dabksxKw0'

mi_bot = telebot.TeleBot(TOKEN)

def listener(mensajes):
	for m in mensajes:
		chat_id = m.chat.id
		if m.content_type == 'text':
			print ("[" + str(chat_id) + "]:" + m.text)

@mi_bot.message_handler(commands=['help'])
def command_reviews(m):
	chat_id = m.chat.id
	mi_bot.send_message(chat_id, "Hi!, I am HardwareBot, nice to meet you! If you want general info of a Graphics Card, ask me with /GPUInfo + card name. For CPUs, say /CPUInfo + CPU Name. If you want a GPU review list, ask /reviewsGPUNVIDIA + GPU Name or /reviewsGPUAMD + GPU Name. Hope I can help you!")

@mi_bot.message_handler(commands=['reviewsGPUAMD'])
def command_reviews(m):
	chat_id = m.chat.id
	message = m.text[15:]
	response = "Reviews of " + message + ":\n"
	reviewsweb = BeautifulSoup(urlopen("https://www.techpowerup.com/reviewdb/Graphics-Cards/AMD/"))
	tags = reviewsweb.find_all("a", class_="categories")
	print(type(tags))
	expresion = re.compile("\D*?"+message)
	for aTag in tags:
		print(aTag.string.strip())
		print(expresion.match(aTag.string.strip()))
		if aTag.string is not None and expresion.match(aTag.string.strip()):
			urlTag = aTag['href']
			print("https://www.techpowerup.com" + urlTag)
			break
	reviewsweb = BeautifulSoup(urlopen("https://www.techpowerup.com" + urlTag))
	tags = reviewsweb.find_all("td", class_="name")
	print(tags)
	for aTag in tags:
		urlTag = aTag.contents[1]
		print(urlTag['href'])
		response = response + urlTag['href'] + "\n\n"
		if 4096 - len(response) < 100:
			mi_bot.send_message(chat_id, response)
			response = ""
	mi_bot.send_message(chat_id, response)

@mi_bot.message_handler(commands=['reviewsGPUNVIDIA'])
def command_reviews(m):
	chat_id = m.chat.id
	message = m.text[18:]
	response = "Reviews of " + message + ":\n"
	reviewsweb = BeautifulSoup(urlopen("https://www.techpowerup.com/reviewdb/Graphics-Cards/NVIDIA/"))
	tags = reviewsweb.find_all("a", class_="categories")
	print(type(tags))
	expresion = re.compile("\D*?"+message)
	for aTag in tags:
		print(aTag.string.strip())
		print(expresion.match(aTag.string.strip()))
		if aTag.string is not None and expresion.match(aTag.string.strip()):
			urlTag = aTag['href']
			print("https://www.techpowerup.com" + urlTag)
			break
	reviewsweb = BeautifulSoup(urlopen("https://www.techpowerup.com" + urlTag))
	tags = reviewsweb.find_all("td", class_="name")
	print(tags)
	for aTag in tags:
		urlTag = aTag.contents[1]
		print(urlTag['href'])
		response = response + urlTag['href'] + "\n\n"
		if 4096 - len(response) < 100:
			mi_bot.send_message(chat_id, response)
			response = ""
	mi_bot.send_message(chat_id, response)

@mi_bot.message_handler(commands=['CPUInfo'])
def command_reviews(m):
	chat_id = m.chat.id
	message = m.text[9:]
	response = "Info about " + message + ":\n"
	reviewsweb = BeautifulSoup(urlopen("https://www.techpowerup.com/cpudb/?mfgr%5B%5D=amd&mfgr%5B%5D=intel&class%5B%5D=desktop&class%5B%5D=server&released%5B%5D=y14_c&released%5B%5D=y11_14&released%5B%5D=y08_11&released%5B%5D=y05_08&released%5B%5D=y00_05&logo=&nCores=&process=&socket=&codename=&multi=&sort=name&q="))
	tags = reviewsweb.find_all("a")
	print(type(tags))
	expresion = re.compile(".*?"+message)
	for aTag in tags:
		print(aTag.string)
		if aTag.string is not None and expresion.match(aTag.string):
			print(aTag.string)
			urlTag = aTag['href']
			print("https://www.techpowerup.com" + urlTag)
			break
	reviewsweb = BeautifulSoup(urlopen("https://www.techpowerup.com" + urlTag))
	img = reviewsweb.find("img", class_="cpulogo")
	urlretrieve("http:" + img['src'],"a.gif")
	mi_bot.send_message(chat_id, response)
	response = ""
	mi_bot.send_photo(chat_id, open('a.gif','rb'))
	trTags = reviewsweb.find_all("tr")
	print(trTags)
	for tcTag in trTags:
		if len(tcTag) >= 4:
			if tcTag.contents[1].string is not None and tcTag.contents[3] is not None and tcTag.contents[3].string is not None :
				thTag = tcTag.contents[1]
				print(thTag)
				tdTag = tcTag.contents[3]
				print(tdTag)
				response = response + thTag.string + " " +tdTag.string + "\n"
			elif tcTag.contents[1].string is not None:
				thTag = tcTag.contents[1]
				print(thTag)
				response = response + thTag.string + " unknown" "\n"
			elif tcTag.contents[3] is not None and tcTag.contents[3].string is not None:
				tdTag = tcTag.contents[3]
				print(tdTag)
				response = response + tdTag.string + "\n"
	mi_bot.send_message(chat_id, response)

@mi_bot.message_handler(commands=['GPUInfo'])
def command_reviews(m):
	chat_id = m.chat.id
	message = m.text[9:]
	response = "Info about " + message + ":\n"
	reviewsweb = BeautifulSoup(urlopen("https://www.techpowerup.com/gpudb/?mfgr%5B%5D=amd&mfgr%5B%5D=nvidia&mobile=0&released%5B%5D=y14_c&released%5B%5D=y11_14&released%5B%5D=y08_11&released%5B%5D=y05_08&released%5B%5D=y00_05&generation=&chipname=&interface=&ushaders=&tmus=&rops=&memsize=&memtype=&buswidth=&slots=&powerplugs=&sort=released&q="))
	tags = reviewsweb.find_all("a")
	print(type(tags))
	expresion = re.compile("\D*?"+message)
	for aTag in tags:
		if aTag.string is not None and expresion.match(aTag.string):
			print(aTag.string)
			urlTag = aTag['href']
			print("https://www.techpowerup.com" + urlTag)
			break
	reviewsweb = BeautifulSoup(urlopen("https://www.techpowerup.com" + urlTag))
	img = reviewsweb.find("img", title="Card Photo")
	if img is not None:
		urlretrieve("https://www.techpowerup.com" + img['src'],"a.jpg")
		mi_bot.send_photo(chat_id, open('a.jpg','rb'))
	mi_bot.send_message(chat_id, response)
	response = ""
	trTags = reviewsweb.find_all("tr")
	print(trTags)
	for tcTag in trTags:
		if len(tcTag) >= 4:
			if tcTag.contents[1].string is not None and tcTag.contents[3] is not None and tcTag.contents[3].string is not None :
				thTag = tcTag.contents[1]
				print(thTag)
				tdTag = tcTag.contents[3]
				print(tdTag)
				response = response + thTag.string + " " +tdTag.string + "\n"
			elif tcTag.contents[1].string is not None:
				thTag = tcTag.contents[1]
				print(thTag)
				response = response + thTag.string + " unknown" "\n"
			elif tcTag.contents[3] is not None and tcTag.contents[3].string is not None:
				tdTag = tcTag.contents[3]
	mi_bot.send_message(chat_id, response)

mi_bot.set_update_listener(listener)

mi_bot.polling(none_stop=True)

while True:
	pass