import telegram, requests, os
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

mow = datetime.datetime.now()
bot = telegram.Bot(token="1007959039:AAHWzSoqu0dZxAR350tQt5shwr2wXvmV72Q")
bot.sendMessage(chat_id=1331159914, text="테스트")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def telegram_bot():
    url = 'https://algumon.com/'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    name = soup.select('div.post-group > div.product-body.clearfix > div > p:nth-child(2) > span > a')
    latest = name[0].text.strip()
    print(latest)
    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+', encoding="utf-8") as f_read:
        before = f_read.readline()
        if before != latest : 
            bot.sendMessage(chat_id=1331159914, text="다른데요?")
        else:
            bot.sendMessage(chat_id=1331159914, text="똑같아요")
        f_read.close()

sched = BlockingScheduler()
telegram_bot()
sched.add_job(telegram_bot, 'interval', seconds=10)
sched.start()