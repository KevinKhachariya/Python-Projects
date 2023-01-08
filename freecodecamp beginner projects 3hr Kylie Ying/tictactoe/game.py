# This project covers inheritance and list comprehension. Using which command line tic-tac-toe game is created.

import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # a list to represent 3x3 board.
        self.current_winner = None # this will keep track of winner.
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |' ) # simple visual representation of board.
    
    @staticmethod
    def print_board_numbers():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        # 2 ways shown here, the one liner code thanks to python lists,
        # and other in my opinion the "beginner way" who just started learning python

        # 1st way: (using lists)
        # return [i for i,spot in enumerate(self.board) if spot == ' ']

        # 2nd way: (using loop and conditionals)
        moves = []
        for (i, spot) in enumerate(self.board):
            if(spot == ' '):
                moves.append(i)
        return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def count_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
    # The winning logic explained by Kylie Ying here -> https://youtu.be/8ext9G7xspg?t=3005

    # check rows to find if all the letters in that row is same.
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all(spot == letter for spot in row):
            return True
        
    # check columns to find if all the letters in that column in same
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True
        
    # check the both diagonals [0,4,8] and [2,4,6]
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all(spot == letter for spot in diagonal2):
                return True
        
        return False




def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_numbers()
    
    # any starting letter just to initialise
    letter = 'X'

    # we must check here if the board has empty spaces that can be filled
    while game.empty_squares():

        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # a function that will make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # just a spacer in between moves

        # every time the make_move function is called we check for the win logic 
        # and set the winner if any of the winner() func. conditions are satisfied.
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!' )
                return letter
    
    
            letter = 'O' if letter == 'X' else 'X' # we switch turns here
        
        # tiny break between turns
        time.sleep(0.8)
    
    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)



