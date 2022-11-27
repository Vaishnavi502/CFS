import os
from cryptography.fernet import Fernet
# import passkey
# import decrypt
key = Fernet.generate_key()
# Create file to store generated key ?
dpath = "/workspaces/CFS/files"
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
        op = f"{dpath}/output/{file}"
        if not os.path.exists(op):
                os.makedirs(op)
        with open(op,'wb') as f:
            f.write(encrypted)
