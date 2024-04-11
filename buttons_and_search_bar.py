import tkinter as tk
import database as db

def search():
    value = search_bar_entry.get()
    print(value)
    querry = "select * from medicine_info where medicine_name = " + '"' + value + '"'
    db.search_db(querry)

def search_button(window,w,col,rw,x,y):
    # Create a button
    button = tk.Button(window, text="Search", command=search, width=w)
    button.grid(column=col,row=rw,padx=x,pady=y)
    


def search_bar(window,w,col,rw,x,y):
    #create a seach bar
    global search_bar_entry
    search_bar_entry= tk.Entry(window,width=w)
    search_bar_entry.grid(column=col,row=rw,padx=x,pady=y)

