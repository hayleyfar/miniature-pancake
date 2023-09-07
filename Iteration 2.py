"""Iteration 2.

Date: 8.9.23

Author: Hayley Far

Description: Fixing pick up/delivery and making cost bold
"""

import tkinter as tk


class Cake:
    """Holds the different options."""

    def __init__(self):
        """Ingrdients to pick from."""
        self.flavours = [
            "Black Forest", "Carrot",
            "Chocolate", "Coffee", "Lemon",
            "Matcha", "Red Velvet", "Vanilla"
        ]
        self.toppings = [
            "Chocolates", "Fresh Fruit",
            "Macaroons", "Nuts", "Oreos",
            "Sprinkles", "Wafers", "Whipped Cream"
        ]
        self.frostings = [
            "Caramel", "Chocolate Ganache", "Coffee",
            "Cream Cheese", "Hazelnut", "Lemon",
            "Strawberry", "Vanilla"
        ]
        self.shapes = ["Circle", "Heart", "Square"]
        self.layers = ["2", "3", "4"]

    def retrieve_ingredients(self):
        """Return the integrient lists."""
        return [
            self.flavours, self.toppings,
            self.frostings, self.shapes, self.layers
        ]

class Order:
    """Retrive and print the user's order."""

    def __init__(self, flavour, var_selected_toppings, frost, shape,
                 layer, txt_order, btn_add, btn_clear, btn_submit,
                 ent_message, user_details):
        """Check order is valid."""
        custom_message = []
        selected_toppings = []

        # Adding the user selected toppings into a list
        if len(selected_toppings) == 0:
            for item in var_selected_toppings:
                if item.get() != "":
                    selected_toppings.append(item.get())

        # Adding the user's message to a list
        if ent_message.get() != "":
            custom_message.append(ent_message.get())

        # Checking if the users order is valid
        if flavour == "0":
            txt_order.configure(state=tk.NORMAL)
            txt_order.delete("1.0", tk.END)
            txt_order.insert("1.0", "Please select a flavour")
            txt_order.configure(state=tk.DISABLED)
        elif frost == "0":
            txt_order.configure(state=tk.NORMAL)
            txt_order.delete("1.0", tk.END)
            txt_order.insert("1.0", "Please select a frosting")
            txt_order.configure(state=tk.DISABLED)
        elif shape == "0":
            txt_order.configure(state=tk.NORMAL)
            txt_order.delete("1.0", tk.END)
            txt_order.insert("1.0", "Please select a shape")
            txt_order.configure(state=tk.DISABLED)
        elif layer == "0":
            txt_order.configure(state=tk.NORMAL)
            txt_order.delete("1.0", tk.END)
            txt_order.insert("1.0", "Please select a layer")
            txt_order.configure(state=tk.DISABLED)
        else:
            # Calculating the costs of the cake
            value = 30
            for topping in selected_toppings:
                value += 1
            if layer == "2":
                value += 2
            elif layer == "3":
                value += 4
            elif layer == "4":
                value += 6
            if len(custom_message) != 0:
                value += 1.5
            if "Address" in user_details and len(user_details["Address"]) != 0:
                value += 5
            self.print_order(
                flavour, selected_toppings,
                frost, shape, layer,
                txt_order, btn_add, btn_clear,
                btn_submit, custom_message, user_details,
                value
            )

    def deselect(self, txt_order, btn_add):
        """Remove order from order screen."""
        txt_order.configure(state=tk.NORMAL)
        txt_order.delete("1.0", tk.END)
        txt_order.configure(state=tk.DISABLED)

        # Allows user to use button again as they removed order
        btn_add["state"] = tk.NORMAL

    def collecting(self, collect, entries, txt_order, flavour,
                   var_selected_toppings, frost, shape, layer,
                   btn_add, btn_clear, btn_submit, ent_message,
                   user_details, pick_up, delivery):
        """Check if the user has ordered first."""
        button = str(btn_add["state"])
        if button == "normal":
            txt_order.configure(state=tk.NORMAL)
            txt_order.delete("1.0", tk.END)
            txt_order.insert("1.0", "Please place an order first")

        # Checking that users collection type
        elif collect != "Pick Up" and collect != "Delivery":
            txt_order.configure(state=tk.NORMAL)
            txt_order.delete("1.0", tk.END)
            txt_order.insert("1.0", "Please select pick up or delivery")
        elif collect == "Pick Up":
            entries[2].configure(state=tk.DISABLED)
            self.check_details(
                collect, entries, txt_order, flavour,
                var_selected_toppings, frost, shape,
                layer, btn_add, btn_clear, btn_submit,
                ent_message, user_details, pick_up, delivery
            )
        elif collect == "Delivery":
            entries[2].configure(state=tk.NORMAL)
            self.check_details(
                collect, entries, txt_order, flavour,
                var_selected_toppings, frost, shape, layer, btn_add,
                btn_clear, btn_submit, ent_message, user_details,
                pick_up, delivery
            )

    def check_details(self, collect, entries, txt_order, flavour,
                      var_selected_toppings, frost, shape, layer,
                      btn_add, btn_clear, btn_submit, ent_message,
                      user_details, pick_up, delivery):
        """Check user's details."""
        # Adding keys and values into the empty dictionary
        list = ["Name", "Number", "Address"]
        i = 0
        for entry in entries:
            ent = entry.get()
            user_details[list[0+i]] = ent
            i += 1

        # Adding selected toppings and custom message to lists
        custom_message = []
        selected_toppings = []
        if len(selected_toppings) == 0:
            for item in var_selected_toppings:
                if item.get() != "":
                    selected_toppings.append(item.get())
        if ent_message.get() != "":
            custom_message.append(ent_message.get())

        # Retrieving the value from each key in the dictionary
        name = user_details.get("Name")
        number = user_details.get("Number")
        address = user_details.get("Address")
        # Check name has no integers
        integer = any(chr.isdigit() for chr in name)
        # Allow phone number to have spaces
        phone = number.replace(" ", "")

        # Checking user details are valid
        if name == "" or integer is True:
            txt_order.configure(state=tk.NORMAL)
            txt_order.delete("1.0", tk.END)
            txt_order.insert("1.0", "Please put your name in (and not digits)")
            txt_order.configure(state=tk.DISABLED)
        elif phone.isdigit() is not True or len(number) < 9:
            txt_order.configure(state=tk.NORMAL)
            txt_order.delete("1.0", tk.END)
            txt_order.insert("1.0", "Your phone number is not valid")
            txt_order.configure(state=tk.DISABLED)
        elif collect == "Delivery" and address == "":
            txt_order.configure(state=tk.NORMAL)
            txt_order.delete("1.0", tk.END)
            txt_order.insert("1.0", "Please enter your address for delivery")
            txt_order.configure(state=tk.DISABLED)
        else:
            # Runs when everything is valid (order and details)
            btn_clear["state"] = tk.DISABLED
            btn_submit["state"] = tk.DISABLED
            pick_up["state"] = tk.DISABLED
            delivery["state"] = tk.DISABLED
            Order(flavour, var_selected_toppings, frost, shape,
                  layer, txt_order, btn_add, btn_clear, btn_submit,
                  ent_message, user_details)

    def print_order(self, flavour, selected_toppings, frost, shape,
                    layer, txt_order, btn_add, btn_clear, btn_submit,
                    custom_message, user_details, value):
        """Print user's order in txt_order."""

        # Collecting the cost in a list and making it to 2 dp
        charge = []
        price = "{0:.2f}".format(value)
        if len(charge) == 0:
            charge.append(price)

        # Printing the cake order
        txt_order.configure(state=tk.NORMAL)
        txt_order.delete("1.0", tk.END)
        txt_order.insert("1.0", "Flavour: ")
        txt_order.insert("1.9", "".join(flavour))
        txt_order.insert("3.0", "\nFrosting: ")
        txt_order.insert("3.10", "".join(frost))
        if len(selected_toppings) != 0:
            txt_order.insert("4.0", "\nToppings: ")
            txt_order.insert("4.10", ", ".join(selected_toppings))
        txt_order.insert("5.0", "\nShape: ")
        txt_order.insert("5.7", "".join(shape))
        txt_order.insert("6.0", "\nLayers: ")
        txt_order.insert("6.8", ", ".join(layer))
        if len(custom_message) != 0:
            txt_order.insert("7.0", "\nCustom Message: ")
            txt_order.insert("7.16", "".join(custom_message))
        # Bold cost
        txt_order.tag_configure("bold", font="Lucinds 12 bold")
        txt_order.insert("8.0", "\n\nCost: $", "bold")
        txt_order.insert("8.7", charge, "bold")

        # Printing the user's details
        if len(user_details) != 0:
            txt_order.configure(state=tk.NORMAL)
            txt_order.insert("10.0", "\n\nName: ")
            txt_order.insert("10.6", "".join(user_details["Name"]))
            txt_order.insert("11.0", "\nPhone Number: ")
            txt_order.insert("11.14", "".join(user_details["Number"]))
            if len(user_details["Address"]) != 0:
                txt_order.insert("12.0", "\nAddress: ")
                txt_order.insert("12.9", "".join(user_details["Address"]))
            txt_order.insert("13.0", "\n\nYour order has been submitted!")
            txt_order.configure(state=tk.DISABLED)
        txt_order.insert(tk.END, "\n\nClick 'Clear' button to change order")
        txt_order.configure(state=tk.DISABLED)

        btn_add["state"] = tk.DISABLED
        return value

