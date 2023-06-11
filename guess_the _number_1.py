import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f" Guess a number between 1 to {x}:"))
        if guess < random_number:
            print(f"wrong answer, guess again, too low")
        elif guess > random_number:
            print(f"Wrong answer, guess again, too high")
        
    print(f"yah! you have guessed the number {random_number} correctly")

guess(10)