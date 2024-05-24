from map import generer_map
import tkinter as tk
import os
import sys
import webbrowser
import folium

def open_map():
    # Open the "map.html" file in the default web browser
    webbrowser.open("map.html")

root = tk.Tk()

button = tk.Button(root, text="Generate and Open Map", command=lambda: [open_map()])
button.pack()

root.mainloop()

