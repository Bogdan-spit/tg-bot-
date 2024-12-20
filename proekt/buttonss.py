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
dp = Dispatcher()  


@dp.message(Command("start")) 
async def cmd_start(message: types.Message): 
    kb = [ 
        [ 
            
            types.KeyboardButton(text="Первая помощь"),
            types.KeyboardButton(text="test229"),
            types.KeyboardButton(text="test230"),
            # types.KeyboardButton(text="start"),
            types.KeyboardButton(text="test"),
            
            
        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.answer("Опции кнопок клавиатуры?", reply_markup=keyboard) 



@dp.message(F.text.lower() == "test") 
async def cmd_special_buttons(message: types.Message): 
    builder = ReplyKeyboardBuilder() 
    builder.row( 
        types.KeyboardButton(text="Форум"), 
        types.KeyboardButton(text="Форум2"), 
        types.KeyboardButton(text="Форум3"), 
        types.KeyboardButton(text="Форум4"), 
        types.KeyboardButton(text="Форум5"), 
        
    ) 

    builder.row( 
        types.KeyboardButton( 
            text="Назад") 
    ) 
 
    await message.answer( 
        "Выберите действие:", 
        reply_markup=builder.as_markup(resize_keyboard=True), 
    ) 
 




@dp.message(F.text.lower() == "назад") 
async def with_puree(message: types.Message): 
    kb = [ 
        [ 
            types.KeyboardButton(text="Первая помощь"),
            types.KeyboardButton(text="test229"),
            types.KeyboardButton(text="test230"),
            # types.KeyboardButton(text="start"),
            types.KeyboardButton(text="test"),
        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.reply("Мы снова здесь", reply_markup=keyboard) 




@dp.message(Command("help")) 



@dp.message(Command("help")) 
async def cmd_start(message: types.Message): 
    kb = [ 
        [ 
            
            types.KeyboardButton(text="Укусы"),
            types.KeyboardButton(text="Не укусы"),
            types.KeyboardButton(text="хз"),
            # types.KeyboardButton(text="start"),
            types.KeyboardButton(text="спс"),
            
            
        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.answer("умный тест хз", reply_markup=keyboard) 

@dp.message(F.text.lower() == "назад") 
async def with_puree(message: types.Message): 
    kb = [ 
        [ 
        types.KeyboardButton(text="123"), 
        types.KeyboardButton(text="456"), 
        types.KeyboardButton(text="789"), 
        types.KeyboardButton(text="101112"), 
        types.KeyboardButton(text="131415"), 
        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.reply("Мы снова здесь", reply_markup=keyboard) 



