# gui_app.py
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import json
from mini_aes import MiniAES
import os

def parse_input(text):
    try:
        parts = text.strip().split()
        if len(parts) != 4:
            raise ValueError("Input harus 4 byte hex")
        return [int(x, 16) for x in parts]
    except Exception as e:
        messagebox.showerror("Error Input", f"Input tidak valid: {e}")
        return None

def format_output(data):
    return ' '.join(f"{byte:02X}" for byte in data)

def encrypt_action():
    plaintext = parse_input(plaintext_entry.get())
    key = parse_input(key_entry.get())
    if plaintext and key:
        mode = mode_var.get()
        show_rounds = show_rounds_var.get()
        
        aes = MiniAES(key)
        
        if mode == "Single Block":
            ciphertext = aes.encrypt(plaintext, show_rounds=show_rounds)
            result_var.set("Ciphertext: " + format_output(ciphertext))
            log_text.insert(tk.END, f"\n--- ENKRIPSI ---\nPlaintext: {format_output(plaintext)}\nKey: {format_output(key)}\nCiphertext: {format_output(ciphertext)}\n")
        
        elif mode == "ECB":
            text_input = text_entry.get("1.0", tk.END).strip()
            # Convert text to list of bytes (using ASCII values)
            bytes_input = [ord(c) for c in text_input]
            blocks = aes.split_into_blocks(bytes_input)
            
            encrypted_blocks = aes.ecb_encrypt(blocks, show_rounds=show_rounds)
            flat_result = [byte for block in encrypted_blocks for byte in block]
            
            result_var.set("ECB Mode Encryption Complete")
            log_text.insert(tk.END, f"\n--- ECB ENKRIPSI ---\nJumlah blok: {len(blocks)}\nHasil: {format_output(flat_result)}\n")
        
        elif mode == "CBC":
            iv = parse_input(iv_entry.get())
            if not iv:
                messagebox.showinfo("Input Error", "IV dibutuhkan untuk mode CBC")
                return
                
            text_input = text_entry.get("1.0", tk.END).strip()
            # Convert text to list of bytes (using ASCII values)
            bytes_input = [ord(c) for c in text_input]
            blocks = aes.split_into_blocks(bytes_input)
            
            encrypted_blocks = aes.cbc_encrypt(blocks, iv, show_rounds=show_rounds)
            flat_result = [byte for block in encrypted_blocks for byte in block]
            
            result_var.set("CBC Mode Encryption Complete")
            log_text.insert(tk.END, f"\n--- CBC ENKRIPSI ---\nIV: {format_output(iv)}\nJumlah blok: {len(blocks)}\nHasil: {format_output(flat_result)}\n")
        
        log_text.see(tk.END)

def decrypt_action():
    ciphertext = parse_input(ciphertext_entry.get())
    key = parse_input(key_entry.get())
    if ciphertext and key:
        mode = mode_var.get()
        show_rounds = show_rounds_var.get()
        
        aes = MiniAES(key)
        
        if mode == "Single Block":
            decrypted = aes.decrypt(ciphertext, show_rounds=show_rounds)
            decrypted_var.set("Decrypted: " + format_output(decrypted))
            log_text.insert(tk.END, f"\n--- DEKRIPSI ---\nCiphertext: {format_output(ciphertext)}\nKey: {format_output(key)}\nDecrypted: {format_output(decrypted)}\n")
        
        elif mode == "ECB":
            # This is oversimplified; you'd need to handle proper byte representation for real implementation
            input_text = ciphertext_entry.get().strip().split()
            bytes_input = [int(x, 16) for x in input_text]
            blocks = aes.split_into_blocks(bytes_input)
            
            decrypted_blocks = aes.ecb_decrypt(blocks, show_rounds=show_rounds)
            flat_result = [byte for block in decrypted_blocks for byte in block]
            
            # Try to convert ASCII values back to text
            try:
                text_result = ''.join(chr(b) for b in flat_result if b >= 32 and b <= 126)
                decrypted_var.set("ECB Mode Decryption Complete")
                log_text.insert(tk.END, f"\n--- ECB DEKRIPSI ---\nHasil Teks: {text_result}\nHasil Hex: {format_output(flat_result)}\n")
            except:
                decrypted_var.set("ECB Mode Decryption Complete (Non-ASCII)")
                log_text.insert(tk.END, f"\n--- ECB DEKRIPSI ---\nHasil Hex: {format_output(flat_result)}\n")
        
        elif mode == "CBC":
            iv = parse_input(iv_entry.get())
            if not iv:
                messagebox.showinfo("Input Error", "IV dibutuhkan untuk mode CBC")
                return
                
            # This is oversimplified; you'd need to handle proper byte representation for real implementation
            input_text = ciphertext_entry.get().strip().split()
            bytes_input = [int(x, 16) for x in input_text]
            blocks = aes.split_into_blocks(bytes_input)
            
            decrypted_blocks = aes.cbc_decrypt(blocks, iv, show_rounds=show_rounds)
            flat_result = [byte for block in decrypted_blocks for byte in block]
            
            # Try to convert ASCII values back to text
            try:
                text_result = ''.join(chr(b) for b in flat_result if b >= 32 and b <= 126)
                decrypted_var.set("CBC Mode Decryption Complete")
                log_text.insert(tk.END, f"\n--- CBC DEKRIPSI ---\nIV: {format_output(iv)}\nHasil Teks: {text_result}\nHasil Hex: {format_output(flat_result)}\n")
            except:
                decrypted_var.set("CBC Mode Decryption Complete (Non-ASCII)")
                log_text.insert(tk.END, f"\n--- CBC DEKRIPSI ---\nIV: {format_output(iv)}\nHasil Hex: {format_output(flat_result)}\n")
        
        log_text.see(tk.END)

