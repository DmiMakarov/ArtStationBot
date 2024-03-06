from aiogram import Bot, Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    await message.reply("Hello, admin!")

async def admin_repeat(bot: Bot, admin: int):
    print(admin)
    await bot.send_message(admin, "Hello, admin!!!!")

def register_admin(dp: Dispatcher):
    dp.message.register(admin_start)
  