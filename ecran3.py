import tkinter as tk
from tkinter import ttk, filedialog, Menu

# Fonction de simulation pour l'encodage
def encode():
    # Simuler l'encodage
    text = entry_url.get() + " " + entry_selector.get()
    encoded_text = f"Encodé: {text}"
    text_result.delete('1.0', tk.END)
    text_result.insert(tk.END, encoded_text)

# Fonction de simulation pour le décodage
def decode():
    # Simuler le décodage
    encoded_text = text_result.get('1.0', tk.END)
    decoded_text = f"Décodé: {encoded_text}"
    text_result.delete('1.0', tk.END)
    text_result.insert(tk.END, decoded_text)

# Initialiser la fenêtre principale
root = tk.Tk()
root.title('Application de Chiffrage de contenu web')
main_frame = tk.Frame(root, bg='light grey')

# Create the menu bar
menu = tk.Menu(root)
# Configure the menu bar
root.config(menu=menu)

# Fonctions pour afficher différents contenus
def show_text_encryption():
        clear_main_frame()
        tk.Label(main_frame, text="Chiffrage de Texte").pack()

def show_file_encryption():
        clear_main_frame()
        tk.Label(main_frame, text="Chiffrage de Fichier").pack()

def show_web_content_encryption():
        clear_main_frame()
        tk.Label(main_frame, text="Chiffrage de contenu web").pack()

def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()
        
 # Ajout des éléments de menu
menu.add_command(label='Chiffrage de Texte', command=show_text_encryption)
menu.add_command(label='Chiffrage de Fichier', command=show_file_encryption)
menu.add_command(label='Chiffrage de contenu web', command=show_web_content_encryption)
menu.add_separator()
menu.add_command(label='Fermer', command=root.quit)

show_web_content_encryption()  # Afficher par défaut le contenu de chiffrage web

# Main frame
main_frame = tk.Frame(root, bg='light grey')
main_frame.pack(fill='both', expand=True)

# Left frame for inputs, options, and buttons
left_frame = tk.Frame(main_frame, bg='light grey')
left_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=10, pady=10)

# URL and Selector Entries and Labels
label_url_selector = tk.Label(left_frame, text="Url, et Selecteur:", bg='white')
label_url_selector.pack(fill='x')
entry_url = ttk.Entry(left_frame, width=50)
entry_url.pack(fill='x', padx=5, pady=5)
entry_selector = ttk.Entry(left_frame, width=50)
entry_selector.pack(fill='x', padx=5, pady=5)

# Button Frame 
button_frame = tk.Frame(left_frame, bg='white')
button_frame.pack(fill='x', padx=5, pady=5)

# Encode and Decode Buttons
button_encode = tk.Button(button_frame, text='=> Encoder =>', command=encode)
button_encode.pack(side=tk.TOP, fill='x')
button_decode = tk.Button(button_frame, text='<= Decoder <=', command=decode)
button_decode.pack(side=tk.TOP, fill='x')

# Dropdown for encryption methods and labels
label_method = tk.Label(left_frame, text='Fonction de chiffrage:', bg='white')
label_method.pack(side=tk.LEFT,padx=1)
encryption_methods = tk.StringVar()
encryption_dropdown = ttk.Combobox(left_frame, textvariable=encryption_methods, state="readonly")
encryption_dropdown['values'] = ('Cesar', 'César avec décalage incrémental', 'Vigenère')  # Add other methods as needed
encryption_dropdown.pack(side=tk.LEFT,padx=1)
encryption_dropdown.current(0)

# Shift Entry and Label 
shift_frame = tk.Frame(left_frame, bg='white')
shift_frame.pack(fill='x', padx=5)
label_shift = tk.Label(shift_frame, text='Nombre de décalage:', bg='white')
label_shift.pack(side=tk.LEFT)
shift_entry = tk.Entry(shift_frame, width=5)
shift_entry.pack(side=tk.LEFT, padx=5)
shift_entry.insert(0, "1")  # Default shift value

# Right frame for result
right_frame = tk.Frame(main_frame, bg='light grey')
right_frame.pack(side=tk.RIGHT, fill='both', expand=True, padx=10, pady=10)

# Result Text Area and Label
label_result = tk.Label(right_frame, text='Texte Resultat:', bg='white')
label_result.pack(fill='x')
text_result = tk.Text(right_frame, height=10, width=50, bg='lavender')
text_result.pack(fill='both', expand=True, padx=5, pady=5)

root.mainloop()