def clear_log():
    log_text.delete(1.0, tk.END)

def save_log():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt"),
                                                       ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(log_text.get(1.0, tk.END))
        messagebox.showinfo("Sukses", f"Log berhasil disimpan ke {file_path}")

def save_data():
    data = {
        "plaintext": plaintext_entry.get(),
        "key": key_entry.get(),
        "ciphertext": ciphertext_entry.get(),
        "iv": iv_entry.get(),
        "text": text_entry.get("1.0", tk.END),
        "mode": mode_var.get(),
        "show_rounds": show_rounds_var.get()
    }
    
    file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                            filetypes=[("JSON files", "*.json"),
                                                       ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            json.dump(data, file)
        messagebox.showinfo("Sukses", f"Data berhasil disimpan ke {file_path}")

def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"),
                                                     ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                
            plaintext_entry.delete(0, tk.END)
            plaintext_entry.insert(0, data.get("plaintext", ""))
            
            key_entry.delete(0, tk.END)
            key_entry.insert(0, data.get("key", ""))
            
            ciphertext_entry.delete(0, tk.END)
            ciphertext_entry.insert(0, data.get("ciphertext", ""))
            
            iv_entry.delete(0, tk.END)
            iv_entry.insert(0, data.get("iv", ""))
            
            text_entry.delete(1.0, tk.END)
            text_entry.insert(1.0, data.get("text", ""))
            
            mode_var.set(data.get("mode", "Single Block"))
            show_rounds_var.set(data.get("show_rounds", False))
            
            messagebox.showinfo("Sukses", f"Data berhasil dimuat dari {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat data: {e}")

def update_mode_gui(*args):
    mode = mode_var.get()
    
    # Hide all mode-specific frames first
    single_block_frame.grid_remove()
    block_mode_frame.grid_remove()
    
    if mode == "Single Block":
        single_block_frame.grid()
    else:  # ECB or CBC
        block_mode_frame.grid()
        
        # Show/hide IV field based on mode
        if mode == "CBC":
            iv_label.grid()
            iv_entry.grid()
        else:
            iv_label.grid_remove()
            iv_entry.grid_remove()

# GUI setup
root = tk.Tk()
root.title("Mini-AES Application")
root.geometry("700x600")

# Create a notebook with tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# Create tabs
encryption_tab = ttk.Frame(notebook)
log_tab = ttk.Frame(notebook)

notebook.add(encryption_tab, text="Encryption/Decryption")
notebook.add(log_tab, text="Log")

# --- Mode Selection ---
mode_frame = ttk.LabelFrame(encryption_tab, text="Mode Operasi")
mode_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

mode_var = tk.StringVar(value="Single Block")
mode_var.trace_add("write", update_mode_gui)

tk.Label(mode_frame, text="Mode:").grid(row=0, column=0)
mode_options = ["Single Block", "ECB", "CBC"]
mode_dropdown = ttk.Combobox(mode_frame, textvariable=mode_var, values=mode_options, state="readonly")
mode_dropdown.grid(row=0, column=1)

show_rounds_var = tk.BooleanVar(value=False)
show_rounds_cb = tk.Checkbutton(mode_frame, text="Tampilkan output tiap ronde", variable=show_rounds_var)
show_rounds_cb.grid(row=0, column=2)

# --- Single Block Mode ---
single_block_frame = ttk.LabelFrame(encryption_tab, text="Single Block Mode")
single_block_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

tk.Label(single_block_frame, text="Plaintext (hex):").grid(row=0, column=0, sticky="w")
plaintext_entry = tk.Entry(single_block_frame, width=30)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)
plaintext_entry.insert(0, "01 02 03 04")

