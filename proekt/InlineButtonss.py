
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
from teext import *




router = Router()



@router.message(F.text.lower() == "кожные повреждения") 
async def first_aid(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Ушиб", callback_data="A1" 
        ), 
        types.InlineKeyboardButton(text="Порез", callback_data="A2"), 
        ) 

    builder.row( 
        types.InlineKeyboardButton(text="Ссадины", callback_data="B1"), 
        types.InlineKeyboardButton(text="Занозы", callback_data="B2"), 
    ) 

    builder.row( 
        types.InlineKeyboardButton(text="Синяки", callback_data="C1"), 
        types.InlineKeyboardButton(text="Рваные раны", callback_data="C2"),

    ) 
    builder.row(
        types.InlineKeyboardButton(text="Укусы", callback_data="D1"),
        types.InlineKeyboardButton(text="Прыщи", callback_data="D2"),
    )
    await message.answer(text="Ответ в формате текста", reply_markup=builder.as_markup())
    




    







@router.message(F.text.lower() == "укусы") 
async def bites(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Пчелы, Шмеля, Осы", callback_data="A3"),
        types.InlineKeyboardButton(text="Муравья", callback_data="A4" ),
        )

    builder.row( 
        types.InlineKeyboardButton(text="Клещи", callback_data="B3"),
        types.InlineKeyboardButton(text="Ежа", callback_data="B4" ),

        )
    builder.row( 
        types.InlineKeyboardButton(text="Блох", callback_data="C3"),
        types.InlineKeyboardButton(text="Змеи", callback_data="C4" ),

    )
    builder.row( 
        types.InlineKeyboardButton(text="Пауков", callback_data="D3"),
        types.InlineKeyboardButton(text="Животных", callback_data="D4" ),
    )
    await message.answer(text="Ответ в формате Текста", reply_markup=builder.as_markup())




@router.message(F.text.lower() == "основы зож") 
async def healthy_iifestyle(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(
            text="Питание", 
            callback_data="A1",
            url="https://profilaktica.ru/for-population/profilaktika-zabolevaniy/vse-o-pravilnom-pitanii/printsipy-zdorovogo-pitaniya/?ysclid=m544msc91c725536571"
        ),

        types.InlineKeyboardButton(
            text="Сон", 
            callback_data="A2",
            url="https://www.kp.ru/doctor/bolezni/kak-pravilno-spat/?ysclid=m545ikl5mr316012729"
            ),
        )

    builder.row( 
        types.InlineKeyboardButton(
            text="Режим и Распорядок дня",
            callback_data="B1",
            url="https://cgon.rospotrebnadzor.ru/naseleniyu/zdorovyy-obraz-zhizni/rezhim-dnya/"
            ),
        types.InlineKeyboardButton(
            text="Зарядка, Комплекс Базовых Упражнений", 
            callback_data="B2",
            url="https://alexfitness.ru/fitness_guide/programma_dlya_utrennej_gimnastiki"
            ),

        )
    builder.row( 
        types.InlineKeyboardButton(
            text="Личная Гигиена", 
            callback_data="C1",
            url="https://cgon.rospotrebnadzor.ru/naseleniyu/zdorovyy-obraz-zhizni/lichnaya-gigiena/"
            ),
        types.InlineKeyboardButton(
            text="Ссылка2", 
            callback_data="C2",
            url=""
            ),
        )
    builder.row( 
        types.InlineKeyboardButton(
            text="Ссылка1", 
            callback_data="D1"
            ),
        types.InlineKeyboardButton(
            text="Ссылка2", 
            callback_data="D2"
            ),
    )
    await message.answer(text="Ответ в формате URL", reply_markup=builder.as_markup())





@router.message(F.text.lower() == "форум3") 
async def forum_three(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="A1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="A2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="A3")
        )

    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="B1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="B2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="B3")
        )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="C1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="C2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="C3")
    )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="D1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="D2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="D3")
    )
    await message.answer(text="Ответ в формате URL", reply_markup=builder.as_markup())





@router.message(F.text.lower() == "форум4") 
async def forum_four(message: types.Message):  
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="A1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="A2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="A3")
        )

    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="B1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="B2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="B3")
        )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="C1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="C2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="C3")
    )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="D1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="D2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="D3")
    )
    await message.answer(text="Ответ в формате URL", reply_markup=builder.as_markup())






@router.message(F.text.lower() == "форум5") 
async def forum_five(message: types.Message):  
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="A1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="A2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="A3")
        )

    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="B1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="B2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="B3")
        )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="C1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="C2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="C3")
    )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="D1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="D2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="D3")
    )
    await message.answer(text="Ответ в формате URL", reply_markup=builder.as_markup())













@router.message(F.text.lower() == "форум2") 
async def sgeadhtgh(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton( 
            text="A1",  
            callback_data="A1", 
            url = "https://misis.ru" 
        ), 
        types.InlineKeyboardButton( 
            text="A2",  
            callback_data="A2",
            url = "https://ya.ru/"
            
        ), 
        types.InlineKeyboardButton(text="A3", callback_data="A3" ),

        ) 
            
    builder.row( 
        types.InlineKeyboardButton(text="B1", callback_data="B1"), 
        types.InlineKeyboardButton(text="B2", callback_data="B2"), 
        types.InlineKeyboardButton(text="B3", callback_data="B3"),

    ) 

    builder.row( 
        types.InlineKeyboardButton(text="C1", callback_data="C1"), 
        types.InlineKeyboardButton(text="C2", callback_data="C2"), 
        types.InlineKeyboardButton(text="C3", callback_data="C3"),

    ) 
    builder.row(
        types.InlineKeyboardButton(text="D1", callback_data="D1"),
        types.InlineKeyboardButton(text="D2", callback_data="D2"),
        types.InlineKeyboardButton(text="D3", callback_data="D3"),

    )
    await message.answer( 
        "Soveti2:", 
        reply_markup=builder.as_markup() 
    ) 
