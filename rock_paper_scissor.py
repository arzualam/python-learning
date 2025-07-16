# Rock, Paper, Scrissors with fixed choice by computer

computer_choice = 'scissors'
user_choice = input('Do you want rock, paper, or scissors?\n')

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
