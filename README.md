# udp_communication
A simple UDP client-server chat application built with Python sockets. This project demonstrates real-time bidirectional communication between two machines using the UDP protocol.
so i used only
Standard library only (no external dependencies) (sys and socket)
Socket programming (UDP protocol)

to use it you have to first run the server on your terminal
"python udp_communication.py serveur"
then you can open another terminal if it's on  the same machine you can just use the 127.0.0.1 ip address
or you can get your machine's ip address by typing "ipconfig " on you terminal
then
you run "python udp_communication.py client" on another terminal
and you can start chatting 


if you get any trouble with the port "1060"
you can run this command
# Run as Administrator
New-NetFirewallRule -DisplayName "UDP Port 1060" -Direction Inbound -Protocol UDP -LocalPort 1060 -Action Allow
so the firewall will allow the communication via this port 
