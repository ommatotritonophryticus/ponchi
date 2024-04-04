"""
Tic-Tac-Toe application
"""
from typing import Callable

from aiogram.types import Message, ReplyKeyboardRemove
from ponchi.session_controller import SessionController

from game import Game
import templates


async def start(message: Message, session: SessionController) -> Callable:
    """
    Default entrypoint to application.
    Also, the function of starting the game.
    """

    #  Create clear field before start
    await session.set_data('field', [['.' for _ in range(3)] for _ in range(3)])

    await message.answer(templates.GREETING)

    #  Create Game object
    game: Game = Game(await session.get_data('field'))

    #  Send keyboard
    await message.answer(templates.MAKE_A_MOVE, reply_markup=game.get_keyboard())

    #  Return next handler
    return game_process


async def game_process(message: Message, session: SessionController) -> Callable:
    """
    Game process function.
    While the game is running, all processing goes through this handler
    """

    game = Game(await session.get_data('field'))

    # Correct move check
    if message.text not in game.cursors:
        await message.answer(templates.CANT_MOVE, reply_markup=game.get_keyboard())
        return game_process

    # Getting a position from a character
    position_x, position_y = game.cursors[message.text]

    # Attempted move
    move_is_done = game.make_a_move(position_x, position_y, 'X')

    if not move_is_done:
        await message.answer(templates.CANT_MOVE, reply_markup=game.get_keyboard())
        return game_process

    return await win_test(
        message,
        session,
        opponent_move,
        game
    )


async def opponent_move(message: Message,
                        session: SessionController,
                        game: Game) -> Callable:
    """
    Opponent move handler
    """

    game.npc()

    return await win_test(
        message,
        session,
        end_of_stroke,
        game
    )


async def win_test(message: Message,
                   session: SessionController,
                   next_function: Callable,
                   game: Game) -> Callable:
    """
    Win test handler
    """

    # Getting game status and winner symbol
    end, symbol = game.win_test()

    if end or game.game_over_test():
        if symbol == 'X':
            status = 'You Win!'
        elif symbol == 'O':
            status = 'You loose.'
        else:
            status = 'Tie.'

        # Send final message
        await message.answer(
            templates.make_final_string(game.make_string(), status),
            reply_markup=ReplyKeyboardRemove()
        )
        # And restart
        return start

    #  If the game is not finished, record the field state
    await session.set_data('field', game.field)

    # And execute next function
    return await next_function(message, session, game)


async def end_of_stroke(message: Message,
                        _,
                        game: Game) -> Callable:
    """
    End of stroke handler
    """
    await message.answer(templates.MAKE_A_MOVE, reply_markup=game.get_keyboard())
    return game_process
