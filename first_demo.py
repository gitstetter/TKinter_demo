### https://realpython.com/python-gui-tkinter/

import tkinter as tk

#Create Window
window = tk.Tk()

#Create Frames
frame_a=tk.Frame(bg="red")
frame_b=tk.Frame()

#Create Label Widget, assign to frame_and pack
greeting = tk.Label(
    master=frame_a,
    text="Hello there!",
    foreground="white",
    background="green",
    width=30, #measured in text units "0"
    height=5) #measured in text units "0"

#Pack Label widget to add window
greeting.pack()

#Create a clickable Button, assign to frame_and pack
button = tk.Button(
    master=frame_b,
    text="Click me!",
    width=25,
    height=5
)
button.pack()

#Create a text entry widget, assign to frame_b and pack
entry=tk.Entry(
    master=frame_b,
    width=50)
entry.pack()

#Pack frames
frame_a.pack(fill=tk.X) #responsive to window resizing on x axis
frame_b.pack()

# Call mainloop
window.mainloop()