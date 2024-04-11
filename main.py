import tkinter as tk
import menu
import buttons_and_search_bar as bs
import mysql.connector
import database as db

# Create a Tkinter window
global window
window = tk.Tk()

# Retrieve screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the title of the window
window.title("Window with Menu")

# Set the size of the window to match screen size
window.geometry(f"{screen_width}x{screen_height}")

# Create the menu
menu.create_menu(window)

bs.search_bar(window,100,0,0,10,10)

bs.search_button(window,20,1,0,10,10)

# Run the Tkinter event loop
window.mainloop()
