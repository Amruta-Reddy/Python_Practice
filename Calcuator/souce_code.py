import os



def add(n1,n2):
    return n1+n2


def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2




def calculator():
    print('''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
''')
    num1=float(input("What's the first number? : "))

    operations_list={
        "+":add, 
        "-":subtract,
        "*":multiply,
        "/":divide
    } 

    for key in operations_list: 
        print(key)


    perform_calculation=True

    answer=num1

    while perform_calculation:
        symbol=input("pick an operation: ")
        num2=float(input("What's the second number? : "))
        
        calculation=operations_list[symbol]
        num=answer
        answer=calculation(answer,num2)
        print(f"{num} {symbol} {num2} = {answer}")

        choice=input(f"Type 'y' to continue calculating with {answer}, or type 'r' to start fresh, or type 'n' to exit. : ").lower()
        if choice=='r':
            perform_calculation=False
            os.system('cls')
            calculator()
        if choice=='n':
            perform_calculation=False


calculator()








