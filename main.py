import os
from gameboard import Gameboard


def cls():
    """Function to clear the console output. Works on terminal, but not in pycharm"""
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
print('''
  _____                        _  _   
 |  ___|__  _ __ ______ _     | || |  
 | |_ / _ \| '__|_  / _` |    | || |_ 
 |  _| (_) | |   / / (_| |    |__   _|
 |_|  \___/|_|  /___\__,_|       |_|  
 
''')  # titolo

t = Gameboard()

game_is_on = True
while game_is_on and t.turn <= 42:
    t.print_board()
    print(f'Player {t.player} turn.')
    t.new_sign()
    #print(t.board[t.last_move[0]])
    if t.is_game_over():
        game_is_on = False
    else:
        t.pass_turn()
        cls()

t.print_board()
if t.turn < 42:
    print(f'Player {t.player} wins!')
else:
    print('It\'s a tie!')
