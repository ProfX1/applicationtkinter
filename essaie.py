import tkinter as tk
from tkinter import ttk, messagebox

# Caesar Cipher logic
def caesar_cipher(text, shift, mode='encrypt'):
    if not text.isascii() or not text.isprintable():
        messagebox.showerror("Erreur", "Le texte contient des caractères non pris en charge.")
        return ""
    
    result = ""
    for char in text:
        if char.isalpha():  # Check if it's an alphabetic character
            shift_amount = shift if mode == 'encrypt' else -shift
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift_amount) % 26 + ord(base))
        else:
            result += char
    return result

# Implementing other encryption functions as needed
def encrypt_decrypt(text, shift, mode='encrypt', method='Cesar'):
    if method == 'Cesar':
        return caesar_cipher(text, shift, mode)
    # Additional methods can be implemented here
    return text

# Define the GUI callbacks
def encode():
    url = entry_url.get()
    selector = entry_selector.get()
    method = encryption_methods.get()
    try:
        shift_value = int(combobox.get())
    except ValueError:
        messagebox.showerror("Erreur", "Le nombre de décalage doit être un nombre entier.")
        return
    
    result = encrypt_decrypt(url + selector, shift_value, mode='encrypt', method=method)
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, result)

def decode():
    encrypted_text = text_result.get("1.0", tk.END).strip()
    method = encryption_methods.get()
    try:
        shift_value = int(combobox.get())
    except ValueError:
        messagebox.showerror("Erreur", "Le nombre de décalage doit être un nombre entier.")
        return
    
    result = encrypt_decrypt(encrypted_text, shift_value, mode='decrypt', method=method)
    entry_url.delete(0, tk.END)
    entry_url.insert(0, result)

# Initialize the main window
root = tk.Tk()
root.title('Application de Chiffrage de contenu web')

# Create the menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# Add menu items directly to the menu bar for horizontal layout
menu.add_command(label='Chiffrage de Texte')
menu.add_command(label='Chiffrage de Fichier')
menu.add_command(label='Chiffrage de contenu web')
menu.add_separator()
menu.add_command(label='Fermer', command=root.quit)

# Main frame
main_frame = tk.Frame(root, bg='light grey')
main_frame.pack(fill='both', expand=True)

# Left frame for inputs, options, and buttons
left_frame = tk.Frame(main_frame, bg='light grey')
left_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=10, pady=10)

# URL and Selector Entries and Labels
label_url_selector = tk.Label(left_frame, text="Url, et Selecteur :", bg='white')
label_url_selector.pack(fill='x')
entry_url = ttk.Entry(left_frame, width=50)
entry_url.pack(fill='x', padx=5, pady=5)
entry_selector = ttk.Entry(left_frame, width=50)
entry_selector.pack(fill='x', padx=5, pady=5)

# Button Frame for vertical alignment
button_frame = tk.Frame(left_frame, bg='white')
button_frame.pack(fill='x', padx=5, pady=5)

# Encode and Decode Buttons
button_encode = tk.Button(button_frame, text='=> Encoder =>', command=encode)
button_encode.pack(side=tk.TOP, fill='x')
button_decode = tk.Button(button_frame, text='<= Decoder <=', command=decode)
button_decode.pack(side=tk.TOP, fill='x')

# Dropdown for encryption methods and labels
label_method = tk.Label(left_frame, text='Fonction de chiffrage :', bg='white')
label_method.pack(side=tk.LEFT, padx=1)
encryption_methods = tk.StringVar()
encryption_dropdown = ttk.Combobox(left_frame, textvariable=encryption_methods, state="readonly")
encryption_dropdown['values'] = ('Cesar', 'César avec décalage incrémental', 'Vigenère')  # Add other methods as needed
encryption_dropdown.pack(side=tk.LEFT, padx=1)
encryption_dropdown.current(0)


# Create a label
label = tk.Label(left_frame, text="Nombre de decalage :",bg="white")
label.pack(side=tk.LEFT, padx=(10, 0))

# Create a Combobox
combobox_values = [str(i) for i in range(26)]  # Assuming the values range from 1 to 10
combobox = ttk.Combobox(left_frame, values=combobox_values, width=3)
combobox.set("1")  # Set the default value to 1
combobox.pack(side=tk.LEFT, padx=2, pady=2)

# Right frame for result
right_frame = tk.Frame(main_frame, bg='light grey')
right_frame.pack(side=tk.RIGHT, fill='both', expand=True, padx=10, pady=10)

# Result Text Area and Label
label_result = tk.Label(right_frame, text='Texte Resultat :', bg='white')
label_result.pack(fill='x')
text_result = tk.Text(right_frame, height=10, width=50, bg='lavender')
text_result.pack(fill='both', expand=True, padx=1, pady=5)

root.mainloop()
