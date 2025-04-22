import tkinter as tk  # Import the tkinter library for GUI components
from tkinter import messagebox, PhotoImage  # Import specific modules from tkinter
import sqlite3  # Import the sqlite3 library for database operations
import subprocess  # Import subprocess to run external scripts

def register_user():
    """
    Registers a new user by inserting their username and password into the database.
    If the username already exists, an error message is displayed.
    """
    username = entry_username.get()  # Get the username from the entry field
    password = entry_password.get()  # Get the password from the entry field

    if username and password:  # Check if both username and password are provided
        conn = sqlite3.connect("cyber_quest.db")  # Connect to the SQLite database
        cursor = conn.cursor()  # Create a cursor object to execute SQL commands

        try:
            # Insert the new user's details into the users table
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password),
            )
            conn.commit()  # Commit the changes to the database
            messagebox.showinfo("Success", "User registered successfully!")  # Show success message
        except sqlite3.IntegrityError:
            # Show error message if the username already exists
            messagebox.showerror("Error", "Username already exists!")

        conn.close()  # Close the database connection
    else:
        # Show error message if username or password is missing
        messagebox.showerror("Error", "Please enter both username and password.")

def login_user():
    """
    Logs in an existing user by checking their username and password against the database.
    If the credentials are correct, a welcome message is displayed and a new script is launched.
    """
    username = entry_username.get()  # Get the username from the entry field
    password = entry_password.get()  # Get the password from the entry field

    conn = sqlite3.connect("cyber_quest.db")  # Connect to the SQLite database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands

    # Query the database for the user with the given username and password
    cursor.execute(
        "SELECT * FROM users WHERE username =? AND password =?", (username, password)
    )
    user = cursor.fetchone()  # Fetch one matching record

    if user:  # Check if a matching user was found
        message = f"Welcome, {user[1]}! Login successful."
        messagebox.showinfo("Success", message)  # Show success message

        # Write the logged-in username to a temporary file
        with open("logged_in_user.txt", "w") as file:
            file.write(username)

        root.destroy()  # Close the current window
        subprocess.Popen(["python3", "cyber_quest/game.py"])  # Launch the external script
    else:
        # Show error message if the credentials are invalid
        messagebox.showerror("Error", "Invalid username or password.")

    conn.close()  # Close the database connection

# Create the main application window
root = tk.Tk()
root.title("Cyber Quest")  # Set the window title
root.geometry("500x400")  # Set the window size
root.eval("tk::PlaceWindow . center")  # Center the window on the screen
root.config(bg="#2B2D42")  # Set the background color

# Load and display the application logo
root.cyber_quest_image = PhotoImage(file=r"cyber_quest/Icons/Cyber Quest.png")
root.label = tk.Label(root, image=root.cyber_quest_image, bg="#2B2D42")
root.label.pack(pady=0)

# Create a frame to hold the input fields and buttons
frame = tk.Frame(root)
frame.pack(pady=20)

# Add a label with instructions
root.label = tk.Label(
    root,
    text="Fill out the information below and either register or log in",
    font=("Tahoma", 15),
    bg="#2B2D42",
)
root.label.place(x=50, y=95)

# Add the username label and entry field
root.label_username = tk.Label(
    root, text="Username:", font=("Tahoma", 25), bg="#2B2D42"
)
root.label_username.pack(padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.pack(padx=10, pady=5)

# Add the password label and entry field
root.label_password = tk.Label(
    root, text="Password:", font=("Tahoma", 25), bg="#2B2D42"
)
root.label_password.pack(padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(padx=10, pady=5)

# Load and add the register button
root.button_register_image = PhotoImage(file=r"cyber_quest/Icons/button_register.png")
root.button_register = tk.Button(
    root, image=root.button_register_image, bg="#2B2D42", command=register_user
)
root.button_register.place(x=30, y=320)

# Load and add the login button
root.button_login_image = PhotoImage(file=r"cyber_quest/Icons/button_login.png")
root.button_login = tk.Button(
    root, image=root.button_login_image, bg="#2B2D42", command=login_user
)
root.button_login.place(x=381, y=320)

# Start the Tkinter event loop
root.mainloop()
