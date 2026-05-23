# Virtual Vending Machine 
import tkinter as tk
import customtkinter as ctk
import time as t
from utilityapp02vmp import vm_products

# Master frame class, for creating general layout
class vending_master_class(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

# Displays products, prices, and their ids
class vending_display_class(ctk.CTkFrame):
    def __init__(self, master_frame, **kwargs):
        super().__init__(master_frame, **kwargs)

        # Define product variables
        product_name_1 = "Cookie"
        product_id_price_1 = "100 - 2.00"
        
        product_name_2 = "Spicy Potato Chips"
        product_id_price_2 = "101 - 4.00"

        product_name_3 = "Cheesy Potato Chips"
        product_id_price_3 = "102 - 4.00"

        product_name_4 = "Cheese Nachos"
        product_id_price_4 = "103 - 4.00"

        product_name_5 = "Spicy Nachos"
        product_id_price_5 = "104 - 4.00"

        product_name_6 = "Chocolate Milk"
        product_id_price_6 = "105 - 2.00"

        product_name_7 = "Strawberry Milk"
        product_id_price_7 = "106 - 2.00"
        
        product_name_8 = "M & M's"
        product_id_price_8 = "107 - 4.00"

        product_name_9 = "Orange Juice"
        product_id_price_9 = "108 - 3.00"

        product_name_10 = "Chocolate Bar"
        product_id_price_10 = "109 - 4.00"

        product_name_11 = "Dark Chocolate Bar"
        product_id_price_11 = "110 - 4.00"

        product_name_12 = "Canned Ice Tea"
        product_id_price_12 = "111 - 2.00"

        product_name_13 = "Bottled Water"
        product_id_price_13 = "112 - 4.00"

        product_name_14 = "Packaged BLT Sandwich"
        product_id_price_14 = "113 - 4.00"

        product_name_15 = "Fruit Cake Slice"
        product_id_price_15 = "114 - 2.00"

        # Product display labels 
        self.display_name_1 = ctk.CTkLabel(self, text = product_name_1)
        self.display_idprice_1 = ctk.CTkLabel(self, text = product_id_price_1)

        self.display_name_2 = ctk.CTkLabel(self, text = product_name_2)
        self.display_idprice_2 = ctk.CTkLabel(self, text = product_id_price_2)

        self.display_name_3 = ctk.CTkLabel(self, text = product_name_3)
        self.display_idprice_3 = ctk.CTkLabel(self, text = product_id_price_3)

        self.display_name_4 = ctk.CTkLabel(self, text = product_name_4)
        self.display_idprice_4 = ctk.CTkLabel(self, text = product_id_price_4)

        self.display_name_5 = ctk.CTkLabel(self, text = product_name_5)
        self.display_idprice_5 = ctk.CTkLabel(self, text = product_id_price_5)

        self.display_name_6 = ctk.CTkLabel(self, text = product_name_6)
        self.display_idprice_6 = ctk.CTkLabel(self, text = product_id_price_6)

        self.display_name_7 = ctk.CTkLabel(self, text = product_name_7)
        self.display_idprice_7 = ctk.CTkLabel(self, text = product_id_price_7)

        self.display_name_8 = ctk.CTkLabel(self, text = product_name_8)
        self.display_idprice_8 = ctk.CTkLabel(self, text = product_id_price_8)

        self.display_name_9 = ctk.CTkLabel(self, text = product_name_9)
        self.display_idprice_9 = ctk.CTkLabel(self, text = product_id_price_9)

        self.display_name_10 = ctk.CTkLabel(self, text = product_name_10)
        self.display_idprice_10 = ctk.CTkLabel(self, text = product_id_price_10)

        self.display_name_11 = ctk.CTkLabel(self, text = product_name_11)
        self.display_idprice_11 = ctk.CTkLabel(self, text = product_id_price_11)

        self.display_name_12 = ctk.CTkLabel(self, text = product_name_12)
        self.display_idprice_12 = ctk.CTkLabel(self, text = product_id_price_12)

        self.display_name_13 = ctk.CTkLabel(self, text = product_name_13)
        self.display_idprice_13 = ctk.CTkLabel(self, text = product_id_price_13)

        self.display_name_14 = ctk.CTkLabel(self, text = product_name_14)
        self.display_idprice_14 = ctk.CTkLabel(self, text = product_id_price_14)

        self.display_name_15 = ctk.CTkLabel(self, text = product_name_15)
        self.display_idprice_15 = ctk.CTkLabel(self, text = product_id_price_15)

        # Gridding
        self.display_name_1.grid(row = 0, column = 0, padx = 5, pady = 2)
        self.display_idprice_1.grid(row = 1, column = 0, padx = 5, pady = 2)

        self.display_name_2.grid(row = 0, column = 1, padx = 5, pady = 2)
        self.display_idprice_2.grid(row = 1, column = 1, padx = 5, pady = 2)

        self.display_name_3.grid(row = 0, column = 2, padx = 5, pady = 2)
        self.display_idprice_3.grid(row = 1, column = 2, padx = 5, pady = 2)

        self.display_name_4.grid(row = 2, column = 0, padx = 5, pady = 2)
        self.display_idprice_4.grid(row = 3, column = 0, padx = 5, pady = 2)

        self.display_name_5.grid(row = 2, column = 1, padx = 5, pady = 2)
        self.display_idprice_5.grid(row = 3, column = 1, padx = 5, pady = 2)

        self.display_name_6.grid(row = 2, column = 2, padx = 5, pady = 2)
        self.display_idprice_6.grid(row = 3, column = 2, padx = 5, pady = 2)

        self.display_name_7.grid(row = 4, column = 0, padx = 5, pady = 2)
        self.display_idprice_7.grid(row = 5, column = 0, padx = 5, pady = 2)

        self.display_name_8.grid(row = 4, column = 1, padx = 5, pady = 2)
        self.display_idprice_8.grid(row = 5, column = 1, padx = 5, pady = 2)

        self.display_name_9.grid(row = 4, column = 2, padx = 5, pady = 2)
        self.display_idprice_9.grid(row = 5, column = 2, padx = 5, pady = 2)

        self.display_name_10.grid(row = 6, column = 0, padx = 5, pady = 2)
        self.display_idprice_10.grid(row = 7, column = 0, padx = 5, pady = 2)

        self.display_name_11.grid(row = 6, column = 1, padx = 5, pady = 2)
        self.display_idprice_11.grid(row = 7, column = 1, padx = 5, pady = 2)

        self.display_name_12.grid(row = 6, column = 2, padx = 5, pady = 2)
        self.display_idprice_12.grid(row = 7, column = 2, padx = 5, pady = 2)

        self.display_name_13.grid(row = 8, column = 0, padx = 5, pady = 2)
        self.display_idprice_13.grid(row = 9, column = 0, padx = 5, pady = 2)

        self.display_name_14.grid(row = 8, column = 1, padx = 5, pady = 2)
        self.display_idprice_14.grid(row = 9, column = 1, padx = 5, pady = 2)

        self.display_name_15.grid(row = 8, column = 2, padx = 5, pady = 2)
        self.display_idprice_15.grid(row = 9, column = 2, padx = 5, pady = 2)

# Selection class mechanism for choosing and buying items
class vending_selector_class(ctk.CTkFrame):
    def __init__(self, master_frame, dispenser_state = None,  **kwargs):
        super().__init__(master_frame, **kwargs)

        # Used to define the default value of dispenser_state in order to connect purchase_func and self.dispenser
        if dispenser_state is not None:
            self.dispenser_state = dispenser_state
        else:
            self.dispenser_state = tk.StringVar(value = "No item purchased yet.")

        # This function gets the ID from the user input and returns it as a key.
        def get_product_id_func(product_id):
            id = str(product_id)
            return vm_products.get(id)

        # This Function gets the number from user's input and saves the selection.
        def select_product_id_func():
            prod_id = id_var.get()
            selection = get_product_id_func(prod_id)
            id_var.set("")

            # If a valid product id selection is detected e.g. 100, it returns the id's respective values: name: Cookie, and price: 2.00
            if selection:
                self.current_selection = selection
                receipt = f"{selection['name']} — ${selection['price']:.2f}"
                self.result_label.configure(text = receipt)
                return selection
            
            # If the product id is invalid e.g. no id for the product such as 115, it returns "Product not found"
            else:
                self.current_selection = None
                receipt = "Product not found"
                self.result_label.configure(text = receipt)
        
        # Defines id variable as a tkinter string variable
        id_var = tk.StringVar()
        
        # Entry GUI
        self.entry = ctk.CTkEntry(self, textvariable = id_var)

        # Button GUI
        self.button1 = ctk.CTkButton(self, text = "1", command = lambda:self.entry.insert('end', '1'))
        self.button2 = ctk.CTkButton(self, text = "2", command = lambda:self.entry.insert('end', '2'))
        self.button3 = ctk.CTkButton(self, text = "3", command = lambda:self.entry.insert('end', '3'))
    
        self.button4 = ctk.CTkButton(self, text = "4", command = lambda:self.entry.insert('end', '4'))
        self.button5 = ctk.CTkButton(self, text = "5", command = lambda:self.entry.insert('end', '5'))
        self.button6 = ctk.CTkButton(self, text = "6", command = lambda:self.entry.insert('end', '6'))

        self.button7 = ctk.CTkButton(self, text = "7", command = lambda:self.entry.insert('end', '7'))
        self.button8 = ctk.CTkButton(self, text = "8", command = lambda:self.entry.insert('end', '8'))
        self.button9 = ctk.CTkButton(self, text = "9", command = lambda:self.entry.insert('end', '9'))

        self.button0 = ctk.CTkButton(self, text = "0", command = lambda:self.entry.insert('end', '0'))
        self.button_ok = ctk.CTkButton(self, text = "Ok", command = select_product_id_func)
        self.button_del = ctk.CTkButton(self, text = "X", command = lambda:self.entry.delete(0, 'end'))

        # Button dimensions configuration
        self.button1.configure(height = 25, width = 70)
        self.button2.configure(height = 25, width = 70)
        self.button3.configure(height = 25, width = 70)

        self.button4.configure(height = 25, width = 70)
        self.button5.configure(height = 25, width = 70)
        self.button6.configure(height = 25, width = 70)

        self.button7.configure(height = 25, width = 70)
        self.button8.configure(height = 25, width = 70)
        self.button9.configure(height = 25, width = 70)

        self.button0.configure(height = 25, width = 70)
        self.button_ok.configure(height = 25, width = 70)
        self.button_del.configure(height = 25, width = 70) 

        # Button and entry gridding
        self.entry.grid(row = 4, column = 1, padx = 2, pady = 2)

        self.button1.grid(row = 0, column = 0, padx = 2, pady = 5, sticky = "s")
        self.button2.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = "s")
        self.button3.grid(row = 0, column = 2, padx = 2, pady = 5, sticky = "s")

        self.button4.grid(row = 1, column = 0, padx = 2, pady = 5, sticky = "s")
        self.button5.grid(row = 1, column = 1, padx = 2, pady = 5, sticky = "s")
        self.button6.grid(row = 1, column = 2, padx = 2, pady = 5, sticky = "s")

        self.button7.grid(row = 2, column = 0, padx = 2, pady = 5, sticky = "s")
        self.button8.grid(row = 2, column = 1, padx = 2, pady = 5, sticky = "s")
        self.button9.grid(row = 2, column = 2, padx = 2, pady = 5, sticky = "s")

        self.button0.grid(row = 3, column = 1, padx = 2, pady = 5, sticky = "s")
        self.button_ok.grid(row = 3, column = 0, padx = 2, pady = 5, sticky = "s")
        self.button_del.grid(row = 3, column = 2, padx = 2, pady = 5, sticky = "s") 

        # Wallet default value
        self.balance = 150.00

        # Purchasing Function
        def purchase_product_func ():
            selection = getattr(self, 'current_selection', None)
            
            # Defines price and stock variables, then gets the price's value and 1 value of stock (-1)
            price = selection.get('price', 0)
            stock = selection.get('stock', 1)

            # Returns "Out of Stock" if stock ran out
            if stock == 0:
                self.result_label.configure(text = "Out of stock")
                return
            
            # Returns "Insufficient balance" if user runs out of money/credit
            if self.balance < price:
                self.result_label.configure(text = "Insufficient balance")
                return
            
            # Deducts balance and product stock upon purchase
            self.balance -= price
            selection['stock'] = stock - 1

            # Sets display of labels
            self.wallet.configure(text = f"Credit Balance: {self.balance:.2f}")
            self.dispenser_state.set("Collect your item here.")
            self.result_label.configure(text = "Purchase successful.")

            # Clears selection
            self.current_selection = None
            return
        
        # Wallet label, receipt label, and purchase button
        wallet_label = f"{'Balance: '}{self.balance:.2f}"
        self.result_label = ctk.CTkLabel(self, text = "")
        self.wallet = ctk.CTkLabel(self, text = wallet_label)
        self.vert_pad = ctk.CTkLabel(self, textvariable = "")
        self.buy = ctk.CTkButton(self, text = "Purchase", command = purchase_product_func)

        # Gridding
        self.result_label.grid(row = 8, column = 1, padx = 2, pady = 2)
        self.vert_pad.grid(row = 5, column = 1, padx = 0, pady = 5, sticky = "nsew")
        self.wallet.grid(row = 6, column = 1, padx = 0, pady = 5, sticky = "nsew")
        self.buy.grid(row = 7, column = 1, padx = 0, pady = 5, sticky = "nsew")

        # Updates GUI
        self.update_idletasks()
        t.sleep(2)

