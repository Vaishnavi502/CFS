import encrypt,encrypt2
import os

dirpath = "/workspaces/CFS/files"
os.chdir(dirpath)

dkey=encrypt.genkey()

for file in os.listdir():
    if file.endswith(".txt"):
        dpath=f'{dirpath}/output/{file}'
        with open(dpath,'rb') as f:
            encrypted=f.read()
        print(f'\nContent of {file} is:')
        decrypted2=encrypt2.re_decrypt(encrypted)
        decrypted=dkey.decrypt(decrypted2)
        st=decrypted.decode('utf8')
        print(st)
