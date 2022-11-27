# To encrypt and decrypt file based on RSA and show output
import os
# from subprocess import call
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
dirpath = f"{os.getcwd()}"
os.chdir(dirpath)
DEFAULT_KEY_FILE=f"{dirpath}/mykey.pem"
DEFAULT_PUB_FILE=f"{dirpath}/mykey.pem.pub"
RSA_KEY_SIZE=4096

def gen_keys():
    key_file=DEFAULT_KEY_FILE
    key_pub_file=DEFAULT_PUB_FILE
    # Generate RSA key pair
    random_gen=Random.new().read
    key=RSA.generate(RSA_KEY_SIZE,random_gen)
    # Extract public key
    pk=key.publickey()
    with open(key_file,'wb') as f:
        f.write(key.exportKey('PEM'))
    with open(key_pub_file,'wb') as pubf:
        pubf.write(pk.exportKey())

def re_encrypt(f):
    # Re-encrypt encrypted file using public key
    pk=RSA.importKey(open(DEFAULT_PUB_FILE,'rb').read())
    encryptor=PKCS1_OAEP.new(pk)
    encrypted=encryptor.encrypt(bytes(f))
    return encrypted

def re_decrypt(encrypted):
    keypair=RSA.importKey(open(DEFAULT_KEY_FILE,'rb').read())
    decryptor=PKCS1_OAEP.new(keypair)
    decrypted=decryptor.decrypt(encrypted)
    return decrypted
