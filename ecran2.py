import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo

# Encryption and decryption functions
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            char_code = ord(char) + shift_amount
            if char.islower():
                char_code = (char_code - 97) % 26 + 97
            else:
                char_code = (char_code - 65) % 26 + 65
            result += chr(char_code)
        else:
            result += char
    return result

# File operations
def open_file(entry):
    filepath = filedialog.askopenfilename()
    if filepath:
        entry.delete(0, tk.END)
        entry.insert(0, filepath)

def encrypt_file():
    source_path = file_plain_entry.get()
    dest_path = file_encrypted_entry.get()
    shift = int(shift_entry.get())
    # Implement file encryption logic here
    showinfo("Info", f"The file {source_path} would be encrypted and saved to {dest_path}.")

def decrypt_file():
    source_path = file_encrypted_entry.get()
    dest_path = file_plain_entry.get()
    shift = int(shift_entry.get())
    # Implement file decryption logic here
    showinfo("Info", f"The file {source_path} would be decrypted and saved to {dest_path}.")

# GUI Callbacks
def encrypt_text():
    plain_text = text_plain.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(plain_text, shift, mode='encrypt')
    text_encrypted.delete("1.0", tk.END)
    text_encrypted.insert(tk.END, encrypted_text)

def decrypt_text():
    encrypted_text = text_encrypted.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    plain_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
    text_plain.delete("1.0", tk.END)
    text_plain.insert(tk.END, plain_text)

# Create the main application window
root = tk.Tk()
root.title('Application de Chiffrage')
root.configure(bg='blue')

# Menu bar at the top
menu_bar = tk.Menu(root, bg='white')
root.config(menu=menu_bar)

# Menu items
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Chiffrage de Texte')  # Placeholder for functionality
file_menu.add_command(label='Chiffrage de Fichiers')  # Placeholder for functionality
file_menu.add_separator()
file_menu.add_command(label='Fermer', command=root.quit)
menu_bar.add_cascade(label='Fichier', menu=file_menu)

# Text Encryption Frame
text_frame = tk.Frame(root, bg='blue')
text_frame.pack(padx=10, pady=10)

# Text Encryption Widgets
label_plain = tk.Label(text_frame, text='Texte en clair:')
label_plain.grid(row=0, column=0, padx=5, pady=5)
text_plain = tk.Text(text_frame, height=10, width=40)
text_plain.grid(row=1, column=0, padx=5, pady=5)

button_frame = tk.Frame(text_frame, bg='blue')
button_frame.grid(row=1, column=1, padx=5, pady=5)
encrypt_button = tk.Button(button_frame, text='Encoder', command=encrypt_text)
encrypt_button.pack(side=tk.TOP, pady=5)
decrypt_button = tk.Button(button_frame, text='Décoder', command=decrypt_text)
decrypt_button.pack(side=tk.TOP, pady=5)

label_encrypted = tk.Label(text_frame, text='Texte Chiffré:')
label_encrypted.grid(row=0, column=2, padx=5, pady=5)
text_encrypted = tk.Text(text_frame, height=10, width=40)
text_encrypted.grid(row=1, column=2, padx=5, pady=5)

encryption_methods = tk.StringVar()
encryption_method_label = tk.Label(text_frame, text='Fonction de chiffrage:')
encryption_method_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
encryption_dropdown = ttk.Combobox(text_frame, textvariable=encryption_methods, state="readonly")
encryption_dropdown['values'] = ('César', 'César avec décalage incrémental', 'Vigenère')
encryption_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky='w')

shift_label = tk.Label(text_frame, text='Nombre de décalage:')
shift_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
shift_entry = tk.Entry(text_frame)
shift_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

# File Encryption Frame
file_frame = tk.Frame(root, bg='blue')
file_frame.pack(padx=10, pady=10, fill='x')

# File Encryption Widgets
file_plain_label = tk.Label(file_frame, text='Fichier en clair:')
file_plain_label.grid(row=0, column=0, padx=5, pady=5)
file_plain_entry = tk.Entry(file_frame, width=50)
file_plain_entry.grid(row=0, column=1, padx=5, pady=5)
file_plain_button = tk.Button(file_frame, text='Ouvrir', command=lambda: open_file(file_plain_entry))
file_plain_button.grid(row=0, column=2, padx=5, pady=5)

file_encrypted_label = tk.Label(file_frame, text='Fichier Chiffré:')
file_encrypted_label.grid(row=1, column=0, padx=5, pady=5)
file_encrypted_entry = tk.Entry(file_frame, width=50)
file_encrypted_entry.grid(row=1, column=1, padx=5, pady=5)
file_encrypted_button = tk.Button(file_frame, text='Ouvrir', command=lambda: open_file(file_encrypted_entry))
file_encrypted_button.grid(row=1, column=2, padx=5, pady=5)

encrypt_file_button = tk.Button(file_frame, text='Chiffrer Fichier', command=encrypt_file)
encrypt_file_button.grid(row=2, column=1, padx=5, pady=5, sticky='e')

decrypt_file_button = tk.Button(file_frame, text='Déchiffrer Fichier', command=decrypt_file)
decrypt_file_button.grid(row=2, column=2, padx=5, pady=5, sticky='w')

root.mainloop()
