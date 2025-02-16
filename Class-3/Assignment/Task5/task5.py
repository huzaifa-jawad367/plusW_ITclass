import tkinter as tk
from tkinter import messagebox

# Global balance variable
balance = 1000

def update_balance_label():
    """Update the label displaying the current balance."""
    balance_label.config(text=f"Current Balance: {balance}")

def deposit():
    """Deposit money into the account."""
    global balance
    try:
        amount = float(deposit_entry.get())
        balance += amount
        messagebox.showinfo("Deposit", f"Deposited: {amount}. New balance: {balance}")
        update_balance_label()
        deposit_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for deposit.")

def withdraw():
    """Withdraw money from the account if sufficient funds exist."""
    global balance
    try:
        amount = float(withdraw_entry.get())
        if amount <= balance:
            balance -= amount
            messagebox.showinfo("Withdraw", f"Withdrew: {amount}. New balance: {balance}")
        else:
            messagebox.showerror("Insufficient Funds", "Insufficient funds for this withdrawal.")
        update_balance_label()
        withdraw_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for withdrawal.")

def check_balance():
    """Show the current balance."""
    messagebox.showinfo("Balance", f"Current balance: {balance}")

# Create the main window
root = tk.Tk()
root.title("ATM System Simulation")

# Deposit widgets
deposit_label = tk.Label(root, text="Deposit Amount:")
deposit_label.grid(row=0, column=0, padx=10, pady=10)

deposit_entry = tk.Entry(root)
deposit_entry.grid(row=0, column=1, padx=10, pady=10)

deposit_button = tk.Button(root, text="Deposit", command=deposit)
deposit_button.grid(row=0, column=2, padx=10, pady=10)

# Withdraw widgets
withdraw_label = tk.Label(root, text="Withdraw Amount:")
withdraw_label.grid(row=1, column=0, padx=10, pady=10)

withdraw_entry = tk.Entry(root)
withdraw_entry.grid(row=1, column=1, padx=10, pady=10)

withdraw_button = tk.Button(root, text="Withdraw", command=withdraw)
withdraw_button.grid(row=1, column=2, padx=10, pady=10)

# Check balance and display current balance
balance_label = tk.Label(root, text=f"Current Balance: {balance}")
balance_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

check_balance_button = tk.Button(root, text="Check Balance", command=check_balance)
check_balance_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
