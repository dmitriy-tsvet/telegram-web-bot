import config
import logging
from aiogram import Dispatcher


async def send(dp: Dispatcher):
    for admin in config.BOT_ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot is running!")
        except Exception as err:
            logging.exception(err)
            continue
