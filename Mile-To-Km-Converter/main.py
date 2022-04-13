from tkinter import *

window = Tk()
window.title("Mile to Km Converter Program")
window.config(padx=40, pady=40)

# Label

lbl_miles = Label(text="Miles", font=("Arial", 16, "italic"))
lbl_miles.grid(column=2, row=0)

lbl_equal = Label(text="is equal to", font=("Arial", 16, "italic"))
lbl_equal.grid(column=0, row=1)

lbl_result = Label(text="0", font=("Arial", 16, "italic"))
lbl_result.grid(column=1, row=1)

lbl_km = Label(text="Km", font=("Arial", 16, "italic"))
lbl_km.grid(column=2, row=1)

#Buttton

def button_clicked():
    #result into the label result when clicked
    text_convert = (float(input_miles.get()) * 1.609344)
    text_convert = round(text_convert, 2)
    text_convert = str(text_convert)
    lbl_result.config(text=text_convert)


bnt_calculate = Button(text="Calculate", command=button_clicked)
bnt_calculate.grid(column=1, row=2)

#Entry

input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)
input_miles.focus()







window.mainloop() # loop to keep the window
