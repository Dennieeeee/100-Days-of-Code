rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_image = [rock, paper, scissors]
user_choice = int(input('Pick a number: 1 (rock), 2 (paper), 3 (scissors): '))
computer_choice = random.randint(0,2)
if user_choice >= 3 or user_choice < 0:
    print('Invalid Input, You Lose!')
else:
    print(game_image[user_choice])
    print('Computer choose: ',game_image[computer_choice])
    if user_choice > computer_choice:
        print('You win!')
    elif user_choice < computer_choice:
        print('You Lose!')
    else:
        print('Tie.')
