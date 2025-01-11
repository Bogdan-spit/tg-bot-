import asyncio  
import logging  
from aiogram import Bot, Dispatcher, types  
from aiogram.filters.command import Command  
from configs import Config 
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
            types.KeyboardButton(text="Основы ЗОЖ"),

            
            
        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.answer("Выберите раздел:", reply_markup=keyboard) 




