import asyncio  
import logging  
from aiogram import Bot, Dispatcher, types  
from aiogram.filters.command import Command  
from configs import Config 
from random import randint 
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
import sqlite3
from aiogram import Router, F




router = Router()

@router.message(Command("start")) 
async def cmd_start(message: types.Message): 
    kb = [ 
        [ 
            
            types.KeyboardButton(text="Первая помощь"),
            types.KeyboardButton(text="test229"),
            types.KeyboardButton(text="test230"),
            types.KeyboardButton(text="test"),
            
            
        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.answer("Опции кнопок клавиатуры?", reply_markup=keyboard) 



# @router.message(Command("help")) 
# async def cmd_start(message: types.Message): 
#     kb = [ 
#         [ 
            
#             types.KeyboardButton(text="Укусы"),
#             types.KeyboardButton(text="Не укусы"),
#             types.KeyboardButton(text="хз"),
#             # types.KeyboardButton(text="start"),
#             types.KeyboardButton(text="спс"),
            
            
#         ], 
#     ] 
#     keyboard = types.ReplyKeyboardMarkup( 
#         keyboard=kb, 
#         resize_keyboard=True, 
#         input_field_placeholder="Текст вместо 'Massage'" 
#     ) 
#     await message.answer("умный тест хз", reply_markup=keyboard) 

def payment_keyboard():
    types.KeyboardButton(text="Советы"),
    types.KeyboardButton(text="test229"),
    types.KeyboardButton(text="test230"),
    # types.KeyboardButton(text="start"),
    types.KeyboardButton(text="test"),

