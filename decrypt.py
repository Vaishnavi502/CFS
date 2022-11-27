import encrypt

dkey,dpath=encrypt.genkey()

with open(dpath,'rb') as f:
    encrypted=f.read()

decrypted=dkey.decrypt(encrypted)
print(decrypted.decode('utf8'))
