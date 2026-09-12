import tkinter as tk
from tkinter import ttk, messagebox

class ROM:

    def __init__(self, root):
        self.root = root
        self.root.title("Restuarant Manager")

        self.menu_items = {
            "FRIES MEAL" : 2,
            "LUNCH MEAL" : 2,
            "BURGER MEAL" : 3,
            "PIZZA MEAL" : 4,
            "CHEESE BURGER" : 2.5,
            "DRINKS" : 1
        }
        self.exchange_rate = 82

        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="Restuaramt Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columspan=3, padx=10, pady=10)

        self.menu_labels={}
        self.menu_quantities={}

        for i, (item, price) in enumerate(self.menu_items):
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial",12)
            )

        label.grid(row=i, column=0, padx=10, pady=5)
        self.menu_labels[item]=label

        quantity_entry = ttk.Entry(frame, width=5)
        quantity_entry.grid(row=i, column=0, padx=10, pady=5)
        self.menu_quantities[item] = quantity_entry

        self.currency_var= tk.StringVar()
        ttk.label(
            frame,
            text="currency : ",
            font=("Arial",12)
        ).grid(
            row= len(self.menu_items)+1,
            column=0,
            padx=10,
            pady=5
        )

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "KSH")
        )
        currency_dropdown.grid(
            row= len(self.menu_items)+1,
            column=0,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_menu_prices)

        order_btn = ttk.Button(
            frame,
            text="Place order",
            command=self.place_order
        )
        order_btn.grid(
            row= len(self.menu_items)+2,
            column=3,
            padx=10,
            pady=10
        )

    def setup_background(self,root):
        bg_width, bg_heigh = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_heigh)
        canvas.pack()

        original_img = tk.PhotoImage(file= "Python/lesson Z7/Screenshot 2026-09-08 113529.png")
        backgroun_img = original_img.subsample(
            original_img.width() //bg_width,
            original_img.height()//bg_heigh
            )

        canvas.create_image(0,0, anchor=tk.NW, image=backgroun_img)
        canvas.image = backgroun_img

    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "ksh." if currency == "KSH" else "$"
        rate = self,self.exchange_rate if currency == "KSH" else 1

        for item, label in self.menu_labels.items():
            price = self.menu_items[item]*rate
            label.config(text=f"{item} ({symbol}{price})")

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "ksh." if currency == "KSH" else "$"
        rate = self.exchange_rate if currency == "KSH" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost

                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
                    )

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")

# Main block to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ROM(root)
    root.geometry("800x600")  # Set the size of the window
    root.mainloop()           # Start the GUI loop

        
