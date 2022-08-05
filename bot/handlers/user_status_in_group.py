from aiogram import F, Router, Bot
from aiogram.dispatcher.filters.chat_member_updated import \
    ChatMemberUpdatedFilter, IS_NOT_MEMBER, MEMBER, ADMINISTRATOR, CREATOR, KICKED, LEFT, RESTRICTED
from aiogram.types import ChatMemberUpdated

router = Router()


@router.chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=(KICKED | LEFT | RESTRICTED | MEMBER) >> (ADMINISTRATOR | CREATOR)
    )
)
async def from_member_to_administrator(event: ChatMemberUpdated):
    return "from_member_to_administrator"
