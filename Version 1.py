"""
Version: 1
Date: 28/7/23
Author: Hayley Far
Description: Creating the grid layout for the GUI

"""

import tkinter as tk

window=tk.Tk()
window.geometry("700x600")
window.title("Online Cake Ordering System")
#window.resizeable(False, False)


frm_flavour=tk.Frame(window, width=150, height=200, bg="Blue") #flavour colour
frm_flavour.grid(row=1, column=0, padx=20)

lbl_flavour = tk.Label(window, text = "Flavour:") #flavour text
lbl_flavour.grid(row=0, column=0, padx=20, pady=(10,0), sticky="nw") #padding(top, bottom)


frm_topping=tk.Frame(window, width=150, height=200, bg="red")
frm_topping.grid(row=3, column=0, rowspan=5, sticky="n")

lbl_topping = tk.Label(window, text = "Toppings:")
lbl_topping.grid(row=2, column=0, padx=20, pady=(10,0), sticky="nw")


frm_frosting=tk.Frame(window, width=150, height=200, background="Green")
frm_frosting.grid(row=1, column=1)

lbl_frosting = tk.Label(window, text = "Frosting:")
lbl_frosting.grid(row=0, column=1, pady=(10,0), sticky="nw") #padding(top, bottom)



frm_shape=tk.Frame(window, width=150, height=85, background="Yellow")
frm_shape.grid(row=3, column=1, sticky ="n")

lbl_shape = tk.Label(window, text = "Shape:")
lbl_shape.grid(row=2, column=1, pady=(10,0), sticky="nw") #padding(top, bottom)



frm_layer=tk.Frame(window, width=150, height=85, background="Pink")
frm_layer.grid(row=5, column=1, rowspan=3, sticky="n")


lbl_layer = tk.Label(window, text = "Layers:")
lbl_layer.grid(row=4, column=1, pady=0, sticky="ws") #padding(top, bottom)

lbl_message = tk.Label(window, text = "Custom Message:")
lbl_message.grid(row=8, column=0, padx=20, pady=(10,0), sticky="nw")

ent_message = tk.Entry(window, width = 34) 
ent_message.grid(row=9, column=0, columnspan=2, padx=0, sticky="ne")

btn_add = tk.Button(window, text="Add to Order")
btn_add.grid(row=10, column=0, sticky="we", padx = 20)

btn_clear = tk.Button(window, text="Clear")
btn_clear.grid(row=10, column=1, sticky="w")

frm_order=tk.Frame(window, width=300, height=230, bg="purple")
frm_order.grid(row=1, column=2, rowspan=2, columnspan=2, padx=30, sticky="n")

lbl_order=tk.Label(window, text="Order:")
lbl_order.grid(row=0, column=2, padx=30, sticky="sw")


lbl_pick_up=tk.Label(window, text = "Pick Up")
lbl_pick_up.grid(row=3, column=2)

lbl_pick_up=tk.Label(window, text = "Delivery")
lbl_pick_up.grid(row=3, column=3, sticky="w")

lbl_name=tk.Label(window, text="Name:")
lbl_name.grid(row=4, column=2, padx=20, sticky="w")

ent_name=tk.Entry(window, width=34)
ent_name.grid(row=5, column=2, columnspan=2, sticky="n")

lbl_number=tk.Label(window, text="Phone Number:")
lbl_number.grid(row=6, column=2, padx=20, sticky="w")

ent_number=tk.Entry(window, width=34)
ent_number.grid(row=7, column=2, columnspan=2, sticky="n")

lbl_address=tk.Label(window, text="Address:")
lbl_address.grid(row=8, column=2, padx=20, sticky="w")

ent_address=tk.Entry(window, width=34)
ent_address.grid(row=9, column=2, columnspan=2, sticky="n")


btn_submit = tk.Button(window, text="Submit")
btn_submit.grid(row=10, column=2, padx=20, sticky="w")


window.mainloop()
