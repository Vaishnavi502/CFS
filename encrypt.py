import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
# Create file to store generated key ?
dpath = "./files"
os.chdir(dpath)

key = Fernet(key)
for file in os.listdir():
    if file.endswith(".txt"):
        fpath = f"{dpath}/{file}"
        with open(fpath, 'rb') as f:
            orig = f.read()
        # Encrypt file
        encrypted = key.encrypt(orig)
        # Copy file into subdirectory ./output
        op = f"{dpath}/output"
        with open(op,'wb') as f:
            f.write(encrypted)
