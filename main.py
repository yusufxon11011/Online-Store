import asyncio
import logging
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from handlers.msg_handlers import msg_routers
from handlers.commands_handlers import commands_router
from aiogram.client.default import DefaultBotProperties
from handlers.admin_msg_handlers import admin_message_router

async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode='HTML',
            link_preview_is_disabled=True
        )
    )
    dp = Dispatcher()
    dp.include_routers(
        commands_router, admin_message_router, msg_routers
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
