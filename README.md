# CFS
Cryptographic File System in Linux using Python
Project to encrypt and decrypt directories in a shared folder (main environment: Ubuntu)
Steps:
1. Create a shared directory in ubuntu using samba (can also connect Windows)
2. Create a subdirectory with files that have sensitive information ("./files")
3. In main shared folder, create a python script to encrypt all files within ./files
4. Server - run encryption and make all files in ./files as encrypted
5. Client - tries to access ./files and will need to provide pass key
6. If pass key matches, server decrypts entire directory

-> entire directory is encrypted with symmetric encryption
-> clients know public key (RSA)

Packages: cryptography (Fernet), os
