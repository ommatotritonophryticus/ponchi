"""
File where message templates are stored
"""
GREETING = 'Hi!\n\nWe can start new game.'

CANT_MOVE = 'You cant make this move. Try again.'

MAKE_A_MOVE = 'Make a move.'


def make_final_string(field_string: str, game_status: str):
    """
    Final string template.
    Arguments: the finished field in the line, and the end-of-game state.
    """
    return f'''Game over
<code>{field_string}</code>
{game_status} Send something to play again.'''
