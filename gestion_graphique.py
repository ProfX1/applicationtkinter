import tkinter as tk
from tkinter import END, ttk
import chiffrage_dechiffrage as c
import requests
from bs4 import BeautifulSoup
from tkinter.filedialog import askopenfilename

def coding(encryption_drop,shift_entry, text_unencrypted, text_encrypt):
    text_encrypt.delete('1.0', END)

    if encryption_drop == 'César':
        text_encrypte = c.cesar_encryption(text_unencrypted)
        text_encrypt.insert('1.0', text_encrypte)

    elif encryption_drop == 'César avec décalage incrémental':
        text_encrypte = c.cesar_encryption(text_unencrypted, int(shift_entry))
        text_encrypt.insert('1.0', text_encrypte)

    elif encryption_drop == 'Vigenère':
        text_encrypte = c.encode(shift_entry, text_unencrypted)
        text_encrypt.insert('1.0', text_encrypte)

    else:
        return
    
def decoding(encryption_drop,shift_entry, text_unencrypted, text_encrypt):
    text_unencrypted.delete('1.0', END)

    if encryption_drop == 'César':
        text_nonencrypted = c.cesar_decryption(text_encrypt)
        text_unencrypted.insert('1.0', text_nonencrypted)
    
    elif encryption_drop == 'César avec décalage incrémental':
        text_nonencrypted = c.cesar_decryption(text_encrypt, int(shift_entry))
        text_unencrypted.insert('1.0', text_nonencrypted)
        
    elif encryption_drop == 'Vigenère':
        text_nonencrypted = c.decode(shift_entry, text_encrypt)
        text_unencrypted.insert('1.0', text_nonencrypted)
    else:
        return
    
def coding2(encryption_drop,shift_entry, text_encryptOld):
    text_unencrypted = text_encryptOld
    
    # text_encrypt.delete('1.0', END)

    if encryption_drop == 'César':
        return c.cesar_encryption(text_unencrypted)
        # text_encrypt.insert('1.0', text_encrypte)

    elif encryption_drop == 'César avec décalage incrémental':
        return c.cesar_encryption(text_unencrypted, int(shift_entry))
        # text_encrypt.insert('1.0', text_encrypte)

    elif encryption_drop == 'Vigenère':
        return c.encode(shift_entry, text_unencrypted)
        # text_encrypt.insert('1.0', text_encrypte)

    else:
        return
    
def decoding2(encryption_drop,shift_entry, text_encryption):
    # text_encryption=text_encrypt.get("1.0", END)
    # text_encrypt.delete('1.0', END)
    print("I am in decoding2")
    if encryption_drop == 'César':
        print("I am in cesar decoding2")
        print(text_encryption.get("1.0", END))
        text_nonencrypted = c.cesar_decryption(text_encryption.get("1.0", END))
        text_encryption.delete('1.0', END)
        text_encryption.insert('1.0', text_nonencrypted)
    
    elif encryption_drop == 'César avec décalage incrémental':
        print("I am in cesar with shift decoding2")
        text_nonencrypted = c.cesar_decryption(text_encryption.get("1.0", END), int(shift_entry))
        text_encryption.delete('1.0', END)
        text_encryption.insert('1.0', text_nonencrypted)
        
    elif encryption_drop == 'Vigenère':
        print("I am in Vigenere")
        text_nonencrypted = c.decode(shift_entry, text_encryption.get("1.0", END))
        text_encryption.delete('1.0', END)
        text_encryption.insert('1.0', text_nonencrypted)
    else:
        print("no action taken")
        return

def scrape_and_cipher(url, selector, method,shift, text_widget):
    url_get = url.get()
    selector_get = selector.get()
    print(url_get)
    print(selector_get)
    print(method)
    print(shift)
    
    try:
        # Fetch the content of the URL
        response = requests.get(url_get)
        response.raise_for_status()  # Raise an exception for HTTP errors
        html = response.text
        
        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find element by CSS selector
        element = soup.select_one(selector_get)
        
        if element:
            content = element.get_text()
            text_widget.delete(1.0, END)
            # text_widget.insert(1.0, content)
            # print(text_widget.get("1.0", END))
            text_widget.insert('1.0', coding2(method,shift, content))
            
            
        else:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, 'Element not found with the specified selector.')
    except Exception as e:
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, 'An error occurred. Please check the URL or selector.')
        print('An error occurred:', e)
# Create the main application window
root = tk.Tk()
root.title('Application de Chiffrage de Texte')
root.configure(bg='light grey')

def clear_screen():
    # Destroy all widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()
