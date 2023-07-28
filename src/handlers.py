import asyncio

from aiogram import Dispatcher, types

import loggers
from src.repo import IGPTRepo


async def echo(message: types.Message):
    """ Выполняется при любом сообщении """
    gpt: IGPTRepo = message.bot['repo_gpt']
    msg_id = await message.answer(f'Запрос \"{message.text}\" успешно задан в GPT')
    try:
        res = await asyncio.get_running_loop().run_in_executor(None, gpt.ask, message.text)
    except Exception as e:
        res = str(e)
    loggers.bot_logger.info(res)
    await message.bot.send_message(message.chat.id, f"Ответ GPT: \n{res}", parse_mode='Markdown', reply_to_message_id=msg_id)


async def start(message: types.Message):
    """ Выполняется при старте """
    await message.answer("<b>Бот для общения с ChatGPT.</b>\nВведите следующим сообщением вопрос к ChatGPT.")


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(echo)

