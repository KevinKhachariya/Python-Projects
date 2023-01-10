import random
import re


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size  # dimension size
        self.num_bombs = num_bombs

        # lets create the board
        self.board = self.make_new_board()  # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row, col) tuples into this set

        self.dug = set()

    def make_new_board(self):
        # construct a new board based on the dim zie and num of bombs
        # we should construct the list of lists here (or whaterever representation you prefer),
        # but since we have a 2-D board, list of lists is more natural)
        board = [['None' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # the array will look like this
        # [ [None, None, ..., None],
        #   [None, None, ..., None],
        # ...
        # ]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            # if dimension is 4 then bombs can be in between 0 to 15
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1
        
        return board


    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

        # generate a new board

        

    def get_num_neighboring_bombs(self, row, col):

        num_neighboring_bombs = 0
        # min and max calculation to not get out of bounds
        for r in range(max(0, row-1), min(self.dim_size-1, (row+1)+1)):
            for c in range(max(0, col-1), min(self.dim_size-1, (col+1)+1)):
                if r == row and c == col:
                    # our original location, don't need to check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at (row,col) location
        # return True if succesful dig, False if bomb dug

        # a few scenarios:
        # hit bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> dig recursively neighbors

        self.dug.add((row, col))  # keeping track of where we dug

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row-1), min(self.dim_size-1, (row+1)+1)):
            for c in range(max(0, col-1), min(self.dim_size-1, (col+1)+1)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        # if the initial dig didn't dug a bomb we shouldn't hit a bomb but stop around it
        return True

    def __str__(self):
        # this is a special function where if you call print on this object
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first lets create a new array that represents what the user would see

        visible_board = [[None for _ in range(
            self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # took the below code from https://github.com/kying18/minesweeper/blob/main/minesweeper.py
        # It is just for pretty UI in CLI which is not important for now while learning to code algorithms


        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep



def play(dim_size=10, num_bombs=10):
    # Step 1 create the board and plant the bomb
    board = Board(dim_size, num_bombs)

    # Step 2 show user the board and ask for where they want to dig

    # Step 3a if location is a bomb, show game over message

    # Step 3b if local is not a bomb, dig recursively until each squares is at least next to a bomb

    # Step 4 repeat steps 2 and 3a/b until there are no more places to dig = win

    safe = True

    # dug is a set which does not contain duplicates in python
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        # there are still non bomb empty spaces users can dig
        print(board)
        # using regular expression we can accept these inputs:
        # 0,0 or 0, 0 or  0
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location. Please try again!")
            continue

        # if the dig is valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb
            break
    
    # 2 ways to end the while loop, either user wins and no space left or dug a bomb
    if safe:
        print('You won!')
    else:
        print('Dug a bomb. Game over!')

        #reveal the board

        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': # good practice. if the project is big this will only run this file
    play()


