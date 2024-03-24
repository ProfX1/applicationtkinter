import json
import tkinter as tk
from tkinter import ttk

from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[("Json Files", "*.json")]
    )
    if not filepath:
        return
    jsonData = json.load(open(filepath, mode="r", encoding="utf-8"))
    txtfirstName.delete(0, tk.END)
    txtfirstName.insert(0, jsonData["firstname"])

    txtlastName.delete(0, tk.END)
    txtlastName.insert(0, jsonData["lastname"])

    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Json Files", "*.json")],
    )
    if not filepath:
        return
    jsonData = {
        "firstname": txtfirstName.get(),
        "lastname": txtlastName.get()
    }
    json.dump(jsonData, open(filepath, mode="w", encoding="utf-8"))
    window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
window.title("Simple Text Editor")

btn_open = tk.Button(window, text="Open", command=open_file).pack()
btn_save = tk.Button(window, text="Save As...", command=save_file).pack()

lblfirstName = ttk.Label(window, text="First Name").pack()
txtfirstName = ttk.Entry(window)
txtfirstName.pack()

lbllastName = ttk.Label(window, text="Last Name").pack()
txtlastName = ttk.Entry(window)
txtlastName.pack()

window.mainloop()