from pprint import pprint
# This project uses bracktracking to solve sudoku
# Using the power of computer we will fill values and check if its the solution
# If its not a solution we backtrack


def find_next_empty(puzzle):
    # The sudoku board will be a list of lists and -1 represents empty space
    # [[1,-1,2,-1,-1,3,-1,7,-1],     this is the first row of 9x9 sudoku board
    #  [-1,-1-1,4,-1,6,-1,-1,-1],
    #  [....]
    # ...]

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    # if no spaces then we return None to let computer know it cant fill anymore spaces
    return None, None


def is_valid(puzzle, guess, row, col):
    # this function figures out whether the guess at the row/col of the puzzle is valid
    # func. returns True if its valid else return False

    # How sudoku works:
    # You place a number in and empty space in the 9x9 grid
    # Your number is only valid if the same nuber does not exists in"
    #   1. the same row
    #   2. the same column
    #   3. Or the 3x3 grid which your placed number's cell is the part of

    # 1. check the same row
    row_vals = puzzle[row]  # this is the first row.
    if guess in row_vals:
        return False

    # 2. check the same column.
    # 2 ways do write the code

    # 1st for lopping
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])

    # 2nd list comprehension
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # 3. check the 3x3 matrix the guess cell is part of
    # A bit tricky. We want to get where 3x3 square starts an iterate over the 3 values in the row/col

    row_start = (row // 3) * 3  # 0 // 3 = 0, 3 // 3 = 1, 4 // 3 = 1
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # If all the above cases are satifies then the move is vaild!
    return True


def solve_sudoku(puzzle):

    row, col = find_next_empty(puzzle)

    # Steps
    # 1.1 If all the cells are filled. We are done
    if row is None:
        return True

    # 2 if there is a place to put a guess. We put a valid guess between 0 and 9
    for guess in range(1, 10):
        # 3 check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # 3.3 if the guess is valid, we place that guess on the puzzle
            # We mutate the list.
            puzzle[row][col] = guess

            # recursively call the solver!
            if solve_sudoku(puzzle):
                return True

        # Now there are 2 more cases which must be handled properly
        # 1. If the guess in not valid
        # 2. if the guess does not solve the sudoku

        # We will backtrack by resetting the puzzle and try with another guess
        puzzle[row][col] = -1

    # 6 if we try all possible solution and still can't solve then its unsolvable
    return False


if __name__ == '__main__':
    example_board = [
        [-1, 8, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   4, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    print(solve_sudoku(example_board))
    pprint(example_board)
