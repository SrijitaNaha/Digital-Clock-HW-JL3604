import tkinter as tk
import time
import random

def random_color():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return color

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.config(fg=random_color())
    root.config(bg=random_color())
    root.after(1000, update_time)

root = tk.Tk()
root.title("My Digital Clock")

title_label = tk.Label(root, text="My Digital Clock", font=("Arial", 20))
title_label.pack()

clock_label = tk.Label(root, font=("Arial", 40), fg=random_color())
clock_label.pack()

update_time()

root.mainloop()