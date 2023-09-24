import os

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

print("Welcome to the secret auction program.")

auction_list={}


def find_highest_bidder(record):
    highest_bid=0
    winner=""
    for key in auction_list:
        x=auction_list[key]
        if x>=highest_bid:
            highest_bid=x
            winner=key
    
    print(f"The winner is {winner} with a bid of ${highest_bid}.")



bidders=True

while bidders:
    name=input("What is your name? : ")
    bid=int(input("What's your bid? : $"))
    auction_list[name]=bid
    choice=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    

    if choice=="no":
            find_highest_bidder(auction_list)
            bidders=False

