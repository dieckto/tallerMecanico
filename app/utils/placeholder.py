
import tkinter as tk
from tkinter import font    

def on_focus_in(entry,placeholder):
    placeholder = placeholder
    if entry.get() == placeholder:
        entry.delete(0, tk.END)   # borra el texto
        entry.config(fg="black")  # 
    
            # Si es el campo de contraseña → activar show="*"
    if placeholder == "contraseña":
        entry.config(show="*")

def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="grey")

    if placeholder == "contraseña":
        entry.config(show="")

def insert_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="grey")

    if placeholder == "contraseña":
        entry.config(show="")