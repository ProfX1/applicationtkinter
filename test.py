import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def scrape_and_cipher():
    url = url_entry.get()
    selector = selector_entry.get()
    try:
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        html = response.text
        
        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find element by CSS selector
        element = soup.select_one(selector)
        
        if element:
            content = element.get_text()
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, content)
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, 'Element not found with the specified selector.')
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, 'An error occurred. Please check the URL or selector.')
        print('An error occurred:', e)

def encrypt_decrypt(mode):
    content = result_text.get(1.0, tk.END)
    key = key_entry.get()
    # Implement encryption or decryption here
    # Example: encrypted_text = vigenere_cipher(content, key, mode)
    # Replace vigenere_cipher with your implementation
    # Display the result in the result_text widget

# Create the main Tkinter window
root = tk.Tk()
root.title("Web Scraper & Vigenère Cipher")

# URL Entry
url_label = ttk.Label(root, text="URL:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
url_entry = ttk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

# CSS Selector Entry
selector_label = ttk.Label(root, text="CSS Selector:")
selector_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
selector_entry = ttk.Entry(root, width=50)
selector_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

# Scrape & Cipher Button
scrape_button = ttk.Button(root, text="Scrape & Cipher", command=scrape_and_cipher)
scrape_button.grid(row=2, column=0, padx=5, pady=5)

# Result Text
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Key Entry
key_label = ttk.Label(root, text="Key:")
key_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
key_entry = ttk.Entry(root, width=50)
key_entry.grid(row=4, column=1, padx=5, pady=5, columnspan=2)



root.mainloop()
