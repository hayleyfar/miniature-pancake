"""
Version: 3
Date: 9.8.23
Author: Hayley Far
Description: Creating checkboxes
for the different options.
"""

import tkinter as tk
#from tkinter import font
#lbl_font = font.Font(size = 14)

window = tk.Tk()
window.geometry("700x580")
window.title("Online Cake Ordering System")
window.configure(bg = "#F5EFE7")


#frame for flavour options
frm_flavour = tk.Frame(
    window,
    width = 150,
    height = 200,
    bg = "#F0E9DF"
)
frm_flavour.grid(
    row = 1,
    column = 0,
    padx = 20
)
#to keep the frame the same with checkboxes
frm_flavour.grid_propagate(False)

#frame for topping options
frm_topping = tk.Frame(
    window,
    width = 150,
    height = 200,
    bg = "#F0E9DF"
)
frm_topping.grid(
    row = 3,
    column = 0,
    rowspan = 5,
    sticky = "n"
)
frm_topping.grid_propagate(False)

#for loop for the labels in column 0
lbls = ["Flavour:", "Toppings:"]
row = 0
for r, text in enumerate(lbls):
    label = tk.Label(
        window,
        text = text,
        bg = "#F5EFE7",
        fg = "#213555"
     )
    label.grid(
        row = row,
        column = 0,
        padx = 20,
        pady = (10,0),
        sticky = "nw"
     )
    row += 2

#frame for frosting options
frm_frosting = tk.Frame(
    window,
    width = 150,
    height = 200,
    bg = "#F0E9DF"
)
frm_frosting.grid(
    row = 1,
    column = 1
)
frm_frosting.grid_propagate(False)

#frame for shape options
frm_shape = tk.Frame(
    window,
    width = 150,
    height = 85,
    bg = "#F0E9DF"
)
frm_shape.grid(
    row = 3,
    column = 1,
    sticky = "n"
)
frm_shape.grid_propagate(False)

#frame for layer options
frm_layer = tk.Frame(
    window,
    width = 150,
    height = 85,
    bg = "#F0E9DF"
)
frm_layer.grid(
    row = 5,
    column = 1,
    rowspan = 3,
    sticky = "n"
)
frm_layer.grid_propagate(False)

#for loop for the labels in column 1
text = ["Frosting:", "Shape:", "Layers:"]
row = 0
for r, text in enumerate(text):
    label = tk.Label(
        window,
        text = text,
        bg = "#F5EFE7",
        fg = "#213555"
     )
    label.grid(
        row = row,
        column = 1,
        pady = (10,0),
        sticky = "ws"
     )
    row += 2

#label for custom messages
lbl_message = tk.Label(
    window,
    text = "Custom Message:",
    bg = "#F5EFE7",
    fg = "#213555"
)
lbl_message.grid(
    row = 8,
    column = 0,
    padx = 20,
    pady = (10,0),
    sticky = "nw"
)

#text box for custom messages
ent_message = tk.Entry(
    window,
    width = 34,
    bg = "#FFFDF6"
) 
ent_message.grid(
    row = 9,
    column = 0,
    columnspan = 2,
    padx = 0,
    sticky = "ne"
)

#button for adding order
btn_add = tk.Button(
    window,
    text = "Add to Order",
    highlightbackground = "#F5EFE7",
    fg = "#213555"
)
btn_add.grid(
    row = 10,
    column = 0,
    padx = 20,
    sticky = "we"
)

#button for clearing
#use deselect
btn_clear = tk.Button(
    window,
    text = "Clear",
    highlightbackground = "#F5EFE7",
    fg = "#213555"
)
btn_clear.grid(
    row = 10,
    column = 1,
    sticky = "w"
)

#frame for displaying cake order
frm_order = tk.Frame(
    window,
    width = 300,
    height = 230,
    bg = "#FFFDF6"
)
frm_order.grid(
    row = 1,
    column = 2,
    rowspan = 2,
    columnspan = 2,
    padx = 30,
    sticky = "n"
)

