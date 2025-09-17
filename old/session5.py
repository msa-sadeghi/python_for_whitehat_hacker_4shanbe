# import requests

# ip = input("enter the ip address: ")
# response = requests.get(f"http://ip-api.com/json/{ip}")
# data = response.json()
# print(data["city"])

# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# url = input("enter site address: ")
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# links = []

# for a in soup.find_all('a'):
#     link = urljoin(url, a['href'])
#     links.append(link)


# print(links)

# username = "test33_33_33_bot"
# from telegram.ext import Updater, CommandHandler
# token = "8442215629:AAHDBL9-RmZu7wCyWWvvuBpNrgqUrgDPgLg"

# def start(update, context):
#     update.message.reply_text("سلام در خدمتیم")

# def main():
#     updater = Updater(token, use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))

#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()

import threading
import time
import random
def port_scan(i):
    time.sleep(random.random())
    print("scanning", i)


threads = []
for i in range(4):
    t = threading.Thread(target=port_scan, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()