# Dispenses purchased items
class vending_dispenser_class(ctk.CTkFrame):
    def __init__(self, master_frame, **kwargs):
        super().__init__(master_frame, **kwargs)

        # Resets the self.dispenser button and self.result_label label so that it appears there is nothing there
        def collect_item():
            self.dispenser_state.set("No item purchased yet.")
            return self.dispenser_state.get()
        
        # The default value of dispenser_state and the button
        self.dispenser_state = tk.StringVar(value = "No item purchased yet.")
        self.dispenser = ctk.CTkButton(self, textvariable = self.dispenser_state, command = collect_item)

        # Gridding
        self.dispenser.grid(row = 0, column = 0, padx = 115, pady = 75, sticky = "nsew")

        # Calls function to set up default state
        collect_item()

# Lays out all the frames in the window
class App(ctk.CTk):
    def __init__(self):    
        super().__init__()
    
        self.title("Vending Machine Simulator")

        # First "layer" of frames, which the second "layer" will be layed on top of
        self.vending_master_frame = vending_master_class(master = self, height = 2700, width = 2700, corner_radius = 0, fg_color = "transparent")
        self.vending_master_frame.grid(row = 0, column = 0, sticky = "nsew")

        # Second "layer" of frames, these frames contain the GUI widgets
        self.vending_display_frame = vending_display_class(self.vending_master_frame)
        self.vending_display_frame.grid(row = 0, column = 0, sticky = "nw")

        self.vending_dispenser_frame = vending_dispenser_class(self.vending_master_frame)
        self.vending_dispenser_frame.grid(row = 1, column = 0, sticky = "sew")

        self.vending_selector_frame = vending_selector_class(self.vending_master_frame, dispenser_state = self.vending_dispenser_frame.dispenser_state)
        self.vending_selector_frame.grid(row = 0, column = 1, sticky = "nse")

app = App()
app.mainloop()