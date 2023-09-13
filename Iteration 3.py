"""Iteration 3.

Date: 13.9.23

Author: Hayley Far

Description: Self parameter, title/summary and colours
"""

import tkinter as tk


class Cake:
    """Holds the different options."""

    def __init__(self):
        """Ingredients to pick from."""
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
                 ent_message):
        """Check order is valid."""
        # Use self parameter
        self.custom_message = []
        self.selected_toppings = []
        self.flavour = flavour
        self.var_selected_toppings = var_selected_toppings
        self.frost = frost
        self.shape = shape
        self.layer = layer
        self.txt_order = txt_order
        self.btn_add = btn_add
        self.btn_clear = btn_clear
        self.btn_submit = btn_submit
        self.ent_message = ent_message.get()
        self.user_details = {}

        # Adding the user selected toppings into a list
        if len(self.selected_toppings) == 0:
            for item in self.var_selected_toppings:
                if item.get() != "":
                    self.selected_toppings.append(item.get())

        # Adding the user's message to a list
        if self.ent_message != "":
            self.custom_message.append(self.ent_message)

        # Checking if the users order is valid
        if self.flavour == "0":
            self.txt_order.configure(state=tk.NORMAL)
            self.txt_order.delete("1.0", tk.END)
            self.txt_order.insert("1.0", "Please select a flavour")
            self.txt_order.configure(state=tk.DISABLED)
        elif self.frost == "0":
            self.txt_order.configure(state=tk.NORMAL)
            self.txt_order.delete("1.0", tk.END)
            self.txt_order.insert("1.0", "Please select a frosting")
            self.txt_order.configure(state=tk.DISABLED)
        elif self.shape == "0":
            self.txt_order.configure(state=tk.NORMAL)
            self.txt_order.delete("1.0", tk.END)
            self.txt_order.insert("1.0", "Please select a shape")
            self.txt_order.configure(state=tk.DISABLED)
        elif self.layer == "0":
            self.txt_order.configure(state=tk.NORMAL)
            self.txt_order.delete("1.0", tk.END)
            self.txt_order.insert("1.0", "Please select a layer")
            self.txt_order.configure(state=tk.DISABLED)
        else:
            # Calculating the costs of the cake
            self.value = 30
            # Cost for toppings
            for topping in self.selected_toppings:
                self.value += 1
            # Cost for layers
            if self.layer == "2":
                self.value += 2
            elif self.layer == "3":
                self.value += 4
            elif self.layer == "4":
                self.value += 6
            # Cost for custom message
            if len(self.custom_message) != 0:
                self.value += 1.5
            self.print_order()

    def deselect(self):
        """Remove order from order screen."""
        self.txt_order.configure(state=tk.NORMAL)
        self.txt_order.delete("1.0", tk.END)
        self.txt_order.configure(state=tk.DISABLED)

        # Allows user to use button again as they removed order
        self.btn_add["state"] = tk.NORMAL

    def collecting(self, collect, entries, pick_up, delivery):
        """Check if the user has ordered first."""
        self.collect = collect
        self.entries = entries
        self.pick_up = pick_up
        self.delivery = delivery

        button = str(self.btn_add["state"])
        if button == "normal":
            self.txt_order.configure(state=tk.NORMAL)
            self.txt_order.delete("1.0", tk.END)
            self.txt_order.insert("1.0", "Please place an order first")

        # Checking that users collection type
        elif self.collect != "Pick Up" and self.collect != "Delivery":
            self.txt_order.configure(state=tk.NORMAL)
            self.txt_order.delete("1.0", tk.END)
            self.txt_order.insert("1.0", "Please select pick up or delivery")
        elif self.collect == "Pick Up":
            self.entries[2].delete(0, tk.END)
            self.entries[2].configure(state=tk.DISABLED)
            self.btn_clear["state"] = tk.DISABLED
            self.check_details()
        elif collect == "Delivery":
            self.entries[2].configure(state=tk.NORMAL)
            self.btn_clear["state"] = tk.DISABLED
            # Delivery fee
            self.value += 5
            self.check_details()

    def check_details(self):
        """Check user's details."""
        # Adding keys and values into the empty dictionary
        list = ["Name", "Num", "A"]
        i = 0
        for entry in self.entries:
            ent = entry.get()
            self.user_details[list[0+i]] = ent
            i += 1

        # Retrieving the value from each key in the dictionary
        name = self.user_details.get("Name")
        number = self.user_details.get("Num")
        address = self.user_details.get("A")
        # Check name has no integers
        integer = any(chr.isdigit() for chr in name)
        # Allow phone number to have spaces
        phone = number.replace(" ", "")

        # Checking user details are valid
        if name == "" or integer is True:
            self.txt_order.configure(state=tk.NORMAL)
            self.txt_order.delete("1.0", tk.END)
            self.txt_order.insert("1.0", "Please put your name in")
            self.txt_order.configure(state=tk.DISABLED)
        elif phone.isdigit() is not True or len(number) < 9:
            self.txt_order.configure(state=tk.NORMAL)
            self.txt_order.delete("1.0", tk.END)
            self.txt_order.insert("1.0", "Your phone number is not valid")
            self.txt_order.configure(state=tk.DISABLED)
        elif self.collect == "Delivery" and address == "":
            self.txt_order.configure(state=tk.NORMAL)
            self.txt_order.delete("1.0", tk.END)
            self.txt_order.insert("1.0", "Please enter your address")
            self.txt_order.configure(state=tk.DISABLED)
        else:
            # Runs when everything is valid (order and details)
            self.btn_clear["state"] = tk.DISABLED
            self.btn_submit["state"] = tk.DISABLED
            self.pick_up["state"] = tk.DISABLED
            self.delivery["state"] = tk.DISABLED
            self.print_order()

    def print_order(self):
        """Print user's order in txt_order."""

        # Collecting the cost in a list and making it to 2 dp
        charge = []
        price = "{0:.2f}".format(self.value)
        if len(charge) == 0:
            charge.append(price)

        # Printing the cake order
        self.txt_order.configure(state=tk.NORMAL)
        self.txt_order.delete("1.0", tk.END)
        self.txt_order.insert("1.0", "Flavour: ")
        self.txt_order.insert("1.9", "".join(self.flavour))
        self.txt_order.insert("3.0", "\nFrosting: ")
        self.txt_order.insert("3.10", "".join(self.frost))
        if len(self.selected_toppings) != 0:
            self.txt_order.insert("4.0", "\nToppings: ")
            self.txt_order.insert("4.10", ", ".join(self.selected_toppings))
        self.txt_order.insert("5.0", "\nShape: ")
        self.txt_order.insert("5.7", "".join(self.shape))
        self.txt_order.insert("6.0", "\nLayers: ")
        self.txt_order.insert("6.8", ", ".join(self.layer))
        if len(self.custom_message) != 0:
            self.txt_order.insert("7.0", "\nCustom Message: ")
            self.txt_order.insert("7.16", "".join(self.custom_message))
        # Bold cost
        self.txt_order.tag_configure("bold", font="Lucinds 12 bold")
        self.txt_order.insert("8.0", "\n\nCost: $", "bold")
        self.txt_order.insert("8.7", charge, "bold")

        # Printing the user's details
        if len(self.user_details) != 0:
            self.txt_order.configure(state=tk.NORMAL)
            self.txt_order.insert("10.0", "\n\nName: ")
            self.txt_order.insert("10.6", "".join(self.user_details["Name"]))
            self.txt_order.insert("11.0", "\nPhone Number: ")
            self.txt_order.insert("11.14", "".join(self.user_details["Num"]))
            if len(self.user_details["A"]) != 0:
                self.txt_order.insert("12.0", "\nAddress: ")
                self.txt_order.insert("12.9", "".join(self.user_details["A"]))
            self.txt_order.insert("13.0", "\n\nOrder submitted!", "bold")
            self.txt_order.configure(state=tk.DISABLED)
        self.txt_order.insert(tk.END, "\n\n'Clear' button to change order")
        self.txt_order.configure(state=tk.DISABLED)

        self.btn_add["state"] = tk.DISABLED

