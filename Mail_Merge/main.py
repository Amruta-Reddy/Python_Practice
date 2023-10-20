f = open("Input\Letters\starting_letter.txt", "r")
content = f.read()

file = open("Input/Names/invited_names.txt", "r")
list_of_names = file.readlines()


for name in list_of_names:
    y=name.strip()
    x = content.replace("[name]", y)
    with open(f"Output/ReadyToSend/letter_for_{y}.txt", "w") as invited_file:
        invited_file.write(x)

f.close()
file.close()
