import tkinter as tk
from tkinter import ttk, filedialog, Menu

# Define the encryption/decryption functions (placeholders for this example)
def encrypt_decrypt(text, shift, mode='encrypt'):
    # Placeholder for the actual encryption/decryption logic
    return text

# Define the GUI callbacks
def encode():
    url = entry_url.get()
    selector = entry_selector.get()
    # Placeholder for the actual encoding logic using url and selector
    result = encrypt_decrypt(url + selector, int(shift_entry.get()), mode='encrypt')
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, result)

def decode():
    encrypted_text = text_result.get("1.0", tk.END).strip()
    result = encrypt_decrypt(encrypted_text, int(shift_entry.get()), mode='decrypt')
    entry_url.delete(0, tk.END)
    entry_url.insert(0, result)

# Initialize the main window
root = tk.Tk()
root.title('tk')
root.configure(bg='light grey')

# Menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Chiffrage de Texte')
file_menu.add_command(label='Chiffrage de Fichier')
file_menu.add_command(label='Chiffrage de contenu web')
file_menu.add_separator()
file_menu.add_command(label='Fermer', command=root.quit)
menu_bar.add_cascade(label='File', menu=file_menu)

# Main frame
main_frame = tk.Frame(root, bg='light grey')
main_frame.pack(fill='both', expand=True)

# Left frame for inputs, options, and buttons
left_frame = tk.Frame(main_frame, bg='light grey')
left_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=10, pady=10)

# URL and Selector Entries and Labels
label_url_selector = tk.Label(left_frame, text="Url, et Selecteur:", bg='light grey')
label_url_selector.pack(fill='x')
entry_url = ttk.Entry(left_frame, width=50)
entry_url.pack(fill='x', padx=5, pady=5)
entry_selector = ttk.Entry(left_frame, width=50)
entry_selector.pack(fill='x', padx=5, pady=5)

# Button Frame for vertical alignment
button_frame = tk.Frame(left_frame, bg='light grey')
button_frame.pack(fill='x', padx=5, pady=5)

# Encode and Decode Buttons
button_encode = tk.Button(button_frame, text='=> Encoder =>', command=encode)
button_encode.pack(side=tk.TOP, fill='x')
button_decode = tk.Button(button_frame, text='<= Decoder <=', command=decode)
button_decode.pack(side=tk.TOP, fill='x')

# Dropdown for encryption methods and labels
label_method = tk.Label(left_frame, text='Fonction de chiffrage:', bg='light grey')
label_method.pack(side=tk.LEFT,padx=1)
encryption_methods = tk.StringVar()
encryption_dropdown = ttk.Combobox(left_frame, textvariable=encryption_methods, state="readonly")
encryption_dropdown['values'] = ('Cesar', 'César avec décalage incrémental', 'Vigenère')  # Add other methods as needed
encryption_dropdown.pack(fill= 'x')
encryption_dropdown.current(0)

# Shift Entry and Label in their own frame for vertical alignment
shift_frame = tk.Frame(left_frame, bg='light grey')
shift_frame.pack(fill='x', pady=5)
label_shift = tk.Label(shift_frame, text='Nombre de décalage:', bg='light grey')
label_shift.pack(side=tk.LEFT)
shift_entry = tk.Entry(shift_frame, width=5)
shift_entry.pack(side=tk.LEFT, padx=5)
shift_entry.insert(0, "1")  # Default shift value

# Right frame for result
right_frame = tk.Frame(main_frame, bg='light grey')
right_frame.pack(side=tk.RIGHT, fill='both', expand=True, padx=10, pady=10)

# Result Text Area and Label
label_result = tk.Label(right_frame, text='Texte Resultat:', bg='light grey')
label_result.pack(fill='x')
text_result = tk.Text(right_frame, height=10, width=50, bg='lavender')
text_result.pack(fill='both', expand=True, padx=5, pady=5)

root.mainloop()


