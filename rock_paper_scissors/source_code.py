import random

player=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computer=random.randint(0,2)



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



if player==0:
    print(rock)
    print("computer choice")
    if computer==0:
        print(rock)
        print("Match Draw")
    elif computer==1:
        print(paper)
        print("You Lose")
    else:
        print(scissors)
        print("You win")

elif player==1:
    print(paper)
    print("computer choice")
    if computer==0:
        print(rock)
        print("You Win")
    elif computer==1:
        print(paper)
        print("Match Draw")
    else:
        print(scissors)
        print("You Lose")

else:
    print(scissors)
    if computer==0:
        print(rock)
        print("You Lose")
    elif computer==1:
        print(paper)
        print("You Win")
    else:
        print(scissors)
        print("Match Draw")
    
