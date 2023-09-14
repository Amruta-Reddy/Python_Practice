print("Welcome to the tip calculator.")
total=float(input("What was the total bill? $"))
percent=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
persons=int(input("How many people to split the bill? "))

final_pay=(percent/100 * total +total)/persons
final=round(final_pay,2)
print(f"Each person should pay: ${final}")
