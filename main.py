# Funcția Fernet este folosită la criptarea și decriptarea mesajului
# Fernet reprezintă o implementare a criptării simetrice
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class Encryptor():

    # Funcția de generare a cheii (aceasta este de 44 de caractere)
    def generate_key(self):
        key = Fernet.generate_key()
        return key

    # Funcția salvează cheia în interiorul fișierului criptat
    def save_key(self, file_name, key):
        with open(file_name, 'ab') as  file:
            file.write(key)
        file.close()

    # După ce am generat cheia, aceasta trebuie citită pentru a realiza decriptarea fișierelor
    def load_key(self, file_name):
        # Extragem cheia din fișierul criptat
        with open(file_name, 'rb') as file:
            content = file.read()
            key = content[-44:]
            content = content[:-44]
        file.close()

        # Ștergem cheia din fișierul criptat pentru a nu întâmpina probleme la decriptare
        with open(file_name, 'wb') as file:
            file.write(content)
        file.close()

        return key

    # Funcția de criptare a unui fișier
    def encrypt_file(self, file_name):
        # Generăm cheia pentru criptarea fișierului
        key = self.generate_key()
        function = Fernet(key)
        with open(file_name, 'rb') as original_file:
            content = original_file.read()
        original_file.close()

        coded_content = function.encrypt(content)
        with open(file_name, 'wb') as encrypt_file:
            encrypt_file.write(coded_content)
        encrypt_file.close()
        self.save_key(file_name, key)

    # Funcția de decriptare a fișierului
    def decrypt_file(self, file_name):
        # Extragem cheia pentru decriptarea fișierului
        key = self.load_key(file_name)
        function = Fernet(key)

        with open(file_name, 'rb') as encrypt_file:
            coded_content = encrypt_file.read()
        encrypt_file.close()
        content = function.decrypt(coded_content)

        with open(file_name, 'wb') as original_file:
            original_file.write(content)
        original_file.close()


file = ' '

root = tk.Tk()
root.title('File Locker Encrypt/Decrypt')
root.geometry('+%d+%d'%(350,100))

canvas = tk.Canvas(root, width=700, height=450, bg="white")
canvas.grid(columnspan=3, rowspan=5)

def cryptoTool(choice):
    encryptor = Encryptor()
    if choice == 'encrypt':
        try:
            encryptor.encrypt_file(file)
            text_box = tk.Text(root, height=2, width=40, padx=15, pady=15)
            text_box.insert(1.0, "Fișierul dumnneavoastră a fost criptat  cu succes!")
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=3)
        except Exception:
            text_box = tk.Text(root, height=2, width=40, padx=15, pady=15)
            text_box.insert(1.0, "Eroare! Fișierul dumnneavoastră nu a    putut fi criptat.")
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=3)

    else:
        try:
            encryptor.decrypt_file(file)
            text_box = tk.Text(root, height=2, width=40, padx=15, pady=15)
            text_box.insert(1.0, "Fișierul dumnneavoastră a fost decriptat cu succes!")
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=3)
        except Exception:
            text_box = tk.Text(root, height=2, width=40, padx=15, pady=15)
            text_box.insert(1.0, "Eroare! Fișierul dumnneavoastră nu a    putut fi decriptat.")
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=3)

def select_file():
    browse_text.set("Loading...")
    global file
    file = filedialog.askopenfilename(parent = root, filetypes=[("All files","*.*")])
    browse_text.set("Browse")

# Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo, bg="white")
logo_label.image = logo
logo_label.grid(column = 1, row = 0,sticky='N')

# Instrucțiuni
instructions = tk.Label(root, text="Select a file from your computer to Encrypt/Decrypt", font=("Times New Roman", 12), bg="white")
instructions.grid(columnspan = 3, column = 0, row = 0,sticky='S',pady=15)

# Browse
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable = browse_text, command = lambda:select_file(), font=("Times New Roman", 13), bg = "#0c334c", fg = "white", height = 2, width = 10 )
browse_text.set("Browse")
browse_btn.grid(column = 1, row = 1,sticky='N',padx=50)

# Salvăm opțiunea utilizatorului: Criptează fișierul / Decriptează fișierul
option = tk.StringVar()

# Adăugăm butoanele pentru opțiunea de criptare și de decriptare a fișierului
encrypt_text = tk.StringVar()
button_encrypt = tk.Button(root, textvariable = encrypt_text, command = lambda:cryptoTool('encrypt'), font=("Times New Roman", 13), bg = "#0c334c", fg = "white", height = 2, width = 15 )
encrypt_text.set("Encrypt File")
button_encrypt.grid(column = 0, row = 2)

decrypt_text = tk.StringVar()
button_decrypt = tk.Button(root, textvariable = decrypt_text, command = lambda:cryptoTool('decrypt'), font=("Times New Roman", 13), bg = "#0c334c", fg = "white", height = 2, width = 15 )
decrypt_text.set("Decrypt File")
button_decrypt.grid(column = 2, row = 2)

root.mainloop()
