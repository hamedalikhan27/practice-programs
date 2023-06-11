# Implementation of rock, paper, scissors game
import random
def play():
    user = input("What's your choice, 'r' for rock, 'p' for paper, 's' for scissors??")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "it's a tie"
    elif (user =='r' and computer == 's') or (user =='s' and computer == 'p') or (user =='p' and computer == 's'):
             return 'You Won!'
    else:
          return 'You lost!'

print(play())    
    