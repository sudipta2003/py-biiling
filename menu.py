import tkinter as tk
import main

def on_exit(window):
    window.destroy()



def create_menu(window):
    # Create a menu bar
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    # Create a File menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=on_exit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    menu_bar.add_cascade(label="Insert new")
    #menu_bar.add_command(command=insert_new_window)
