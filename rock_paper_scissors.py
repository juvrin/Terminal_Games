#exercises from www.practicepython.org

#exercise 8 
#against computer version (one player)
import random

while True:
    user_choice = str(input("Type rock, paper or scissors: "))
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    comp_choice = random.choice(list(game_dict.keys()))
    a = game_dict.get(user_choice)
    b = game_dict.get(comp_choice)
    dif = a - b
    if dif in [-1, 2]:
        print(f"You win! Because {user_choice} beats {comp_choice}")
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print(f"You loose! Because {comp_choice} beats {user_choice}")
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print("It's a draw.")

