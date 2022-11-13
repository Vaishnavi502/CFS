#! /bin/bash
apt install samba smbclient
systemctl status smbd
ufw allow 'Samba'

#pip3 install cryptography
#python -m pip install --upgrade pip
#export PATH="usr/local/python/3.10.4/bin:$PATH"