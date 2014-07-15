A Collection of Tips for Raspberry Pi Projects
===========

###Direct Networking

* On the Pi
 * Edit the /etc/network/interfaces file
 * Edit cmdline.txt in the boot section of the SD card

* On the host computer 
 * In the connections manager, make a new ethernet connection called _Direct Connection_
 * Select "Shared to other computers"
 * Select that connection when you plug in the Pi
 * Plug, maybe replug the ethernet cable before starting ssh 
