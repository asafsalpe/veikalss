import tkinter as tk
from PIL import Image, ImageTk
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product_to_cart(self, product):
        self.products.append(product)
        return f"Pievieno produktu: {product.name}"

    def remove_product_from_cart(self, product):
        self.products.remove(product)
        return f"Noņem produktu: {product.name}"

    def get_total_price(self):
        total = sum(product.get_total_price() for product in self.products)
        return f"Kopējā summa ir: {total:.2f} EUR"

    def clear_cart(self):
        self.products.clear()

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Iepirkumu grozs")
        self.master.geometry("315x550")
        self.master.configure(bg="#fadadd")
        self.cart = ShoppingCart()

        self.name_label = tk.Label(master, text="Produkta nosaukums: ", bg="#fdfd66")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.price_label = tk.Label(master, text="Cena: ", bg="#fdfd66")
        self.price_label.grid(row=1, column=0, padx=5, pady=5)

        self.price_entry = tk.Entry(master)
        self.price_entry.grid(row=1, column=1)

        self.quantity_label = tk.Label(master, text="Daudzums: ", bg="#fdfd66")
        self.quantity_label.grid(row=2, column=0, padx=5, pady=5)

        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="Pievienot grozam", command=self.add_to_cart)
        self.add_button.grid(row=3, columnspan=2, pady=10)
        self.add_button.configure(bg="#5bb450", fg="white")

        self.cart_listbox = tk.Listbox(master, width=50, bg="#fadadd")
        self.cart_listbox.grid(row=4, columnspan=2, padx=5, pady=5)

        self.total_label = tk.Label(master, text="Kopējā summa: 0.00 EUR", bg="#dafaf7")
        self.total_label.grid(row=5, columnspan=2)

        self.add_button1 = tk.Button(master, text="Iztīrīt grozu", command=self.clear_cart1)
        self.add_button1.grid(row = 6, columnspan=2)
        self.add_button1.configure(bg="#ff2c2c", fg="white")

        self.image = Image.open("mrlb.png")
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(master, image=self.image_tk, bg="#fadadd")
        self.image_label.grid(row=7, columnspan=2, pady=10)

    def add_to_cart(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        quantity = float(self.quantity_entry.get())

        product = Product(name, price, quantity)
        self.cart.add_product_to_cart(product)

        self.cart_listbox.insert(tk.END, f"{name}: {price:.2f} EUR, {quantity} gab")
        self.update_total_price()

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def update_total_price(self):
        total = self.cart.get_total_price()
        self.total_label.config(text=total)
    
    def clear_cart1(self):
        self.cart.clear_cart()
        self.cart_listbox.delete(0, tk.END)
        self.update_total_price()

if __name__ == "__main__":
    master = tk.Tk()
    app = App(master)
    master.mainloop()