# To encrypt and decrypt file based on RSA and show output
import os
# from subprocess import call
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
dirpath = "/workspaces/CFS/files"
os.chdir(dirpath)
DEFAULT_KEY_FILE=f"{dirpath}/mykey.pem"
DEFAULT_PUB_FILE=f"{DEFAULT_KEY_FILE}.pub"
RSA_KEY_SIZE=2048

def gen_keys():
    key_file=DEFAULT_KEY_FILE
    key_pub_file=f"{dirpath}/{key_file}.pub"
    # Generate RSA key pair
    random_gen=Random.new().read
    key=RSA.generate(RSA_KEY_SIZE,random_gen)
    # Extract public key
    publickey=key.public_key()
    with open(key_file,'wb') as f:
        f.write(key.export_key('PEM'))
    with open(key_pub_file,'wb') as pubf:
        pubf.write(publickey)

def re_encrypt(f):
    # Re-encrypt encrypted file using public key
    publickey=open(DEFAULT_PUB_FILE,'rb').read()
    encryptor=PKCS1_OAEP.new(publickey)
    encrypted=encryptor.encrypt(f)
    return encrypted

def re_decrypt(encrypted):
    keypair=open(DEFAULT_KEY_FILE,'rb').read()
    decryptor=PKCS1_OAEP.new(keypair)
    decrypted=decryptor.decrypt(encrypted)
    return decrypted
