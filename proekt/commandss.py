from aiogram import types  
from aiogram.filters.command import Command  
from aiogram import Router




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








