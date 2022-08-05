import asyncio
from aiogram import Bot, Dispatcher

from bot.handlers import user_status_in_group
from fake_updates import chat_member_updated


async def main():
    bot = Bot("")
    dp = Dispatcher()

    dp.include_router(user_status_in_group.router)

    result = await dp.feed_update(bot, chat_member_updated.member_became_admin)
    assert result == "from_member_to_administrator"

asyncio.run(main())
