# gui_app.py
import tkinter as tk
from tkinter import messagebox
from mini_aes import MiniAES

def parse_input(text):
    try:
        parts = text.strip().split()
        if len(parts) != 4:
            raise ValueError("Input must be 4 hex bytes")
        return [int(x, 16) for x in parts]
    except Exception as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")
        return None

def format_output(ciphertext):
    return ' '.join(f"{byte:02X}" for byte in ciphertext)

def encrypt_action():
    plaintext = parse_input(plaintext_entry.get())
    key = parse_input(key_entry.get())
    if plaintext and key:
        aes = MiniAES(key)
        ciphertext = aes.encrypt(plaintext)
        result_var.set("Ciphertext: " + format_output(ciphertext))

def decrypt_action():
    ciphertext = parse_input(ciphertext_entry.get())
    key = parse_input(key_entry.get())
    if ciphertext and key:
        aes = MiniAES(key)
        decrypted = aes.decrypt(ciphertext)
        decrypted_var.set("Decrypted: " + format_output(decrypted))

# GUI setup
root = tk.Tk()
root.title("Mini-AES GUI")

tk.Label(root, text="Plaintext (hex):").grid(row=0, column=0)
plaintext_entry = tk.Entry(root)
plaintext_entry.grid(row=0, column=1)

tk.Label(root, text="Key (hex):").grid(row=1, column=0)
key_entry = tk.Entry(root)
key_entry.grid(row=1, column=1)

encrypt_btn = tk.Button(root, text="Encrypt", command=encrypt_action)
encrypt_btn.grid(row=2, column=0, columnspan=2)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).grid(row=3, column=0, columnspan=2)

# Decryption section
tk.Label(root, text="Ciphertext (hex):").grid(row=4, column=0)
ciphertext_entry = tk.Entry(root)
ciphertext_entry.grid(row=4, column=1)

decrypt_btn = tk.Button(root, text="Decrypt", command=decrypt_action)
decrypt_btn.grid(row=5, column=0, columnspan=2)

decrypted_var = tk.StringVar()
tk.Label(root, textvariable=decrypted_var).grid(row=6, column=0, columnspan=2)

root.mainloop()
