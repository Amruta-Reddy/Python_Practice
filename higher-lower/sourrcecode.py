from game_data import data
import random
import os


logo="""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

"""

print(logo)




def compare_followers(guess,followers_A,followers_B):
    if followers_A > followers_B:
        return guess=='A'
    else:
        return guess=='B'




score=0
play_game=True



while play_game:
    A=random.choice(data)
    B=random.choice(data)
    if A==B:
        b=random.choice(data)
    followers_A=A['follower_count']
    followers_B=B['follower_count']


    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")



    print('''

     _    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____(_)

    ''')



    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

    guess=input("Who has more followers? Type 'A' or 'B' :  ").upper()


    is_correct=compare_followers(guess,followers_A,followers_B)
    os.system('cls')
    print(logo)
    if is_correct:
        score+=1
        print(f"You're rigth! Current score: {score}")

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        play_game=False

    
    







