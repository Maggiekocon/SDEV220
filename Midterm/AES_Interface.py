from SHA import hash_sha
from AES import encrypt_aes
import tkinter as tk
from tkinter import filedialog as fd, simpledialog as sd, messagebox as mb
import os

def browse_file():
    
    root = tk.Tk()
    root.lift() 
    root.focus_force()
    root.withdraw()
    

    # Select File
    filepath = fd.askopenfilename(
        initialdir="/",
        title="Select a file to encrypt",
        filetypes=(("All files", "*.*"), ("Text files", "*.txt"))
    )

    if not filepath:
        mb.showinfo("Failer", "File selection failed.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        message = f.read()

    # Hash File
    starthash = hash_sha(message, 256)

    # Get password
    while True:
        password = sd.askstring("Input", "Please Enter a Password :",
                                        parent=root)
        if not password:
            answer = mb.askyesno(title="Continue?", message="You must Enter a Password to continue. Would you like to continue?")
            if not answer:
                return
        else:
            break 
    # Encrypt with AES
    encrypted_message, decrypted_message = encrypt_aes(message, password)

    # Hash decryted message
    finalhash = hash_sha(decrypted_message, 256)

    # Compare first and last hash to test encryption  
    if starthash == finalhash:
        mb.showinfo("Success", "Your file was successfully encrypted")

        # Get save path.
        save_path = fd.asksaveasfilename(
            title="Choose where to save file. ",
            defaultextension=".aes",
            filetypes=[("AES Encrypted File", "*.aes"), ("All Files", "*.*")]
        )

        if not save_path:
            mb.showinfo("Failer", "File did not save.")
            return

        # Write encrypted file to given path
        with open(save_path, 'wb') as f:
            f.write(encrypted_message)
        mb.showinfo("Success", "Your file was successfully saved")

    # Check message encryption
    print(encrypted_message)
    print(decrypted_message)

if __name__ == "__main__":
    browse_file()
