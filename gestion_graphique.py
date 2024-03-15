import tkinter as tk
from tkinter import ttk
import chiffrage_dechiffrage as c
import Vigenere as v

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

# Callback for the encrypt button
def encrypt_text():
    plain_text = text_plain.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(plain_text, shift, mode='encrypt')
    text_encrypted.delete("1.0", tk.END)
    text_encrypted.insert(tk.END, encrypted_text)

# Callback for the decrypt button
def decrypt_text():
    encrypted_text = text_encrypted.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    plain_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
    text_plain.delete("1.0", tk.END)
    text_plain.insert(tk.END, plain_text)

# Create the main application window
root = tk.Tk()
root.title('Application de Chiffrage de Texte')
root.configure(bg='blue')

# Menu bar at the top
menu_bar = tk.Menu(root, bg='white')
root.config(menu=menu_bar)

# Menu items
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Chiffrage de Texte')  # Placeholder for functionality
file_menu.add_command(label='Chiffrage de Fichiers')  # Placeholder for functionality
file_menu.add_command(label='Chiffrage de Contenu Web')  # Placeholder for functionality
file_menu.add_separator()
file_menu.add_command(label='Fermer', command=root.quit)
menu_bar.add_cascade(label='Fichier', menu=file_menu)

# Create the main frame
main_frame = tk.Frame(root, bg='blue')
main_frame.pack(padx=10, pady=10)

# Left side (Plain text)
label_plain = tk.Label(main_frame, text='Texte en clair:')
label_plain.grid(row=0, column=0, padx=5, pady=5)
text_plain = tk.Text(main_frame, height=10, width=40)
text_plain.grid(row=1, column=0, padx=5, pady=5)



# Right side (Encrypted text)
label_encrypted = tk.Label(main_frame, text='Texte Chiffré:')
label_encrypted.grid(row=0, column=2, padx=5, pady=5)
text_encrypted = tk.Text(main_frame, height=10, width=40)
text_encrypted.grid(row=1, column=2, padx=5, pady=5)

# Encryption method dropdown
# Encryption method dropdown and label
encryption_methods = tk.StringVar()
encryption_method_label = tk.Label(main_frame, text='Fonction de chiffrage:')
encryption_method_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
encryption_dropdown = ttk.Combobox(main_frame, textvariable=encryption_methods, state="readonly")
encryption_dropdown['values'] = ('César', 'César avec décalage incrémental', 'Vigenère')
encryption_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky='w')
# Entry for the number of shifts
shift_label = tk.Label(main_frame, text='Nombre de décalage:')
shift_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
shift_entry = tk.Entry(main_frame)
shift_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

# Middle (Buttons)
button_frame = tk.Frame(main_frame, bg='blue')
button_frame.grid(row=1, column=1, padx=5, pady=5)
encrypt_button = tk.Button(button_frame, text='=> Encoder =>', command=lambda: c.codage(shift_entry.get(), text_plain.get("1.0", tk.END), text_encrypted))
encrypt_button.pack(side=tk.TOP, pady=5)
decrypt_button = tk.Button(button_frame, text='<= Décoder<=', command=decrypt_text)
decrypt_button.pack(side=tk.TOP, pady=5)

root.mainloop()


