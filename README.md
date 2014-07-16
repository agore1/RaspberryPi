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

###Remote Desktop

* On the Pi:  
  * Install [TightVNC](http://www.tightvnc.com/)
  * Start a vnc server with "vncserver -geometry 1920x1080"

* On the remote computer:
  * In Ubuntu, start the Remmina Remote Desktop Client
  * Create a new remote desktop file, Protocol: "VNC - Virtual Network Computing"  
    Password: the shortened password of the pi (8 chars?), Server: "10.42.0.2:5901"  
    (for a directly networked Pi with 10.42.0.2 as the IP addr and default vncserver port).
