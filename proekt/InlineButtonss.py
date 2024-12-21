
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



@router.message(F.text.lower() == "первая помощь")
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
    return builder









def forum(message: types.Message): 
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
    return builder
    # await message.answer( 
    #     "Ссылки:", 
    #     reply_markup=builder.as_markup() 
    # ) 






def forum_two(message: types.Message): 
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
    return builder
    # await message.answer( 
    #     "Ссылки:", 
    #     reply_markup=builder.as_markup() 
    # ) 






@router.message(F.text.lower() == "123") 
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
    return builder
    # await message.answer( 
    #     "Ссылки:", 
    #     reply_markup=builder.as_markup() 
    # ) 





# def forum_four(message: types.Message): 
#     builder = InlineKeyboardBuilder() 
#     builder.row( 
#         types.InlineKeyboardButton(text="Ссылка1", callback_data="A1"),
#         types.InlineKeyboardButton(text="Ссылка2", callback_data="A2" ),
#         types.InlineKeyboardButton(text="Ссылка3", callback_data="A3")
#         )

#     builder.row( 
#         types.InlineKeyboardButton(text="Ссылка1", callback_data="B1"),
#         types.InlineKeyboardButton(text="Ссылка2", callback_data="B2" ),
#         types.InlineKeyboardButton(text="Ссылка3", callback_data="B3")
#         )
#     builder.row( 
#         types.InlineKeyboardButton(text="Ссылка1", callback_data="C1"),
#         types.InlineKeyboardButton(text="Ссылка2", callback_data="C2" ),
#         types.InlineKeyboardButton(text="Ссылка3", callback_data="C3")
#     )
#     builder.row( 
#         types.InlineKeyboardButton(text="Ссылка1", callback_data="D1"),
#         types.InlineKeyboardButton(text="Ссылка2", callback_data="D2" ),
#         types.InlineKeyboardButton(text="Ссылка3", callback_data="D3")
#     )

    # await message.answer( 
    #     "Ссылки:", 
    #     reply_markup=builder.as_markup() 
    # ) 





def forum_five(message: types.Message): 
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
    return builder
    # await message.answer( 
    #     "Ссылки:", 
    #     reply_markup=builder.as_markup() 
    # ) 
















@router.message(F.text.lower() == "test229") 
async def x(message: types.Message): 
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




@router.message(F.text.lower() == "test230") 
async def xt(message: types.Message): 
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
        "Soveti3:", 
        reply_markup=builder.as_markup() 
    ) 
