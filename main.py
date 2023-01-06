import requests
import config
from aiogram import types, executor, Dispatcher, Bot
from bs4 import BeautifulSoup as b

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, """Привет! Я бот с помощью которого можно быстро найти товары в <b><a href='https://www.kivano.kg/mobilnye-telefony'>kivano.kg</a></b>
    
Чтобы получить товар введите его название""",
parse_mode='html', disable_web_page_preview=1)


@dp.message_handler(content_types=['text'])
async def parser(message: types.message):
    url = 'https://www.kivano.kg/product/index?search=' + message.text
    request = requests.get(url)
    soup = b(request.text, 'html.parser')


    all_links = soup.find_all('div', class_='listbox_title')
    for link in all_links:
        url = 'https://www.kivano.kg/'+link['href']
        request = requests.get(url)
        soup = b(request.text, 'html.parser')
        print(1)
    

        name = soup.find('div', class_='listbox_title').find('a').text
        price = name.find('strong')
        # name.find('a').extract()
        name = name.text
        print(name)

        img = soup.find('div', class_='img200')
        img = img.findChildren('img')[0]
        img = img['src']
        

        




executor.start_polling(dp)