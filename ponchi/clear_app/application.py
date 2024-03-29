from typing import Callable

from aiogram.types import Message

from ponchi.session_controller import SessionController


async def start(message: Message, session: SessionController) -> Callable:
    '''
    Example function for clear project
    '''
    await message.answer(message.text)
    return start