#label for order
lbl_order = tk.Label(
    window,
    text = "Order:",
    bg = "#F5EFE7",
    fg = "#213555"
)
lbl_order.grid(
    row = 0,
    column = 2,
    padx = 30,
    sticky = "sw"
)

#radio buttons for collection type 
collect = tk.IntVar(window)

#pick up
pick_up = tk.Radiobutton(
    window,
    variable = collect,
    text = "Pick Up",
    value = "Pick Up",
    bg = "#F5EFE7",
    fg = "#4F709C"
)
pick_up.grid(
    row = 3,
    column = 2
)

#delivery
delivery = tk.Radiobutton(
    window,
    variable = collect,
    text = "Delivery",
    value = "Delivery",
    bg = "#F5EFE7",
    fg = "#4F709C"
)
delivery.grid(
    row = 3,
    column = 3,
    sticky = "w"
)


#creating the admin section of the GUI
labels = ["Name:", "Phone Number:", "Address:"]
row = 4
for r, text in enumerate(labels):
    label = tk.Label(
        window,
        text = text,
        bg = "#F5EFE7",
        fg = "#213555"
     )
    entry = tk.Entry(
        window,
        width = 34,
        bg = "#FFFDF6"
     )

    label.grid(
        row = row,
        column = 2,
        padx = 20,
        sticky = "sw"
     )
    entry.grid(
        row = row + 1,
        column = 2,
        columnspan = 2,
        sticky = "n"
     )

    row += 2

#button to submit order
btn_submit = tk.Button(
    window,
    text = "Submit",
    highlightbackground = "#F5EFE7",
    fg = "#213555"
)
btn_submit.grid(
    row = 10,
    column = 2,
    padx = 20,
    sticky = "w"
)

#check buttons for topping options
toppings = ["Chocolates", "Fresh Fruit", "Macaroons",
            "Nuts", "Oreos", "Sprinkles", "Wafers",
            "Whipped Cream"]

for r, text in enumerate(toppings):
    topping = tk.Checkbutton(
        master = frm_topping,
        text = text,
        bg = "#F0E9DF",
        fg = "#4F709C"
    )
    topping.grid(
        sticky = "nw",
    )

#radio buttons for flavour (flvr) options
flavour = tk.IntVar(window)
flavours = ["Black Forest", "Carrot", "Chocolate", "Coffee",
            "Lemon", "Matcha", "Red Velvet", "Vanilla"]

for r, text in enumerate(flavours):
    flvr = tk.Radiobutton(
        master = frm_flavour,
        variable = flavour,
        text = text,
        value = text,
        bg = "#F0E9DF",
        fg = "#4F709C"
    )   
    flvr.grid(
        sticky = "nw"
    )

#radio buttons for frosting (frost) options
frost = tk.IntVar(window) 
frostings = ["Caramel", "Chocolate Ganache", "Coffee",
             "Cream Cheese", "Hazelnut", "Lemon", "Strawberry",
             "Vanilla"]

for r, text in enumerate(frostings):
    frosting = tk.Radiobutton(
        master = frm_frosting,
        variable = frost,
        text = text,
        value = text,
        bg = "#F0E9DF",
        fg = "#4F709C"
    )
    frosting.grid(
        sticky = "nw"
    )

#radio buttons for shape options
shape = tk.IntVar(window) 
shapes = ["Circle", "Heart", "Square"]

for r, text in enumerate(shapes):
    shpe = tk.Radiobutton(
        master = frm_shape,
        variable = shape,
        text = text,
        value = text,
        bg = "#F0E9DF",
        fg = "#4F709C"
    )
    shpe.grid(
        sticky = "nw",
        pady = (3,0)
    )

#radio buttons for layer (lyr) options
layer = tk.IntVar(window) 
layers = [2, 3, 4]
for r, text in enumerate(layers):
    lyr = tk.Radiobutton(
        master = frm_layer,
        variable = layer,
        text = text,
        value = text,
        bg = "#F0E9DF",
        fg = "#4F709C"
    )
    lyr.grid(
        sticky = "nw",
        pady = (3,0)
    )

window.mainloop()
