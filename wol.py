import socket
import struct

def wake_on_lan(mac_address):
    # Convertir l'adresse MAC en bytes
    mac_bytes = bytes.fromhex(mac_address.replace(':', ''))

    # Créer un magic packet
    magic_packet = b'\xff' * 6 + mac_bytes * 16

    # Envoyer le magic packet sur le réseau
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(magic_packet, ('<broadcast>', 9))

# Adresse MAC de l'ordinateur à allumer (ex: "00:11:22:33:44:55")
mac_address = input("Entrez l'adresse MAC de l'ordinateur à allumer: ")

wake_on_lan(mac_address)
print("Magic packet envoyé avec succès pour allumer l'ordinateur.")
