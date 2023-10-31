from tkinter import *

window = Tk()

window.title("Mile To Km Converter")
window.config(padx=10, pady=10)


def on_click():
    miles = miles_input.get()
    km = round(float(miles) * 1.609)
    converted_value.config(text=f"{km}")


miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

mile = Label(text="Miles", padx=10, pady=10)
mile.grid(row=0, column=2)

equal_to = Label(text="is equal to", padx=10, pady=10)
equal_to.grid(row=1, column=0)

converted_value = Label(text="0")
converted_value.grid(row=1, column=1)

kilometer = Label(text="Km", padx=10, pady=10)
kilometer.grid(row=1, column=2)

calculator = Button(text="Calculate", padx=3, pady=3, width=8,command=on_click)
calculator.grid(row=2, column=1)


window.mainloop()
