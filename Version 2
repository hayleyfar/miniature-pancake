"""
Version: 2
Date: 6.8.23
Author: Hayley Far
Description: Adding colour!
"""

import tkinter as tk

window = tk.Tk()
window.geometry("700x580")
window.title("Online Cake Ordering System")
window.configure(bg = "#F5EFE7")


#frames for the labels below
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

#for loop for the labels
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

#frames for the labels below
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

#for loop for the labels
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

#custom message text
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

#custom message text box
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

#add users order to order text box button
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

#clear button
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

#order frame
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

#order text
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

#pick up
lbl_pick_up = tk.Label(
    window,
    text = "Pick Up",
    bg = "#F5EFE7",
    fg = "#213555")
lbl_pick_up.grid(
    row = 3,
    column = 2
)

#delivery 
lbl_pick_up = tk.Label(
    window,
    text = "Delivery",
    bg = "#F5EFE7",
    fg = "#213555"
)
lbl_pick_up.grid(
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

#submit button
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

window.mainloop()
