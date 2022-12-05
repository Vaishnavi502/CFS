#! /bin/bash
apt install samba smbclient
systemctl status smbd
ufw allow 'Samba'

#pip3 install cryptography
#pip3 install pycryptodome
#python -m pip install --upgrade pip
#export PATH="usr/local/python/3.10.4/bin:$PATH"