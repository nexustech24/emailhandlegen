import tkinter as tk
from tkinter import messagebox

def generate_email():
    first_name = first_name_entry.get().strip().lower()
    day = day_entry.get().strip()
    month = month_entry.get().strip()
    last_name = last_name_entry.get().strip().lower()

    if not first_name or not day or not month or not last_name:
        messagebox.showerror("Error", "All fields are required!")
        return

    if len(first_name) < 3 or len(last_name) < 3:
        messagebox.showerror("Error", "First and last names must have at least 3 characters!")
        return

    try:
        day = int(day)
        month = int(month)
        if day < 1 or day > 31 or month < 1 or month > 12:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Day must be between 1-31 and month must be between 1-12.")
        return

    formatted_day = f"{day:02}"
    email_handle = f"{first_name[:3]}{formatted_day}{month}{last_name[:3]}"

    email_label.config(text=f"Generated Email Handle: {email_handle}")
    email_output.delete(0, tk.END)
    email_output.insert(0, email_handle)
    email_output.config(state="readonly")

def on_day_entry_change(entry_var):
    value = entry_var.get().strip()
    if value.isdigit() and 1 <= int(value) <= 9:
        entry_var.set(f"0{value}")

# Create the main window
root = tk.Tk()
root.title("Email Handle Generator")
root.resizable(False, False)  # Prevent window maximization

# Input fields and labels
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="First Name:").grid(row=0, column=0, sticky="e")
first_name_entry = tk.Entry(frame)
first_name_entry.grid(row=0, column=1)

tk.Label(frame, text="Day:").grid(row=1, column=0, sticky="e")
day_var = tk.StringVar()
day_var.trace_add("write", lambda *args: on_day_entry_change(day_var))
day_entry = tk.Entry(frame, textvariable=day_var)
day_entry.grid(row=1, column=1)

tk.Label(frame, text="Month:").grid(row=2, column=0, sticky="e")
month_var = tk.StringVar()
month_entry = tk.Entry(frame, textvariable=month_var)
month_entry.grid(row=2, column=1)

tk.Label(frame, text="Last Name:").grid(row=3, column=0, sticky="e")
last_name_entry = tk.Entry(frame)
last_name_entry.grid(row=3, column=1)

# Generate button
generate_button = tk.Button(frame, text="Generate", command=generate_email)
generate_button.grid(row=4, columnspan=2, pady=10)

# Label to display the email handle
email_label = tk.Label(root, text="", font=("Helvetica", 12), pady=10)
email_label.pack()

# Entry to display and copy the email handle
email_output = tk.Entry(root, font=("Helvetica", 12), state="normal")
email_output.pack(pady=10)

# Run the application
root.mainloop()
