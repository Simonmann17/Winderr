import tkinter as tk
import random

root = tk.Tk()
root.title("Hello")
win_width = 300
win_height = 150
root.geometry(f"{win_width}x{win_height}")

msgs = ["Nice Try", "Too Slow", "Try Again", "Almost", "You Got Me"]

MAX_DODGES = 5

label = tk.Label(root, text="Hello World")
label.pack(pady=20)

button = tk.Button(root, text="OK", command=root.destroy)
button.pack()

max_x = int(root.winfo_screenwidth()) - win_width
max_y = int(root.winfo_screenheight()) - win_height
count = 0

def on_hover(event):
	global count
	if (count < MAX_DODGES):
		new_x = random.randint(0, max_x)
		new_y = random.randint(30, max_y-30)
		label.config(text=msgs[count])
		root.geometry(f"+{new_x}+{new_y}")
		count = count + 1
		print(count)

button.bind("<Enter>", on_hover)

root.mainloop()