"""
Version: 1
Date: 26/7/23
Author: Hayley Far
Description: Creating the grid layout for the GUI

"""

import tkinter as tk

window=tk.Tk()
window.geometry("500x600")
window.title("Online Cake Ordering System")


frame1=tk.Frame(window, width=150, height=200, bg="Blue") #flavour colour
frame1.grid(row=1, column=0, padx=20)

lbl = tk.Label(window, text = "Flavour:") #flavour text
lbl.grid(row=0, column=0, padx=20, pady=(10,0), sticky="nw") #padding(top, bottom)


frame2=tk.Frame(window, width=150, height=80, bg="red")
frame2.grid(row=3, column=0, sticky="n")

lbl2 = tk.Label(window, text = "Toppings:")
lbl2.grid(row=2, column=0, padx=20, pady=(10,0), sticky="nw")

framr = tk.Frame(window, width=150, height=30, bg="red")
framr.grid(row=4, column=0, pady=0, sticky="n")

framm = tk.Frame(window, width=150, height=80, bg ="red")
framm.grid(row=5, column=0, pady=0, sticky="n")



frame3=tk.Frame(window, width=150, height=200, background="Green")
frame3.grid(row=1, column=1)

lbl3 = tk.Label(window, text = "Frosting:")
lbl3.grid(row=0, column=1, pady=(10,0), sticky="nw") #padding(top, bottom)




frame4=tk.Frame(window, width=150, height=80, background="Yellow")
frame4.grid(row=3, column=1, sticky ="n")

lbl4 = tk.Label(window, text = "Shape:")
lbl4.grid(row=2, column=1, pady=(10,0), sticky="nw") #padding(top, bottom)




frame5=tk.Frame(window, width=150, height=80, background="Pink")
frame5.grid(row=5, column=1, sticky="n")


lbl5 = tk.Label(window, text = "Layers:")
lbl5.grid(row=4, column=1, pady=0, sticky="ws") #padding(top, bottom)





window.mainloop()
