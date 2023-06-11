# In this program you have to choose a number between 1 to 100 and computer will guess the number
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} is high (H) or low (L) or correct (C): ").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    
    print(f'yah! computer has guessed your number {guess} correctly!')

computer_guess(100)
