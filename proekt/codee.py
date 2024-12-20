


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


import asyncio  
import logging  
from aiogram import Bot, Dispatcher, types  
from aiogram.filters.command import Command  
from configs import Config 
from aiogram import F 
from random import randint 
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
import sqlite3


logging.basicConfig(level=logging.INFO)  
bot = Bot(token="7942694780:AAEDRJqWBnKbiAx1p99Kt7sW_YGtczeQGuM")  
dp = Dispatcher()  








@dp.message(F.text.lower() == "первая помощь") 
async def cmd_first(message: Message, state: FSMContext):
    await message.answer(
        text="Ответ в формате текста",
        reply_markup=first_aid().as_markup
    )







@dp.callback_query(F.data == "A1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(A1)) 
    
        

@dp.callback_query(F.data == "A2") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(A2)) 

@dp.callback_query(F.data == "B1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(B1)) 

@dp.callback_query(F.data == "B2") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(B2)) 

@dp.callback_query(F.data == "C1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(C1)) 

@dp.callback_query(F.data == "C2") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(C2)) 

@dp.callback_query(F.data == "D1")
async def send_random_value(callback: types.CallbackQuery):  
    await callback.message.answer(str(D1)) 

@dp.callback_query(F.data == "D2") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(D2)) 









async def main():  
    dp.include_router(commandss.router)
    await dp.start_polling(bot) 
    

if __name__ == "__main__":  
    asyncio.run(main())








