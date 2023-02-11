from aiogram import types, Dispatcher
import config


async def cmd_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="App",
        web_app=types.WebAppInfo(url=f"{config.APP_URL}/web-start")
    )
    keyboard.add(btn)
    await message.answer(
        "Hello, World!",
        reply_markup=keyboard,
    )


def register_handler(dp: Dispatcher):
    dp.register_message_handler(
        cmd_start,
        commands="start"
    )
