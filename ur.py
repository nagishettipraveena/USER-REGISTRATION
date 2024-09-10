import tkinter as tk
from tkinter import messagebox

def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        with open("user_data.txt", "a") as file:
            file.write(f"{username},{password}\n")
        messagebox.showinfo("Success", "Registration Successful!")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Create a new window
window = tk.Tk()
window.title("User Registration Form")

# Username Label and Entry
label_username = tk.Label(window, text="Username")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

# Password Label and Entry
label_password = tk.Label(window, text="Password")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Register Button
btn_register = tk.Button(window, text="Register", command=register_user)
btn_register.pack()

# Run the main loop
window.mainloop()
