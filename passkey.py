# To check if client has entered correct pass key
import os
from subprocess import call
DEFAULT_KEY_FILE="./mykey.pem"
RSA_KEY_SIZE=2048

def gen_keys():
    key_file=DEFAULT_KEY_FILE
    key_pub_file=f"{key_file}.pub"
    # Generate RSA key pair
    call(['openssl','genrsa','-out',key_file,str(RSA_KEY_SIZE)])
    # Extract public key
    with open(key_pub_file,'w') as stdout:
        call(['openssl','rsa','-in',key_file,'-pubout'],stdout=stdout)
    # Broadcast RSA public key
    with open(key_pub_file,'r') as fin:
        print(fin.read())
pwd = "S_V$035"
def check():
    pkey=input(str("Enter password: "))
    if(pwd == pkey):
        return 1
    return 0
