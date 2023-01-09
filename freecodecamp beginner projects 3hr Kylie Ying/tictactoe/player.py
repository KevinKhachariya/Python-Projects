import math
import random


class Player:
    def __init__(self, letter):
        # letter can be either x or o which represents a player respectively
        self.letter = letter

    def get_move(self, game):
        pass

# inheritance in python using classes


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8):")

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid move. Try again!")

        return val

# The below class implements minimax algorithm and recursion using python dictionaries
# To calculate the utility function to either always win or tie in a tic-tac-toe game.
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            self.get_move(random.choice(game.available_move()))
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    # The minimax algorithm to calculate the utility function value to either win or tie the game,
    def minimax(self, state, player):

        max_player = self.letter  # genius player itself
        other_player = 'O' if player == 'X' else 'X'  # the other player
       
    # check if the previous move is the winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.count_empty_squares() + 1) if other_player == max_player else -1 * (state.count_empty_squares() + 1)}

        elif not state.empty_squares(): # if there are no sqaures left to fill
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # the minimax logic

            # step 1 make a move and try the spot
            state.make_move(possible_move, player)
            
            # step 2 recurse using minimax to simulate the game maxing the move
            # now we simulate the game by recursion and either find max or 0 (either win or tie)
            sim_score = self.minimax(state, other_player)
            
            # step 3 undo the move. 
            # Why? Because for the current state of the game for the current turns of either genius player or opponent
            # we have a simulated score based on which we move. This score always makes sure we either tie or win
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # other this messes up with recursion part
            
            # step 4 update the dictionaries if possible

            # if we are maximizing player from the simulated score based on all the predicted moves by genius player
            # Maximizing player always chooses maximum score
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
            # Else if the genius player is the minimizing player we chose the minimum score (this is what the algorithm is!).
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score # replace best
        
        return best


        
