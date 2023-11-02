import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    "Open a file for editing"
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt.edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text= input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
window.title("Text editor")

window.rowconfigure(0, minsize=800, weight=1) #set the height of the first row to 800 pix
window.columnconfigure(1, minsize=800, weight=1) #set the width the second column to 800

txt_edit = tk.Text(window)

frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open=tk.Button(frm_buttons, text="open", command=open_file)
btn_save=tk.Button(frm_buttons, text="Save as...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5) #expand horizontally in both directions and fill the entire frame
btn_save.grid(row=1, column=0, sticky="ew", padx=5) #expand horizontally in both directions and fill the entire frame

frm_buttons.grid(row=0, column=0, sticky="ns") #force the frame to expand vertically
txt_edit.grid(row=0, column=1, sticky="nsew") #force the frame to expand in every direction.

window.mainloop()