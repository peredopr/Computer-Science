from tkinter import *

window = Tk()
window.title('Kilometer to Miles Converter')
window.config(padx=10, pady=10)

def km_to_miles():
    km = float(km_input.get())
    miles = km * 1.609
    miles_value_label.config(text=f'{miles}')

km_input = Entry(width=15)
km_input.grid(column=1, row=0)

km_label = Label(text='Kilometer')
km_label.grid(column=2, row=0)

equal_to_label = Label(text='Is equal to')
equal_to_label.grid(column=0, row=1)

miles_value_label = Label(text='0')
miles_value_label.grid(column=1, row=1)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate', command=km_to_miles)
calculate_button.grid(column=1, row=2)





window.mainloop()