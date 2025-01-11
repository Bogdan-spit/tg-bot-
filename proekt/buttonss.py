import asyncio  
import logging  
from aiogram import Bot, Dispatcher, types  
from aiogram.filters.command import Command  
from configs import Config 
from aiogram import F, Router
from random import randint 
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
import sqlite3




router = Router() 










@router.message(F.text.lower() == "назад") 
async def with_puree(message: types.Message): 
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
    await message.reply("Вы вернулись в меню выбора.", reply_markup=keyboard) 










@router.message(F.text.lower() == "первая помощь") 
async def arrhrtjrjrhrththg(message: types.Message): 
    builder = ReplyKeyboardBuilder() 
    builder.row( 
        types.KeyboardButton(text="Кожные повреждения"), 
        types.KeyboardButton(text="Укусы"), 
        types.KeyboardButton(text="Помощь при инсульте"), 


        
    ) 

    builder.row( 
        types.KeyboardButton( 
            text="Назад") 
    ) 

    await message.answer( 
        "Выберите интересующую проблему:", 
        reply_markup=builder.as_markup(resize_keyboard=True), 
    ) 






