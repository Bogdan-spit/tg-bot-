import asyncio  
import logging  
from aiogram import Bot, Dispatcher  

from teext import *
from buttonss import *
from InlineButtonss import *
import commandss
import InlineButtonss
import buttonss
import vivodd


logging.basicConfig(level=logging.INFO)  
bot = Bot(token="TOKEN")  
dp = Dispatcher()  




async def main():  
    dp.include_router(commandss.router)
    dp.include_router(InlineButtonss.router)
    dp.include_router(buttonss.router)
    dp.include_router(vivodd.router)
    await dp.start_polling(bot) 


if __name__ == "__main__":  
    asyncio.run(main())




