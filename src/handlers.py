import asyncio

from aiogram import Dispatcher, types, Bot

import loggers
from src.repo import IGPTRepo


async def _ask_question(bot: Bot, tg_message: int, chat_id: int, gpt: IGPTRepo, question: str):
    res = await asyncio.get_running_loop().run_in_executor(None, gpt.ask, question)
    loggers.bot_logger.info(res)
    await bot.send_message(chat_id, f"Ответ GPT: \n{res}", parse_mode='Markdown', reply_to_message_id=tg_message)


async def echo(message: types.Message):
    """ Выполняется при любом сообщении """
    gpt: IGPTRepo = message.bot['repo_gpt']
    msg_id = await message.answer(f'Запрос \"{message.text}\" успешно задан в GPT')
    await _ask_question(message.bot, msg_id.message_id, message.chat.id, gpt, message.text)


async def start(message: types.Message):
    """ Выполняется при старте """
    await message.answer("<b>Бот для общения с ChatGPT.</b>\n Введите следующим сообщением вопрос к ChatGPT.")


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(echo)
