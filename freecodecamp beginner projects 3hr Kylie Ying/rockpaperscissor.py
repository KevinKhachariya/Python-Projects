## This project demonstrate simple rock, paper and scissors game which a user plays against their computer.

import random

def play():
    user = input("r or p or s: ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'

    # r > s , s > p, p > r

    if is_win(user, computer):
        return f'You won! You: {user} Computer: {computer}'
    
    return f'You lost to computer. Computer choice was {computer} '
    
      
def is_win(user, opponent):
    if (user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') or (user == 'p' and opponent == 'r'):
        return True

print(play())