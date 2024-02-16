import socket
import struct

def wake_on_lan(mac_address, ip_address='<broadcast>', port=9):
    try:
        # Convertir l'adresse MAC en bytes
        mac_bytes = bytes.fromhex(mac_address.replace(':', ''))

        # Créer un magic packet
        magic_packet = b'\xff' * 6 + mac_bytes * 16

        # Envoyer le magic packet sur le réseau
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.sendto(magic_packet, (ip_address, port))
        print("Magic packet envoyé avec succès pour allumer l'ordinateur.")
    except ValueError:
        print("Erreur: Adresse MAC invalide.")
    except Exception as e:
        print("Erreur lors de l'envoi du magic packet:", str(e))

# Fonction pour valider une adresse MAC
def is_valid_mac(mac_address):
    if len(mac_address) == 17:
        parts = mac_address.split(':')
        if len(parts) == 6:
            try:
                int(parts[0], 16)
                int(parts[1], 16)
                int(parts[2], 16)
                int(parts[3], 16)
                int(parts[4], 16)
                int(parts[5], 16)
                return True
            except ValueError:
                pass
    return False

# Fonction pour valider une adresse IP
def is_valid_ip(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False

if __name__ == "__main__":
    mac_address = input("Entrez l'adresse MAC de l'ordinateur à allumer: ")
    if not is_valid_mac(mac_address):
        print("Erreur: Adresse MAC invalide.")
    else:
        ip_address = input("Entrez l'adresse IP ou appuyez sur Entrée pour utiliser la diffusion: ")
        if ip_address and not is_valid_ip(ip_address):
            print("Erreur: Adresse IP invalide.")
        else:
            port = input("Entrez le port à utiliser (par défaut 9): ")
            if port:
                try:
                    port = int(port)
                except ValueError:
                    print("Erreur: Port invalide, utilisant le port par défaut 9.")
                    port = 9
            else:
                port = 9

            wake_on_lan(mac_address, ip_address, port)
