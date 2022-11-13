#! /bin/bash
apt install samba smbclient
systemctl status smbd
ufw allow 'Samba'
