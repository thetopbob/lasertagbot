NAME := lasertagbot

.PHONY: install
install:
	sudo apt-get install python3 python3-pip
	sudo pip install -r requirements.txt
	cp remote/BN59-00516A.conf /etc/lirc/lircd.conf
