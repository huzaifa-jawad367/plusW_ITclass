import tkinter as tk
from tkinter import messagebox

# Initialize an empty dictionary
inventory = {}

# Function to add items
def add_item():
    item = item_entry.get()
    try:
        quantity = int(quantity_entry.get())
        if item:
            if item in inventory:
                inventory[item] += quantity
            else:
                inventory[item] = quantity
            update_inventory_display()
        else:
            messagebox.showwarning("Warning", "Item name cannot be empty!")
    except ValueError:
        messagebox.showerror("Error", "Quantity must be a valid number!")

# Function to remove items
def remove_item():
    item = item_entry.get()
    try:
        quantity = int(quantity_entry.get())
        if item in inventory:
            if inventory[item] >= quantity:
                inventory[item] -= quantity
                if inventory[item] == 0:
                    del inventory[item]
                update_inventory_display()
            else:
                messagebox.showwarning("Warning", f"Insufficient quantity of {item}.")
        else:
            messagebox.showwarning("Warning", f"{item} does not exist in inventory.")
    except ValueError:
        messagebox.showerror("Error", "Quantity must be a valid number!")

# Function to update inventory display
def update_inventory_display():
    inventory_text.delete(1.0, tk.END)
    for item, quantity in inventory.items():
        inventory_text.insert(tk.END, f"{item}: {quantity}\n")

# Create the main Tkinter window
root = tk.Tk()
root.title("Inventory System")
root.geometry("300x400")

# Create UI components
item_label = tk.Label(root, text="Item:")
item_label.pack()
item_entry = tk.Entry(root)
item_entry.pack()

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack()

remove_button = tk.Button(root, text="Remove Item", command=remove_item)
remove_button.pack()

inventory_label = tk.Label(root, text="Inventory:")
inventory_label.pack()

inventory_text = tk.Text(root, height=10, width=30)
inventory_text.pack()

# Run the Tkinter event loop
root.mainloop()
