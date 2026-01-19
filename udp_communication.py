import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535
PORT = 1060

if sys.argv[1:] == ['serveur']:
    s.bind(("0.0.0.0", PORT))
    print("---serveur prét---")
    print("listening", s.getsockname())
    print("en attent la connection du client")
    ad_client = None
    while True:
        data, address = s.recvfrom(MAX)
        message = data.decode()
        
        if ad_client == None:
            ad_client = address
            print("le client est connecté depuis {}".format(address))
        if message.lower() == "quit":
            s.sendto("bye!!".encode(), address)
            ad_client = None
            print("en attent pour le client suivant")
            continue
        
        print("client: {}".format(message))
        reply = input("serveur: ")
        s.sendto(reply.encode(), address)
        
        if reply.lower() == "quit":
            print("le serveur a deconnecté")
            ad_client = None
            print("en attent pour le client suivant")

elif sys.argv[1:] == ['client']:
    serveur_ip = input("donné l'address ip du serveur (par defaut 127.0.0.1 local) : ")
    if not serveur_ip:
        serveur_ip = '127.0.0.1'
    print("---client prét---")
    print("connection au serveur {}, {}".format(serveur_ip, PORT))
    print("tapez 'quit' pour quittez")
    
    while True:
        message = input("client: ")
        s.sendto(message.encode(), (serveur_ip, PORT))
        
        if message.lower() == 'quit':
            data, address = s.recvfrom(MAX)
            print(data.decode())
            print("deconnection du serveur")
            break
        
        data, address = s.recvfrom(MAX)
        reponse = data.decode()
        print("serveur: {}".format(reponse))
        
        if reponse.lower() == 'quit':
            print("serveur a fermé la connection")
            break
    
    s.close()

else:
    print("erreur python udp_communication.py serveur|client", file=sys.stderr)
    sys.exit(1)