from aiogram import Router, F
from aiogram.types import Message

msg_routers = Router()

@msg_routers.message(F.document)
async def file_handler(message: Message):
        file = await message.bot.get_file(file_id=message.document.file_id)
        file_path = file.file_path
        await message.bot.download_file(file_path, f"downloads\\{message.document.file_name}")