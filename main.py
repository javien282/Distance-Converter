from tkinter import *

def calculate():
    miles = float(input.get())
    miles *= 1.6
    label_2["text"] = miles


window = Tk()
window.minsize(width=300, height=200)
window.config(padx=25, pady=25)
window.title("Mile to Km Converter")

# User to input Miles
input = Entry(width=10)
input.insert(index=0, string="0")
input.get()
input.grid(column=1, row=0)

# Label
my_label = Label(text="is equal to ", font=("Arial", 16, "normal"))
my_label.grid(column=0, row=1)

# Label 2 ("place holder numebr)
label_2 = Label(text="0", font=("Arial", 16, "normal"))
label_2.grid(column=1, row=1)

# Label 3 ("Km)
label_3 = Label(text="Km", font=("Arial", 16, "normal"))
label_3.grid(column=2, row=1)

# Label 4 ("Miles)
label_4 = Label(text="Miles", font=("Arial", 16, "normal"))
label_4.grid(column=2, row=0)

# Calculate - Start the conversion
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
