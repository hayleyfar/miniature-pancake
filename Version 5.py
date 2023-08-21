"""
Version: 5
Date: 19.8.23
Author: Hayley Far
Description: Classes
"""

import tkinter as tk

class Cake:
    def __init__(self):
        #Ingrdients to pick from
        self.flavours = ["Black Forest", "Carrot", "Chocolate", "Coffee", "Lemon", "Matcha", "Red Velvet", "Vanilla"]
        self.toppings = ["Chocolates", "Fresh Fruit", "Macaroons", "Nuts", "Oreos", "Sprinkles", "Wafers", "Whipped Cream"]
        self.frostings = ["Caramel", "Chocolate Ganache", "Coffee", "Cream Cheese", "Hazelnut", "Lemon", "Strawberry", "Vanilla"]
        self.shapes = ["Circle", "Heart", "Square"]
        self.layers = ["2", "3", "4"]
        
    def RetrieveIngredients(self):
        #Returning the integrient lists
        return [self.flavours, self.toppings, self.frostings, self.shapes, self.layers]

class Order:
    def __init__(self, flavour, var_selected_toppings, frost, shape, layer, txt_order, btn_add, ent_message):
        selected_toppings = []
        custom_message = []
        
        for item in var_selected_toppings:
                if item.get() != "":
                    selected_toppings.append(item.get())
        custom_message.append(ent_message.get())

        if flavour == "0":
                txt_order.configure(state = tk.NORMAL)
                txt_order.delete("1.0", tk.END)
                txt_order.insert("1.0", "Please select a flavour")
                txt_order.configure(state = tk.DISABLED)
        elif frost == "0":
                txt_order.configure(state = tk.NORMAL)
                txt_order.delete("1.0", tk.END)
                txt_order.insert("1.0", "Please select a frosting")
                txt_order.configure(state = tk.DISABLED)
        elif shape == "0": 
                txt_order.configure(state = tk.NORMAL)
                txt_order.delete("1.0", tk.END)
                txt_order.insert("1.0", "Please select a shape")
                txt_order.configure(state = tk.DISABLED)
        elif layer == "0": 
                txt_order.configure(state = tk.NORMAL)
                txt_order.delete("1.0", tk.END)
                txt_order.insert("1.0", "Please select a layer")
                txt_order.configure(state = tk.DISABLED)
        else:
            txt_order.configure(state = tk.NORMAL)
            txt_order.delete("1.0", tk.END)
            txt_order.insert("1.0", "Flavour: ")
            txt_order.insert("1.9", "".join(flavour))
            txt_order.insert("2.0", "\nFrosting: ")
            txt_order.insert("2.10", "".join(frost))
            if len(selected_toppings) != 0:
                txt_order.insert("3.0", "\nToppings: ")
                txt_order.insert("4.10", ", ".join(selected_toppings))
            txt_order.insert("4.0", "\nShape: ")
            txt_order.insert("4.7", "".join(shape))
            txt_order.insert("5.0", "\nLayers: ")
            txt_order.insert("5.8", ", ".join(layer))
            if ent_message.get() != "":
                txt_order.insert("6.0", "\nCustom Message: ")
                txt_order.insert("6.16", "".join(custom_message))
            txt_order.insert("7.0", "\nCost: 'Code later' ")
            txt_order.insert(tk.END, "\n\nClick 'Clear' button to change order")
            txt_order.configure(state = tk.DISABLED)

            btn_add["state"] = tk.DISABLED


    def deselect(self, txt_order, btn_add): #txt_order may not work
        #Remove order from order screen
        txt_order.configure(state = tk.NORMAL)
        txt_order.delete("1.0", tk.END)
        txt_order.configure(state = tk.DISABLED)

        #Allows user to user button again as they removed order
        btn_add["state"] = tk.NORMAL
        
        