class Gui:
    """Layout of the GUI."""

    def __init__(self, ingredients):
        """Create elements for window."""
        # Empty dictionary which is called and edited
        user_details = {}

        # Creating the frames for other widgets
        self.frm_flavour = tk.Frame(
            window,
            width=150,
            height=200,
            bg="#F0E9DF"
        )
        self.frm_flavour.grid(
            row=1,
            column=0,
            padx=20
        )
        self.frm_flavour.grid_propagate(False)  # Maintains frame attributes

        self.frm_topping = tk.Frame(
            window,
            width=150,
            height=200,
            bg="#F0E9DF"
        )
        self.frm_topping.grid(
            row=3,
            column=0,
            rowspan=5,
            sticky="n"
        )
        self.frm_topping.grid_propagate(False)

        # Creating labels in first column
        lbls = ["Flavour:", "Toppings:"]
        row = 0
        for r, text in enumerate(lbls):
            self.label = tk.Label(
                window,
                text=text,
                bg="#F5EFE7",
                fg="#213555"
            )
            self.label.grid(
                row=row,
                column=0,
                padx=20,
                pady=(10, 0),
                sticky="nw"
            )
            row += 2

        # Creating the frames for other widgets
        self.frm_frosting = tk.Frame(
            window,
            width=150,
            height=200,
            bg="#F0E9DF"
        )
        self.frm_frosting.grid(
            row=1,
            column=1
        )
        self.frm_frosting.grid_propagate(False)

        self.frm_shape = tk.Frame(
            window,
            width=150,
            height=85,
            bg="#F0E9DF"
        )
        self.frm_shape.grid(
            row=3,
            column=1,
            sticky="n"
        )
        self.frm_shape.grid_propagate(False)

        self.frm_layer = tk.Frame(
            window,
            width=150,
            height=85,
            bg="#F0E9DF"
        )
        self.frm_layer.grid(
            row=5,
            column=1,
            rowspan=3,
            sticky="n"
        )
        self.frm_layer.grid_propagate(False)

        # Creating labels in 2nd column
        text = ["Frosting:", "Shape:", "Layers:"]
        row = 0
        for r, text in enumerate(text):
            self.label = tk.Label(
                window,
                text=text,
                bg="#F5EFE7",
                fg="#213555"
            )
            self.label.grid(
                row=row,
                column=1,
                pady=(10, 0),
                sticky="ws"
            )
            row += 2

        # Gui for custom message
        self.lbl_message = tk.Label(
            window,
            text="Custom Message:",
            bg="#F5EFE7",
            fg="#213555"
        )
        self.lbl_message.grid(
            row=8,
            column=0,
            padx=20,
            pady=(10, 0),
            sticky="nw"
        )

        self.ent_message = tk.Entry(
            window,
            width=34,
            bg="#FFFDF6",
            fg="#4F709C"
        )
        self.ent_message.grid(
            row=9,
            column=0,
            columnspan=2,
            padx=0,
            sticky="ne"
        )

        # Display screen
        self.txt_order = tk.Text(
            window,
            width=43,
            height=17,
            state=tk.DISABLED,
            bg="#FFFDF6",
            fg="#4F709C"
        )
        self.txt_order.grid(
            row=1,
            column=2,
            rowspan=2,
            columnspan=2,
            padx=30,
            sticky="nw"
        )

        self.lbl_order = tk.Label(
            window,
            text="Order:",
            bg="#F5EFE7",
            fg="#213555"
        )
        self.lbl_order.grid(
            row=0,
            column=2,
            padx=30,
            sticky="sw"
        )

        # Gui for user details
        labels = ["Name:", "Phone Number:", "Address:"]
        self.entries = []
        row = 4
        for r, text in enumerate(labels):
            self.label = tk.Label(
                window,
                text=text,
                bg="#F5EFE7",
                fg="#213555"
             )
            self.entry = tk.Entry(
                window,
                width=34,
                bg="#FFFDF6"
             )

            self.label.grid(
                row=row,
                column=2,
                padx=25,
                sticky="sw"
             )
            self.entry.grid(
                row=row + 1,
                column=2,
                columnspan=2,
                sticky="n"
             )

            row += 2
            self.entries.append(self.entry)

        # Displaying options for collection type
        self.collect = tk.StringVar(window)
        self.pick_up = tk.Radiobutton(
            window,
            variable=self.collect,
            text="Pick Up",
            value="Pick Up",
            command=lambda: Order(
                self.flavour.get(),
                self.var_selected_toppings,
                self.frost.get(),
                self.shape.get(),
                self.layer.get(),
                self.txt_order,
                self.btn_add,
                self.btn_clear,
                self.btn_submit,
                self.ent_message,
                user_details
                ).collecting(
                    self.collect.get(),
                    self.entries,
                    self.txt_order,
                    self.flavour.get(),
                    self.var_selected_toppings,
                    self.frost.get(),
                    self.shape.get(),
                    self.layer.get(),
                    self.btn_add,
                    self.btn_clear,
                    self.btn_submit,
                    self.ent_message,
                    user_details,
                    self.pick_up,
                    self.delivery),
            bg="#F5EFE7",
            fg="#4F709C"
        )
        self.pick_up.grid(
            row=3,
            column=2
        )
        self.delivery = tk.Radiobutton(
            window,
            variable=self.collect,
            text="Delivery",
            value="Delivery",
            command=lambda: Order(
                self.flavour.get(),
                self.var_selected_toppings,
                self.frost.get(),
                self.shape.get(),
                self.layer.get(),
                self.txt_order,
                self.btn_add,
                self.btn_clear,
                self.btn_submit,
                self.ent_message,
                user_details
                ).collecting(
                    self.collect.get(),
                    self.entries,
                    self.txt_order,
                    self.flavour.get(),
                    self.var_selected_toppings,
                    self.frost.get(),
                    self.shape.get(),
                    self.layer.get(),
                    self.btn_add,
                    self.btn_clear,
                    self.btn_submit,
                    self.ent_message,
                    user_details,
                    self.pick_up,
                    self.delivery),
            bg="#F5EFE7",
            fg="#4F709C"
        )
        self.delivery.grid(
            row=3,
            column=3,
            sticky="w"
        )
        self.collect.set(0)

        # Displaying options for flavours
        self.flavour = tk.StringVar(window)

        for r, text in enumerate(ingredients[0]):
            self.flvr = tk.Radiobutton(
                master=self.frm_flavour,
                text=text,
                variable=self.flavour,
                value=text,
                bg="#F0E9DF",
                fg="#4F709C"
            )
            self.flvr.grid(
                sticky="nw"
            )
        self.flavour.set(0)

        # Displaying options for toppings
        self.var_selected_toppings = []
        for r, text in enumerate(ingredients[1]):
            self.var = tk.StringVar(window)
            self.topping = tk.Checkbutton(
                master=self.frm_topping,
                text=text,
                variable=self.var,
                onvalue=text,
                offvalue="",
                bg="#F0E9DF",
                fg="#4F709C",
            )
            self.topping.grid(
                sticky="nw",
            )
            self.var_selected_toppings.append(self.var)

        # Displaying options for frostings
        self.frost = tk.StringVar(window)

        for r, text in enumerate(ingredients[2]):
            self.frosting = tk.Radiobutton(
                master=self.frm_frosting,
                variable=self.frost,
                text=text,
                value=text,
                bg="#F0E9DF",
                fg="#4F709C"
            )
            self.frosting.grid(
                sticky="nw"
            )
        self.frost.set(0)

        # Displaying options for shapes
        self.shape = tk.StringVar(window)

        for r, text in enumerate(ingredients[3]):
            self.shpe = tk.Radiobutton(
                master=self.frm_shape,
                variable=self.shape,
                text=text,
                value=text,
                bg="#F0E9DF",
                fg="#4F709C"
            )
            self.shpe.grid(
                sticky="nw",
                pady=(3, 0)
            )
        self.shape.set(0)

        # Displaying options for layers
        self.layer = tk.StringVar(window)

        for r, text in enumerate(ingredients[4]):
            self.lyr = tk.Radiobutton(
                master=self.frm_layer,
                variable=self.layer,
                text=text,
                value=text,
                bg="#F0E9DF",
                fg="#4F709C"
            )
            self.lyr.grid(
                sticky="nw",
                pady=(3, 0)
            )
        self.layer.set(0)

        #Submit button
        self.btn_submit = tk.Button(
            window,
            text="Submit",
            command=lambda: Order(
                self.flavour.get(),
                self.var_selected_toppings,
                self.frost.get(),
                self.shape.get(),
                self.layer.get(),
                self.txt_order,
                self.btn_add,
                self.btn_clear,
                self.btn_submit,
                self.ent_message,
                user_details
                ).collecting(
                    self.collect.get(),
                    self.entries,
                    self.txt_order,
                    self.flavour.get(),
                    self.var_selected_toppings,
                    self.frost.get(),
                    self.shape.get(),
                    self.layer.get(),
                    self.btn_add,
                    self.btn_clear,
                    self.btn_submit,
                    self.ent_message,
                    user_details,
                    self.pick_up,
                    self.delivery),
            highlightbackground="#F5EFE7",
            fg="#213555"
        )
        self.btn_submit.grid(
            row=10,
            column=2,
            padx=20,
            sticky="w"
        )
        # Add button
        self.btn_add = tk.Button(
            window,
            text="Add to Order",
            command=lambda: [
                self.collect.set(0),
                Order(
                    self.flavour.get(),
                    self.var_selected_toppings,
                    self.frost.get(),
                    self.shape.get(),
                    self.layer.get(),
                    self.txt_order,
                    self.btn_add,
                    self.btn_clear,
                    self.btn_submit,
                    self.ent_message,
                    user_details
                )
            ],
            highlightbackground="#F5EFE7",
            fg="#213555"
        )
        self.btn_add.grid(
            row=10,
            column=0,
            padx=20,
            sticky="we"
        )

        # Clear button 
        self.btn_clear = tk.Button(
            window,
            text="Clear",
            command=lambda: Order(
                self.flavour.get(),
                self.var_selected_toppings,
                self.frost.get(),
                self.shape.get(),
                self.layer.get(),
                self.txt_order,
                self.btn_add,
                self.btn_clear,
                self.btn_submit,
                self.ent_message,
                user_details
                ).deselect(
                    self.txt_order,
                    self.btn_add),
            highlightbackground="#F5EFE7",
            fg="#213555"
        )
        self.btn_clear.grid(
            row=10,
            column=1,
            sticky="w"
        )
  
        window.mainloop()

if __name__ == "__main__":
    # Creating the window
    window = tk.Tk()
    window.geometry("700x580")
    # Set window 
    window.resizable(False, False)
    window.title("Online Cake Ordering System")
    window.configure(bg = "#F5EFE7")
    Gui(Cake().retrieve_ingredients())
