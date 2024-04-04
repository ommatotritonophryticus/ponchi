"""
File include Tic-Tac-Toe game class
"""
import random
from typing import Tuple, List, Dict

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class Game:
    """
    Tic-Tac-Toe game class
    """

    cursors: Dict[str, Tuple[int, int]] = {
        '⇙': (2, 0),
        '⇘': (2, 2),
        '⇗': (0, 2),
        '⇖': (0, 0),
        '⇐': (1, 0),
        '⇑': (0, 1),
        '⇒': (1, 2),
        '⇓': (2, 1),
        '↺': (1, 1),
    }

    def __init__(self, field: List[List[str]] | None = None):
        """
        If the field is not passed, it creates a blank field.
        """
        if field:
            self.field: List[List[str]] = field

        else:
            self.field = [['.' for _ in range(3)] for _ in range(3)]

    def get_symbol_about_position(self, x: int, y: int) -> str:
        """
        Returns a character based on the position
        """
        for item in self.cursors.items():
            if item[1] == (x, y):
                return item[0]
        raise ValueError(f'The coordinates(x={x}, y={y}) are out of the field')

    def get_keyboard(self) -> 'ReplyKeyboardMarkup':
        """
        Creates a keyboard based on the state of the playing field
        """
        keyboard: List[List[KeyboardButton]] = []
        for row_index, row in enumerate(self.field):

            temp_row: List[KeyboardButton] = []
            for column_index, element in enumerate(row):

                if element == '.':
                    temp_row.append(
                        KeyboardButton(text=self.get_symbol_about_position(row_index, column_index))
                    )

                else:
                    temp_row.append(
                        KeyboardButton(text=self.field[row_index][column_index])
                    )

            keyboard.append(temp_row)

        return ReplyKeyboardMarkup(keyboard=keyboard)

    def change_symbol(self, x: int, y: int, symbol: str) -> bool:
        """
        Changes the symbol on the field based on the coordinates
        """
        self.field[x][y] = symbol
        return True

    def make_a_move(self, x: int, y: int, symbol: str) -> bool:
        """
        Execution of a move, if possible
        """
        if self.field[x][y] != '.':
            return False

        self.change_symbol(x, y, symbol)
        return True

    def win_test(self) -> Tuple[bool, str]:
        """
        Test of win
        """
        for i in range(3):

            if self.field[i][0] == self.field[i][1] == self.field[i][2] != '.':
                return True, self.field[i][0]

            if self.field[0][i] == self.field[1][i] == self.field[2][i] != '.':
                return True, self.field[0][i]

        if self.field[0][0] == self.field[1][1] == self.field[2][2] != '.':
            return True, self.field[0][0]

        if self.field[0][2] == self.field[1][1] == self.field[2][0] != '.':
            return True, self.field[0][2]

        return False, '.'

    def game_over_test(self) -> bool:
        """
        Checks for free fields
        """
        return not any('.' in row for row in self.field)

    def npc(self) -> 'Game':
        """
        Just puts the character in a random free field
        """
        if self.game_over_test():
            return self

        while 1:
            x = random.randint(0, 2)
            y = random.randint(0, 2)

            if self.field[y][x] == '.':
                self.field[y][x] = 'O'
                break

        return self

    def make_string(self) -> str:
        """
        Render field to string
        """

        result = '\n―――――\n'
        for row in self.field:
            result += '│'.join(row)
            result += '\n―――――\n'
        return result