class Gui:
    def __init__(self, ingredients):
 
        self.frm_flavour = tk.Frame(
            window,
            width = 150,
            height = 200,
            bg = "#F0E9DF"
        )
        self.frm_flavour.grid(
            row = 1,
            column = 0,
            padx = 20
        )
        self.frm_flavour.grid_propagate(False)

        self.frm_topping = tk.Frame(
            window,
            width = 150,
            height = 200,
            bg = "#F0E9DF"
        )
        self.frm_topping.grid(
            row = 3,
            column = 0,
            rowspan = 5,
            sticky = "n"
        )
        self.frm_topping.grid_propagate(False)

        lbls = ["Flavour:", "Toppings:"]
        row = 0
        for r, text in enumerate(lbls):
            self.label = tk.Label(
                window,
                text = text,
                bg = "#F5EFE7",
                fg = "#213555"
            )
            self.label.grid(
                row = row,
                column = 0,
                padx = 20,
                pady = (10,0),
                sticky = "nw"
            )
            row += 2
            
        self.frm_frosting = tk.Frame(
            window,
            width = 150,
            height = 200,
            bg = "#F0E9DF"
        )
        self.frm_frosting.grid(
            row = 1,
            column = 1
        )
        self.frm_frosting.grid_propagate(False)

        self.frm_shape = tk.Frame(
            window,
            width = 150,
            height = 85,
            bg = "#F0E9DF"
        )
        self.frm_shape.grid(
            row = 3,
            column = 1,
            sticky = "n"
        )
        self.frm_shape.grid_propagate(False)

        self.frm_layer = tk.Frame(
            window,
            width = 150,
            height = 85,
            bg = "#F0E9DF"
        )
        self.frm_layer.grid(
            row = 5,
            column = 1,
            rowspan = 3,
            sticky = "n"
        )
        self.frm_layer.grid_propagate(False)

        text = ["Frosting:", "Shape:", "Layers:"]
        row = 0
        for r, text in enumerate(text):
            self.label = tk.Label(
                window,
                text = text,
                bg = "#F5EFE7",
                fg = "#213555"
            )
            self.label.grid(
                row = row,
                column = 1,
                pady = (10,0),
                sticky = "ws"
            )
            row += 2

        self.lbl_message = tk.Label(
            window,
            text = "Custom Message:",
            bg = "#F5EFE7",
            fg = "#213555"
        )
        self.lbl_message.grid(
            row = 8,
            column = 0,
            padx = 20,
            pady = (10,0),
            sticky = "nw"
        )

        self.ent_message = tk.Entry(
            window,
            width = 34,
            bg = "#FFFDF6",
            fg = "#4F709C"
        )
        self.ent_message.grid(
            row = 9,
            column = 0,
            columnspan = 2,
            padx = 0,
            sticky = "ne"
        )

        self.txt_order = tk.Text(
            window,
            width = 43,
            height = 17,
            state = tk.DISABLED,
            bg = "#FFFDF6",
            fg = "#4F709C"
        )
        self.txt_order.grid(
            row = 1,
            column = 2,
            rowspan = 2,
            columnspan = 2,
            padx = 30,
            sticky = "nw"
        )

        self.lbl_order = tk.Label(
            window,
            text = "Order:",
            bg = "#F5EFE7",
            fg = "#213555"
        )
        self.lbl_order.grid(
            row = 0,
            column = 2,
            padx = 30,
            sticky = "sw"
        )

        self.collect = tk.IntVar(window)
        self.pick_up = tk.Radiobutton(
            window,
            variable = self.collect,
            text = "Pick Up",
            value = "Pick Up",
            bg = "#F5EFE7",
            fg = "#4F709C"
        )
        self.pick_up.grid(
            row = 3,
            column = 2
        )
        self.delivery = tk.Radiobutton(
            window,
            variable = self.collect,
            text = "Delivery",
            value = "Delivery",
            bg = "#F5EFE7",
            fg = "#4F709C"
        )
        self.delivery.grid(
            row = 3,
            column = 3,
            sticky = "w"
        )

        labels = ["Name:", "Phone Number:", "Address:"]
        row = 4
        for r, text in enumerate(labels):
            self.label = tk.Label(
                window,
                text = text,
                bg = "#F5EFE7",
                fg = "#213555"
             )
            self.entry = tk.Entry(
                window,
                width = 34,
                bg = "#FFFDF6"
             )

            self.label.grid(
                row = row,
                column = 2,
                padx = 25,
                sticky = "sw"
             )
            self.entry.grid(
                row = row + 1,
                column = 2,
                columnspan = 2,
                sticky = "n"
             )

            row += 2


        self.var_selected_toppings = []
        for r, text in enumerate(ingredients[1]):
            self.var = tk.StringVar(window)
            self.topping = tk.Checkbutton(
            master = self.frm_topping,
            text = text,
            variable = self.var,
            onvalue = text,
            offvalue = "",
            bg = "#F0E9DF",
            fg = "#4F709C",
            )
            self.topping.grid(
                sticky = "nw",
            )
            self.var_selected_toppings.append(self.var)

        #flavours
        self.flavour = tk.StringVar(window)

        for r, text in enumerate(ingredients[0]):
            self.flvr = tk.Radiobutton(
                master = self.frm_flavour,
                text = text,
                variable = self.flavour,
                value = text,
                bg = "#F0E9DF",
                fg = "#4F709C"
            )   
            self.flvr.grid(
                sticky = "nw"
            )
        self.flavour.set(0)

        #frostings
        self.frost = tk.StringVar(window)

        for r, text in enumerate(ingredients[2]):
            self.frosting = tk.Radiobutton(
                master = self.frm_frosting,
                variable = self.frost,
                text = text,
                value = text,
                bg = "#F0E9DF",
                fg = "#4F709C"
            )
            self.frosting.grid(
                sticky = "nw"
            )
        self.frost.set(0)

        #shapes
        self.shape = tk.StringVar(window)

        for r, text in enumerate(ingredients[3]):
            self.shpe = tk.Radiobutton(
                master = self.frm_shape,
                variable = self.shape,
                text = text,
                value = text,
                bg = "#F0E9DF",
                fg = "#4F709C"
            )
            self.shpe.grid(
                sticky = "nw",
                pady = (3,0)
            )
        self.shape.set(0)

        #layers
        self.layer = tk.StringVar(window)

        for r, text in enumerate(ingredients[4]):
            self.lyr = tk.Radiobutton(
                master = self.frm_layer,
                variable = self.layer,
                text = text,
                value = text,
                bg = "#F0E9DF",
                fg = "#4F709C"
            )
            self.lyr.grid(
                sticky = "nw",
                pady = (3,0)
            )
        self.layer.set(0)

        self.btn_submit = tk.Button(
            window,
            text = "Submit",
            highlightbackground = "#F5EFE7",
            fg = "#213555"
        )
        self.btn_submit.grid(
            row = 10,
            column = 2,
            padx = 20,
            sticky = "w"
        )
        
        self.btn_add = tk.Button(
            window,
            text = "Add to Order",
            command = lambda: Order(self.flavour.get(), self.var_selected_toppings, self.frost.get(), self.shape.get(), self.layer.get(), self.txt_order, self.btn_add, self.ent_message),
            highlightbackground = "#F5EFE7",
            fg = "#213555"
        )
        self.btn_add.grid(
            row = 10,
            column = 0,
            padx = 20,
            sticky = "we"
        )

        self.btn_clear = tk.Button(
            window,
            text = "Clear",
            command = lambda: Order(self.flavour.get(), self.var_selected_toppings, self.frost.get(), self.shape.get(), self.layer.get(), self.txt_order, self.btn_add, self.ent_message).deselect(self.txt_order, self.btn_add),
            highlightbackground = "#F5EFE7",
            fg = "#213555"
        )
        self.btn_clear.grid(
            row = 10,
            column = 1,
            sticky = "w"
        )
  
        window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("700x580")
    window.title("Online Cake Ordering System")
    window.configure(bg = "#F5EFE7")
    Gui(Cake().RetrieveIngredients())
    