class Gui:
    """Layout of the GUI."""

    def __init__(self, ingredients):
        """Create elements for window."""
        # Creating a canvas
        canvas = tk.Canvas(
            window,
            width="650",
            height="600",
            bg = "#F5EFE7"
        )
        canvas.grid(
            sticky="news",
            padx=10,
            pady=10
        )

        # Creating the frames for other widgets
        frm_summary = tk.Frame(
            master=canvas,
            width=300,
            height=80,
            bg="#003258"
        )
        frm_summary.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="we"
        )
        frm_summary.grid_propagate(False)
       
        frm_flavour = tk.Frame(
            master=canvas,
            width=150,
            height=200,
            bg="#F0E9DF"
        )
        frm_flavour.grid(
            row=2,
            column=0,
            padx=20
        )
        frm_flavour.grid_propagate(False)  # Maintains frame attributes

        frm_topping = tk.Frame(
            master=canvas,
            width=150,
            height=200,
            bg="#F0E9DF"
        )
        frm_topping.grid(
            row=4,
            column=0,
            rowspan=5,
            sticky="n"
        )
        frm_topping.grid_propagate(False)

        # Summary label
        summary = "Customise your own cake, then click 'Add to Order'"
        text = "Enter collection type and your details to finalise your order"

        lbl_title = tk.Label(
            master=frm_summary,
            text="ONLINE CAKE ORDER SYSTEM",
            fg="#ffffff",
            bg="#003258",
            font=('Helvatical bold',20)
        )
        lbl_title.grid(
            padx=10,
            sticky="w"
        )
        lbl_summary = tk.Label(
            master=frm_summary,
            text=summary,
            fg="#ffffff",
            bg="#003258"
        )
        lbl_summary.grid(
            padx=10,
            sticky="w"
        )
       
        lbl_text = tk.Label(
            master=frm_summary,
            text=text,
            fg="#ffffff",
            bg="#003258"
        )
        lbl_text.grid(
            padx=10,
            sticky="w"
        )

        # Creating labels in first column
        lbls = ["Flavour:", "Toppings:"]
        row = 1
        for r, text in enumerate(lbls):
            label = tk.Label(
                master=canvas,
                text=text,
                bg="#F5EFE7",
                fg="#9F6A91"
            )
            label.grid(
                row=row,
                column=0,
                padx=20,
                pady=(10, 0),
                sticky="nw"
            )
            row += 2

        # Creating the frames for other widgets
        frm_frosting = tk.Frame(
            master=canvas,
            width=150,
            height=200,
            bg="#F0E9DF"
        )
        frm_frosting.grid(
            row=2,
            column=1
        )
        frm_frosting.grid_propagate(False)

        frm_shape = tk.Frame(
            master=canvas,
            width=150,
            height=85,
            bg="#F0E9DF"
        )
        frm_shape.grid(
            row=4,
            column=1,
            sticky="n"
        )
        frm_shape.grid_propagate(False)

        frm_layer = tk.Frame(
            master=canvas,
            width=150,
            height=85,
            bg="#F0E9DF"
        )
        frm_layer.grid(
            row=6,
            column=1,
            rowspan=3,
            sticky="n"
        )
        frm_layer.grid_propagate(False)

        # Creating labels in 2nd column
        text = ["Frosting:", "Shape:", "Layers:"]
        row = 1
        for r, text in enumerate(text):
            label = tk.Label(
                master=canvas,
                text=text,
                bg="#F5EFE7",
                fg="#9F6A91"
            )
            label.grid(
                row=row,
                column=1,
                pady=(10, 0),
                sticky="ws"
            )
            row += 2

        # Gui for custom message
        lbl_message = tk.Label(
            master=canvas,
            text="Custom Message:",
            bg="#F5EFE7",
            fg="#9F6A91"
        )
        lbl_message.grid(
            row=9,
            column=0,
            padx=20,
            pady=(10, 0),
            sticky="nw"
        )

        ent_message = tk.Entry(
            master=canvas,
            width=34,
            bg="#FFFFFF",
            fg="#4F709C"
        )
        ent_message.grid(
            row=10,
            column=0,
            columnspan=2,
            padx=0,
            sticky="ne"
        )

        # Display screen
        txt_order = tk.Text(
            master=canvas,
            width=43,
            height=17,
            state=tk.DISABLED,
            bg="#FFFFFF",
            fg="#4F709C"
        )
        txt_order.grid(
            row=2,
            column=2,
            rowspan=2,
            columnspan=2,
            padx=30,
            sticky="nw"
        )

        lbl_order = tk.Label(
            master=canvas,
            text="Order:",
            bg="#F5EFE7",
            fg="#9F6A91"
        )
        lbl_order.grid(
            row=1,
            column=2,
            padx=30,
            sticky="sw"
        )

        # Gui for user details
        labels = ["Name:", "Phone Number:", "Address:"]
        entries = []
        row = 5
        for r, text in enumerate(labels):
            label = tk.Label(
                master=canvas,
                text=text,
                bg="#F5EFE7",
                fg="#9F6A91"
             )
            entry = tk.Entry(
                master=canvas,
                width=34,
                bg="#FFFFFF",
                fg="#4F709C"
             )

            label.grid(
                row=row,
                column=2,
                padx=25,
                sticky="sw"
             )
            entry.grid(
                row=row + 1,
                column=2,
                columnspan=2,
                sticky="n"
             )

            row += 2
            entries.append(entry)

        # Displaying options for collection type
        collect = tk.StringVar(window)
        pick_up = tk.Radiobutton(
            master=canvas,
            variable=collect,
            text="Pick Up",
            value="Pick Up",
            command=lambda: Order(
                flavour.get(),
                var_selected_toppings,
                frost.get(),
                shape.get(),
                layer.get(),
                txt_order,
                btn_add,
                btn_clear,
                btn_submit,
                ent_message
                ).collecting(
                    collect.get(),
                    entries,
                    pick_up,
                    delivery),
            bg="#F5EFE7",
            fg="#4F709C"
        )
        pick_up.grid(
            row=4,
            column=2
        )
        delivery = tk.Radiobutton(
            master=canvas,
            variable=collect,
            text="Delivery",
            value="Delivery",
            command=lambda: Order(
                flavour.get(),
                var_selected_toppings,
                frost.get(),
                shape.get(),
                layer.get(),
                txt_order,
                btn_add,
                btn_clear,
                btn_submit,
                ent_message
                ).collecting(
                    collect.get(),
                    entries,
                    pick_up,
                    delivery),
            bg="#F5EFE7",
            fg="#4F709C"
        )
        delivery.grid(
            row=4,
            column=3,
            sticky="w"
        )
        collect.set(0)

        # Displaying options for flavours
        flavour = tk.StringVar(window)

        for r, text in enumerate(ingredients[0]):
            flvr = tk.Radiobutton(
                master=frm_flavour,
                text=text,
                variable=flavour,
                value=text,
                bg="#F0E9DF",
                fg="#4F709C"
            )
            flvr.grid(
                sticky="nw"
            )
        flavour.set(0)

        # Displaying options for toppings
        var_selected_toppings = []
        for r, text in enumerate(ingredients[1]):
            var = tk.StringVar(window)
            topping = tk.Checkbutton(
                master=frm_topping,
                text=text,
                variable=var,
                onvalue=text,
                offvalue="",
                bg="#F0E9DF",
                fg="#4F709C",
            )
            topping.grid(
                sticky="nw",
            )
            var_selected_toppings.append(var)

        # Displaying options for frostings
        frost = tk.StringVar(window)

        for r, text in enumerate(ingredients[2]):
            frosting = tk.Radiobutton(
                master=frm_frosting,
                variable=frost,
                text=text,
                value=text,
                bg="#F0E9DF",
                fg="#4F709C"
            )
            frosting.grid(
                sticky="nw"
            )
        frost.set(0)

        # Displaying options for shapes
        shape = tk.StringVar(window)

        for r, text in enumerate(ingredients[3]):
            shpe = tk.Radiobutton(
                master=frm_shape,
                variable=shape,
                text=text,
                value=text,
                bg="#F0E9DF",
                fg="#4F709C"
            )
            shpe.grid(
                sticky="nw",
                pady=(3, 0)
            )
        shape.set(0)

        # Displaying options for layers
        layer = tk.StringVar(window)

        for r, text in enumerate(ingredients[4]):
            lyr = tk.Radiobutton(
                master=frm_layer,
                variable=layer,
                text=text,
                value=text,
                bg="#F0E9DF",
                fg="#4F709C"
            )
            lyr.grid(
                sticky="nw",
                pady=(3, 0)
            )
        layer.set(0)

        #Submit button
        btn_submit = tk.Button(
            master=canvas,
            text="Submit",
            command=lambda: Order(
                flavour.get(),
                var_selected_toppings,
                frost.get(),
                shape.get(),
                layer.get(),
                txt_order,
                btn_add,
                btn_clear,
                btn_submit,
                ent_message
                ).collecting(
                    collect.get(),
                    entries,
                    pick_up,
                    delivery),
            highlightbackground="#F5EFE7",
            fg="#213555"
        )
        btn_submit.grid(
            row=11,
            column=2,
            padx=20,
            sticky="w"
        )
        # Add button
        btn_add = tk.Button(
            master=canvas,
            text="Add to Order",
            command=lambda: [
                collect.set(0),
                Order(
                    flavour.get(),
                    var_selected_toppings,
                    frost.get(),
                    shape.get(),
                    layer.get(),
                    txt_order,
                    btn_add,
                    btn_clear,
                    btn_submit,
                    ent_message
                )
            ],
            highlightbackground="#F5EFE7",
            fg="#213555"
        )
        btn_add.grid(
            row=11,
            column=0,
            padx=20,
            sticky="we"
        )

        # Clear button
        btn_clear = tk.Button(
            master=canvas,
            text="Clear",
            command=lambda: Order(
                flavour.get(),
                var_selected_toppings,
                frost.get(),
                shape.get(),
                layer.get(),
                txt_order,
                btn_add,
                btn_clear,
                btn_submit,
                ent_message,
                ).deselect(),
            highlightbackground="#F5EFE7",
            fg="#213555"
        )
        btn_clear.grid(
            row=11,
            column=1,
            sticky="w",
            pady=8
        )
 
        window.mainloop()

if __name__ == "__main__":
    # Creating the window
    window = tk.Tk()
    window.geometry("732x674")
    # Set window
    window.resizable(False, False)
    window.title("Online Cake Ordering System")
    window.configure(bg="#003258")
    Gui(Cake().retrieve_ingredients())
