"""
Version: 4
Date: 14.8.23
Author: Hayley Far
Description: Displaying selected
options
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
    bg = "#FFFDF6",
    fg = "#4F709C"
) 
ent_message.grid(
    row = 9,
    column = 0,
    columnspan = 2,
    padx = 0,
    sticky = "ne"
)

#text for displaying cake order
txt_order = tk.Text(
    window,
    width = 43,
    height = 17,
    state = tk.DISABLED,
    bg = "#FFFDF6"
)
txt_order.grid(
    row = 1,
    column = 2,
    rowspan = 2,
    columnspan = 2,
    padx = 30,
    sticky = "nw"
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
""" included the code above in classes"""
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
        padx = 25,
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

def add_to_order():
    #adding selected options into empty lists
    selected_toppings = []
    selected_flavour = []
    selected_frosting = []
    selected_shape = []
    selected_layer = []
    custom_message = []
    
    for topping in var_selected_toppings:
        if topping.get() != "":
            selected_toppings.append(topping.get())

    selected_flavour.append(flavour.get())
    selected_frosting.append(frost.get())
    selected_shape.append(shape.get())
    selected_layer.append(layer.get())
    custom_message.append(ent_message.get())
    
    
    #if statement to ensure user selects required options
    if "0" in selected_flavour or "0" in selected_frosting or "0" in selected_shape or "0" in selected_layer:
        txt_order.configure(state = tk.NORMAL)
        txt_order.delete("1.0", tk.END)
        txt_order.insert("1.0", "Please select a flavour, frosting flavour, shape and number of layers")
        txt_order.configure(state = tk.DISABLED)
        return
    else:
        pass

    #printing users order in the order screen
    txt_order.configure(state = tk.NORMAL)
    txt_order.delete("1.0", tk.END)
    txt_order.insert("1.0", "Flavour: ")
    txt_order.insert("1.9", "".join(selected_flavour))
    txt_order.insert("2.0", "\nFrosting: ")
    txt_order.insert("2.10", "".join(selected_frosting))
    if len(selected_toppings) != 0:
        txt_order.insert("3.0", "\nToppings: ")
        txt_order.insert("4.10", ", ".join(selected_toppings))
    txt_order.insert("4.0", "\nShape: ")
    txt_order.insert("4.7", "".join(selected_shape))
    txt_order.insert("5.0", "\nLayers: ")
    txt_order.insert("5.8", ", ".join(selected_layer))
    if len(ent_message.get()) != 0:
        txt_order.insert("6.0", "\nCustom Message: ")
        txt_order.insert("6.16", "".join(custom_message))
    txt_order.insert("7.0", "\nCost: 'Code later' ")
    txt_order.insert(tk.END, "\n\nClick 'Clear' button to change order")
    txt_order.configure(state = tk.DISABLED)

    btn_add["state"] = tk.DISABLED


def deselect():
    #remove order from order screen
    txt_order.configure(state = tk.NORMAL)
    txt_order.delete("1.0", tk.END)
    txt_order.configure(state = tk.DISABLED)

    #allows user to user button again as they removed order
    btn_add["state"] = tk.NORMAL

   
#check buttons for topping options
toppings = ["Chocolates", "Fresh Fruit", "Macaroons",
            "Nuts", "Oreos", "Sprinkles", "Wafers",
            "Whipped Cream"]
var_selected_toppings = []
 
for r, text in enumerate(toppings):
    var = tk.StringVar(window)
    topping = tk.Checkbutton(
        master = frm_topping,
        text = text,
        variable = var,
        onvalue = text,
        offvalue = "",
        bg = "#F0E9DF",
        fg = "#4F709C",
    )
    topping.grid(
        sticky = "nw",
    )
    var_selected_toppings.append(var)


#radio buttons for flavour (flvr) options
flavours = ["Black Forest", "Carrot", "Chocolate", "Coffee",
            "Lemon", "Matcha", "Red Velvet", "Vanilla"]
flavour = tk.StringVar(window)

for r, text in enumerate(flavours):
    flvr = tk.Radiobutton(
        master = frm_flavour,
        text = text,
        variable = flavour,
        value = text,
        bg = "#F0E9DF",
        fg = "#4F709C"
    )   
    flvr.grid(
        sticky = "nw"
    )
flavour.set(0)

#radio buttons for frosting (frost) options
frostings = ["Caramel", "Chocolate Ganache", "Coffee",
             "Cream Cheese", "Hazelnut", "Lemon", "Strawberry",
             "Vanilla"]
frost = tk.StringVar(window)

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
frost.set(0)

#radio buttons for shape options
shapes = ["Circle", "Heart", "Square"]
shape = tk.StringVar(window)

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
shape.set(0)

#radio buttons for layer (lyr) options
layers = ["2", "3", "4"]
layer = tk.StringVar(window)

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
layer.set(0)

#button for adding order
btn_add = tk.Button(
    window,
    text = "Add to Order",
    command = add_to_order,
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
    command = deselect,
    highlightbackground = "#F5EFE7",
    fg = "#213555"
)
btn_clear.grid(
    row = 10,
    column = 1,
    sticky = "w"
)

window.mainloop()