tk.Label(single_block_frame, text="Key (hex):").grid(row=1, column=0, sticky="w")
key_entry = tk.Entry(single_block_frame, width=30)
key_entry.grid(row=1, column=1, padx=5, pady=5)
key_entry.insert(0, "0A 0B 0C 0D")

encrypt_btn = tk.Button(single_block_frame, text="Encrypt", command=encrypt_action)
encrypt_btn.grid(row=2, column=0, columnspan=2, pady=5)

result_var = tk.StringVar()
tk.Label(single_block_frame, textvariable=result_var).grid(row=3, column=0, columnspan=2)

# Decryption section in single block mode
tk.Label(single_block_frame, text="Ciphertext (hex):").grid(row=4, column=0, sticky="w")
ciphertext_entry = tk.Entry(single_block_frame, width=30)
ciphertext_entry.grid(row=4, column=1, padx=5, pady=5)

decrypt_btn = tk.Button(single_block_frame, text="Decrypt", command=decrypt_action)
decrypt_btn.grid(row=5, column=0, columnspan=2, pady=5)

decrypted_var = tk.StringVar()
tk.Label(single_block_frame, textvariable=decrypted_var).grid(row=6, column=0, columnspan=2)

# --- Block Mode Frame (ECB/CBC) ---
block_mode_frame = ttk.LabelFrame(encryption_tab, text="Block Mode")
block_mode_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

# IV (for CBC mode)
iv_label = tk.Label(block_mode_frame, text="IV (hex):")
iv_label.grid(row=0, column=0, sticky="w")
iv_entry = tk.Entry(block_mode_frame, width=30)
iv_entry.grid(row=0, column=1, padx=5, pady=5)
iv_entry.insert(0, "01 02 03 04")

# Text input for block modes
tk.Label(block_mode_frame, text="Text Input:").grid(row=1, column=0, sticky="nw")
text_entry = tk.Text(block_mode_frame, height=5, width=40)
text_entry.grid(row=1, column=1, padx=5, pady=5)

# Encrypt/Decrypt buttons for block modes
block_encrypt_btn = tk.Button(block_mode_frame, text="Encrypt", command=encrypt_action)
block_encrypt_btn.grid(row=2, column=0, padx=5, pady=5)

block_decrypt_btn = tk.Button(block_mode_frame, text="Decrypt", command=decrypt_action)
block_decrypt_btn.grid(row=2, column=1, padx=5, pady=5)

# --- File Operations Frame ---
file_frame = ttk.LabelFrame(encryption_tab, text="File Operations")
file_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

save_data_btn = tk.Button(file_frame, text="Save Data", command=save_data)
save_data_btn.grid(row=0, column=0, padx=5, pady=5)

load_data_btn = tk.Button(file_frame, text="Load Data", command=load_data)
load_data_btn.grid(row=0, column=1, padx=5, pady=5)

save_log_btn = tk.Button(file_frame, text="Save Log", command=save_log)
save_log_btn.grid(row=0, column=2, padx=5, pady=5)

# --- Log Tab ---
log_frame = ttk.Frame(log_tab)
log_frame.pack(expand=True, fill="both", padx=10, pady=10)

log_text = tk.Text(log_frame, wrap=tk.WORD)
log_text.pack(expand=True, fill="both", side=tk.LEFT)

log_scrollbar = ttk.Scrollbar(log_frame, command=log_text.yview)
log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_text.config(yscrollcommand=log_scrollbar.set)

clear_log_btn = tk.Button(log_tab, text="Clear Log", command=clear_log)
clear_log_btn.pack(pady=5)

# Initialize GUI mode
update_mode_gui()

# Hide the block mode frame initially
block_mode_frame.grid_remove()

root.mainloop()