def screen1():
    clear_screen()
    menu()
    # Create the main frame
    main_frame = tk.Frame(root, bg='light grey')
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
    encryption_dropdown = ttk.Combobox(main_frame, textvariable=encryption_methods, state="readonly", )
    encryption_dropdown['values'] = ('César', 'César avec décalage incrémental', 'Vigenère')
    encryption_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky='w')
    
    # Entry for the number of shifts
    shift_label = tk.Label(main_frame, text='Nombre de décalage:')
    shift_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
    shift_entry = tk.Entry(main_frame)
    shift_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    # Middle (Buttons)
    button_frame = tk.Frame(main_frame, bg='light grey')
    button_frame.grid(row=1, column=1, padx=5, pady=5)
    encrypt_button = tk.Button(button_frame, text='=> Encoder =>', command=lambda: coding(encryption_methods.get(),shift_entry.get(), text_plain.get("1.0", END), text_encrypted))
    encrypt_button.pack(side=tk.TOP, pady=5)
    decrypt_button = tk.Button(button_frame, text='<= Décoder<=', command=lambda: decoding(encryption_methods.get(),shift_entry.get(), text_plain, text_encrypted.get("1.0", END)))
    decrypt_button.pack(side=tk.TOP, pady=5)

def screen2():
    clear_screen()
    menu()

    def open_file(filetext):
        filepath = askopenfilename(
            filetypes=[("Text files", "*.txt")]
        )
        if not filepath:
            return
        txt_Data = open(filepath,"r", encoding="utf-8")
        filetext.delete('1.0', END)
        filetext.insert('1.0', txt_Data.readlines())

    main_frame = tk.Frame(root, bg='light grey')
    main_frame.pack(padx=10, pady=10)

    # Left side (Plain text)
    label_plain = tk.Label(main_frame, text='Texte en clair:')
    label_plain.grid(row=0, column=0, padx=5, pady=5)
    text_plain = tk.Text(main_frame, height=10, width=40)
    text_plain.grid(row=1, column=0, padx=5, pady=5)

    # Middle open file
    btn_open = tk.Button(main_frame, text="Open File", command=lambda: open_file(text_plain))
    btn_open.grid(row=0, column=1, padx=5, pady=5)

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
    encryption_dropdown = ttk.Combobox(main_frame, textvariable=encryption_methods, state="readonly", )
    encryption_dropdown['values'] = ('César', 'César avec décalage incrémental', 'Vigenère')
    encryption_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky='w')
    
    # Entry for the number of shifts
    shift_label = tk.Label(main_frame, text='Nombre de décalage:')
    shift_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
    shift_entry = tk.Entry(main_frame)
    shift_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    # Middle (Buttons)
    button_frame = tk.Frame(main_frame, bg='light grey')
    button_frame.grid(row=1, column=1, padx=5, pady=5)
    encrypt_button = tk.Button(button_frame, text='=> Encoder =>', command=lambda: coding(encryption_methods.get(),shift_entry.get(), text_plain.get("1.0", END), text_encrypted))
    encrypt_button.pack(side=tk.TOP, pady=5)
    decrypt_button = tk.Button(button_frame, text='<= Décoder<=', command=lambda: decoding(encryption_methods.get(),shift_entry.get(), text_plain, text_encrypted.get("1.0", END)))
    decrypt_button.pack(side=tk.TOP, pady=5)

def screen3():
    clear_screen()
    menu()
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

    button_frame = tk.Frame(left_frame, bg='white')
    button_frame.pack(fill='x', padx=5, pady=5)

    # Dropdown for encryption methods and labels
    label_method = tk.Label(left_frame, text='Fonction de chiffrage:', bg='white')
    label_method.pack(side=tk.LEFT,padx=1)
    encryption_methods = tk.StringVar()
    encryption_dropdown = ttk.Combobox(left_frame, textvariable=encryption_methods, state="readonly")
    encryption_dropdown['values'] = ('César', 'César avec décalage incrémental', 'Vigenère')  # Add other methods as needed
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

    # Encode and Decode Buttons
    button_encode = tk.Button(button_frame, text='=> Encoder =>', command=lambda: scrape_and_cipher(entry_url, entry_selector, encryption_methods.get(), shift_entry.get(), text_result))
    button_encode.pack(side=tk.TOP, fill='x')
    button_decode = tk.Button(button_frame, text='<= Decoder <=', command=lambda: decoding2(encryption_methods.get(), shift_entry.get(), text_result))  # Pass Text widget object
    button_decode.pack(side=tk.TOP, fill='x')

def menu():
    # Menu bar at the top
    menu_bar = tk.Menu(root, bg='white')
    root.config(menu=menu_bar)

    # Menu items
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Chiffrage de Texte', command=screen1)  # Placeholder for functionality
    file_menu.add_command(label='Chiffrage de Fichiers', command=screen2)  # Placeholder for functionality
    file_menu.add_command(label='Chiffrage de Contenu Web', command=screen3)  # Placeholder for functionality
    file_menu.add_separator()
    file_menu.add_command(label='Fermer', command=root.quit)
    menu_bar.add_cascade(label='Fichier', menu=file_menu)



screen1()
root.mainloop()


