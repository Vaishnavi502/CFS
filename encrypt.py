import os
from cryptography.fernet import Fernet
# import passkey
# import decrypt
key = Fernet.generate_key()
# Create file to store generated key ?
dirpath = "/workspaces/CFS/files"
os.chdir(dirpath)

key = Fernet(key)
for file in os.listdir():
    if file.endswith(".txt"):
        fpath = f"{dirpath}/{file}"
        with open(fpath, 'rb') as f:
            orig = f.read()
        # Encrypt file
        encrypted = key.encrypt(orig)
        # Copy file into subdirectory ./output
        op = f"{dirpath}/output/"
        if not os.path.exists(op):
            os.makedirs(op)
        opfile = f"{op}/{file}"
        with open(opfile,'wb') as f:
            f.write(encrypted)
