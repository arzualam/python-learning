# Use module so that computer can select Random Values

import random

computer_choice = random.choice(['rock', 'paper', 'scissor'])
user_choice = input('Do you want rock, paper, or scissors?\n')

print ('Computer Choice:', computer_choice)

if computer_choice == user_choice:
   print('TIE')
elif user_choice == 'rock' and computer_choice == "scissors":
   print('You WIN')
elif user_choice == 'paper' and computer_choice == "rock":
   print('You WIN')
elif user_choice == 'scissors' and computer_choice == "paper":
   print('You WIN')
else:
    print ('You loose, Computer WINS')
