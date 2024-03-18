import tkinter as tk
from tkinter import ttk
import chiffrage_dechiffrage as c

def coding(encryption_drop,shift_entry, text_unencrypted, text_encrypt):
    if encryption_dropdown in ('César', 'César avec décalage incrémental'):
        c.cesar_encryption(text_unencrypted, shift_entry)
    elif encryption_dropdown.get() == 'Vigenère':
        c.encode(shift_entry, text_plain)
    else:
        return
def decoding(encryption_drop,shift_entry, text_unencrypted, text_encrypt):
    if encryption_drop in ('César', 'César avec décalage incrémental'):
        c.cesar_decryption(text_encrypt, shift_entry)
    elif encryption_dropdown == 'Vigenère':
        c.decode(shift_entry, text_plain)
    else:
        return


# Create the main application window
root = tk.Tk()
root.title('Application de Chiffrage de Texte')
root.configure(bg='grey')

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
main_frame = tk.Frame(root, bg='grey')
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
button_frame = tk.Frame(main_frame, bg='grey')
button_frame.grid(row=1, column=1, padx=5, pady=5)
encrypt_button = tk.Button(button_frame, text='=> Encoder =>', command=lambda: coding(encryption_dropdown.get(),shift_entry.get(), text_plain.get("1.0", tk.END), text_encrypted.get("1.0", tk.END)))
encrypt_button.pack(side=tk.TOP, pady=5)
decrypt_button = tk.Button(button_frame, text='<= Décoder<=', command=lambda: decoding(encryption_dropdown.get(),shift_entry.get(), text_plain.get("1.0", tk.END), text_encrypted.get("1.0", tk.END)))
decrypt_button.pack(side=tk.TOP, pady=5)

root.mainloop()


