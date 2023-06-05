class Gameboard:
    def __init__(self):
        self.board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.player = 'X'
        self.turn = 1
        self.last_move = []

    def print_board(self):
        print('\n 1 2 3 4 5 6 7')
        for r in range(6):
            print('|', end='')
            for c in range(6):
                print(f'{self.board[r][c]}', end='.')
            print(f'{self.board[r][6]}|')
        # print('---------------')  # mettere il fondo mi sembra bruttino
        print()

    def new_sign(self):
        try:
            col = int(input('Which column do you want? '))
            if col < 1 or col > 7 or self.board[0][col-1] in ['X', 'O']:
                raise ValueError
        except ValueError:
            print('Invalid input!')
            return self.new_sign()
        else:
            for row in range(5, -1, -1):
                if self.board[row][col-1] == ' ':
                    self.board[row][col-1] = self.player
                    self.last_move = [row, col-1]  # per ridurre i check necessari al game over
                    return

    def pass_turn(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
        self.turn += 1

    def is_game_over(self):  # LIST COMPREHENSION modo migliore per accedere a colonne in una lista di liste
        r = self.last_move[0]
        c = self.last_move[1]
        line = ''.join(self.player for _ in range(4))
        if (line in ''.join(row[c] for row in self.board)  # verticale
                or line in ''.join(self.board[r])  # orizzontale
                or line in ''.join(self.board[r+i][c+i] for i in range(-4, 4) if (0 <= r+i <= 5 and 0 <= c+i <= 6))  # diagonale 1
                or line in ''.join(self.board[r + i][c - i] for i in range(-4, 4) if (0 <= r+i <= 5 and 0 <= c-i <= 6))):  # diagonale 2
            return True
        return False
