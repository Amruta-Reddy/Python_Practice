import random


print('''

 _____                       _____ _                                   _               
|  __ \                     |_   _| |                                 | |              
| |  \/_   _  ___  ___ ___    | | | |__   ___    _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|   | | | '_ \ / _ \  | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \   | | | | | |  __/  | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/   \_/ |_| |_|\___|  |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                       
                                                                                       

''')



print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

number_to_be_guessed=random.randint(1,100)


def compare_number(number_to_be_guessed,guessed_number):
    if number_to_be_guessed > guessed_number:
        print("Too Low")
        print("Guess again")
    elif number_to_be_guessed < guessed_number:
        print("Too High")
        print("Guess again")
    else:
        print(f"You got it! The answer was {number_to_be_guessed}")
        



def play_game(n):
    while n>=0:
        print(f"You have {n} attempts remaining to guess the number.")
        guessed_number=int(input("Make a guess: "))
        compare_number(number_to_be_guessed,guessed_number)
        if number_to_be_guessed == guessed_number:
            break
        n=n-1
        if n==0:
            print("You've run out of guesses, you loose")
            print(f"The actual answer is {number_to_be_guessed}")
            break





choose=input("Choose a difficulty. Type 'easy' or 'medium' or 'hard' :  ")
if choose=='hard':
    play_game(3)

elif choose=='medium':
    play_game(6)

else:
    play_game(10)
    
