import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too low!')
        elif guess > random_number:
            print('Too high')
    
    print(f'Nice {guess} is the correct number which was {random_number}')

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low  (L), or correct (C)??").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f"Correct guess computer: it was {guess}")
        
user_input = int(input("User please provide a number for computer to guess: "))
comp_guess(user_input)
        