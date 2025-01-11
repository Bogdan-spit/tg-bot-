import aiogram
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove


from teext import *
from buttonss import *
from InlineButtonss import *
import commandss
import InlineButtonss
import buttonss
import vivodd

import asyncio  
import logging  
from aiogram import Bot, Dispatcher, types  
from aiogram.filters.command import Command  
from configs import Config 
from random import randint 
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
import sqlite3


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
