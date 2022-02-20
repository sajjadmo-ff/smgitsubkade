from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from googlesearch import search
from bs4 import BeautifulSoup
import requests

api_id = 4431543
api_hash = 'b9923e14724a0c5e24efc6c22caeff21'
bot_token = '5251659379:AAHh-fO7FlTQW_-oMPIXwPcMlJHe116BKto'
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
client = TelegramClient('anon', api_id, api_hash)
@client.on(events.NewMessage)
async def my_event_handler(event):
    filmName = event.raw_text

    for url in search(filmName+'site:subkade.ir', stop=1):
        #print(url)
        page = requests.get(url)
    soup = BeautifulSoup( page.content ,'html.parser')
#print(url)
    url = search(filmName+'site:subkade.ir')
    link0 = soup.find("div",class_="sgl_dl a3")
    del link0['class']

    link1 = soup.find("div",class_="sgl_dl").find("a",class_="dl_item_btn")
    link2 = link1['href']

    await event.reply(link2)
client.start()
client.run_until_disconnected()
