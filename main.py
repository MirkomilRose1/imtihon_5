import os
import asyncio
from aiogram import Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from dispatcher.dispatcher import dp
from function import get_information

from dotenv import load_dotenv

load_dotenv()


@dp.message(CommandStart())
async def startup(message: Message):
    first_name = message.from_user.first_name
    await message.answer(f"""Hello {first_name}! 
Our bot can send image to this bot from Kun.uz website 
If you ready click this --> /Go""")


data = get_information()


@dp.message(lambda msg: msg.text == '/Go')
async def send_image(message: Message):
    s = data["date"], data["year"], data["info1"], *data["info2"]
    photo = FSInputFile('news-firefox.png', filename='screenshot')
    await message.answer_photo(photo)
    await message.answer(str(s).replace(',', '').replace('(', '').replace(')', '').replace("'", ''))


async def main():
    token = os.getenv('BOT_TOKEN')
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
