from tkinter import *

window = Tk()

window.title("Hellow")

window.geometry('450x450')

lbl = Label(window, text="choose a command:")
lbl.grid(column=16, row=0)

# btn_not = Button(window, text="")
draw_btn = Button(window, width=16, text="draw")
time_btn = Button(window, width=16, text="time")
date_btn = Button(window, width=16, text="date")
area_btn = Button(window, width=16, text="area")
area_squers_btn = Button(window, width=16, text="area_squers")
clear_btn = Button(window, width=16, text="clear")



# btn_not.grid(column=3, row=1)
draw_btn.grid(column=16, row=2)
time_btn.grid(column=16, row=3)
date_btn.grid(column=16, row=4)
area_btn.grid(column=16, row=5)
area_squers_btn.grid(column=16, row=6)
clear_btn.grid(column=16, row=7)

window.mainloop()

