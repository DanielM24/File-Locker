## File-Locker

File-Locker is a tool for Encryption and Decryption made in Python. The project follows symmetric encryption which means it uses  the same key to encrypt and decrypt the files. It is able to encrypt any type of file. The key used in encryption is included in the encrypted file.

#### How it looks:

<img src="C:\Users\danie\Desktop\Github\demo.png" alt="k" style="zoom: 67%;" />

 

[^]: This is how the app looks

<img src="C:\Users\danie\Desktop\Github\encrypt_message.png" style="zoom:67%;" />

 

[^]: When you successfully encrypted a file you will receive this message

<img src="C:\Users\danie\Desktop\Github\decrypt_message.png" style="zoom:67%;" />

[^]: When you successfully decrypted a file you will receive this message





#### **Fernet**

Fernet is built on top of a number of standard cryptographic primitives. Specifically, it uses:

- ​	 [**AES**](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.algorithms.AES) in [**CBC**](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.modes.CBC) mode with a 128-bit key for encryption; using [**PKCS7**](https://cryptography.io/en/latest/hazmat/primitives/padding/#cryptography.hazmat.primitives.padding.PKCS7) padding.
- ​	 [**HMAC**](https://cryptography.io/en/latest/hazmat/primitives/mac/hmac/#cryptography.hazmat.primitives.hmac.HMAC) using [**SHA256**](https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/#cryptography.hazmat.primitives.hashes.SHA256) for authentication.
- ​	 Initialization vectors are generated using os.urandom().

For complete details consult the [specification](https://github.com/fernet/spec/blob/master/Spec.md).

#### **Limitations**

​	Fernet is ideal for encrypting data that easily fits in memory. As a design feature, it does not expose unauthenticated bytes. This means that the complete message contents must be available in memory, making Fernet generally unsuitable for very large files at this time.

#### **Dependencies**:

- [x] Python v.3 is required
- [x] Tkinter module is required 
- [x] Pillow module is required