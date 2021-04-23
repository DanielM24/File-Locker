# Funcția Fernet este folosită la criptarea și decriptarea mesajului
# Fernet reprezintă o implementare a criptării simetrice
from cryptography.fernet import Fernet
import tkinter as tk

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

def user_interface():
    def cryptoTool():
        file_path = entry_widget.get()
        choice = variable.get()
        encryptor = Encryptor()
        if choice == 'encrypt':
            encryptor.encrypt_file(file_path)
            label_widget['text'] = "Fișierul dumnneavoastră a fost criptat cu succes!"
        else:
            encryptor.decrypt_file(file_path)
            label_widget['text'] = "Fișierul dumnneavoastră a fost decriptat cu succes!"

    # Realizăm interfața pentru program
    root = tk.Tk()
    root.title('File Locker Encrypt/Decrypt')
    root.minsize(width = 700, height = 400)

    app_ui = tk.Canvas(root, width = 700, height = 400)
    app_ui.pack()

    entry_widget = tk.Entry(root)
    app_ui.create_window(350, 200, window = entry_widget)

    label_widget = tk.Label()
    app_ui.create_window(350, 200, window = label_widget)

    button_widget = tk.Button(text='Submit', command=cryptoTool)
    app_ui.create_window(350, 320, window=button_widget)

    variable = tk.StringVar()
    variable.set('encrypt')

    #Adăugăm butoanele pentru opțiunea de criptare și de decriptare a fișierului
    button_encrypt = tk.Radiobutton(root, text='Encrypt File', variable = variable, value = 'encrypt')
    app_ui.create_window(350, 40, window = button_encrypt)
    button_decrypt = tk.Radiobutton(root, text='Decrypt File', variable = variable, value = 'decrypt')
    app_ui.create_window(350, 80, window = button_decrypt)

    root.mainloop()

user_interface()