import tkinter as tk
from tkinter import messagebox

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher Tool")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Configure styles
        self.root.configure(bg="#f0f0f0")
        title_font = ("Helvetica", 16, "bold")
        label_font = ("Helvetica", 10)
        button_font = ("Helvetica", 10, "bold")
        
        # Title
        tk.Label(
            self.root, 
            text="Caesar Cipher Encryption/Decryption", 
            font=title_font, 
            bg="#f0f0f0"
        ).pack(pady=10)
        
        # Message Input
        tk.Label(
            self.root, 
            text="Enter your message:", 
            font=label_font, 
            bg="#f0f0f0"
        ).pack(anchor="w", padx=20)
        
        self.message_entry = tk.Text(
            self.root, 
            height=5, 
            width=50, 
            font=label_font, 
            wrap="word"
        )
        self.message_entry.pack(padx=20, pady=5)
        
        # Shift Value
        tk.Label(
            self.root, 
            text="Enter shift value (1-25):", 
            font=label_font, 
            bg="#f0f0f0"
        ).pack(anchor="w", padx=20)
        
        self.shift_entry = tk.Entry(
            self.root, 
            width=10, 
            font=label_font, 
            justify="center"
        )
        self.shift_entry.pack(anchor="w", padx=20, pady=5)
        
        # Buttons Frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        self.encrypt_button = tk.Button(
            button_frame, 
            text="Encrypt", 
            font=button_font, 
            bg="#4CAF50", 
            fg="white", 
            command=self.encrypt
        )
        self.encrypt_button.pack(side="left", padx=10)
        
        self.decrypt_button = tk.Button(
            button_frame, 
            text="Decrypt", 
            font=button_font, 
            bg="#2196F3", 
            fg="white", 
            command=self.decrypt
        )
        self.decrypt_button.pack(side="left", padx=10)
        
        self.clear_button = tk.Button(
            button_frame, 
            text="Clear", 
            font=button_font, 
            bg="#f44336", 
            fg="white", 
            command=self.clear
        )
        self.clear_button.pack(side="left", padx=10)
        
        # Result
        tk.Label(
            self.root, 
            text="Result:", 
            font=label_font, 
            bg="#f0f0f0"
        ).pack(anchor="w", padx=20)
        
        self.result_text = tk.Text(
            self.root, 
            height=5, 
            width=50, 
            font=label_font, 
            wrap="word", 
            state="disabled"
        )
        self.result_text.pack(padx=20, pady=5)
        
    def encrypt(self):
        message = self.message_entry.get("1.0", "end-1c")
        shift = self.shift_entry.get()
        
        if not message:
            messagebox.showwarning("Warning", "Please enter a message to encrypt!")
            return
            
        if not shift.isdigit() or int(shift) < 1 or int(shift) > 25:
            messagebox.showwarning("Warning", "Shift value must be an integer between 1 and 25!")
            return
            
        shift = int(shift)
        encrypted_message = self.caesar_cipher(message, shift)
        self.display_result(encrypted_message)
        
    def decrypt(self):
        message = self.message_entry.get("1.0", "end-1c")
        shift = self.shift_entry.get()
        
        if not message:
            messagebox.showwarning("Warning", "Please enter a message to decrypt!")
            return
            
        if not shift.isdigit() or int(shift) < 1 or int(shift) > 25:
            messagebox.showwarning("Warning", "Shift value must be an integer between 1 and 25!")
            return
            
        shift = -int(shift)  # Decryption is just encryption with negative shift
        decrypted_message = self.caesar_cipher(message, shift)
        self.display_result(decrypted_message)
        
    def caesar_cipher(self, text, shift):
        result = ""
        
        for char in text:
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += char
                
        return result
        
    def display_result(self, text):
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", text)
        self.result_text.config(state="disabled")
        
    def clear(self):
        self.message_entry.delete("1.0", "end")
        self.shift_entry.delete(0, "end")
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
