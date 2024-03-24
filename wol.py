import socket
import struct
import re

# Constantes
DEFAULT_PORT = 9

def wake_on_lan(mac_address, ip_address='<broadcast>', port=DEFAULT_PORT):
    try:
        mac_bytes = bytes.fromhex(mac_address.replace(':', ''))
        magic_packet = b'\xff' * 6 + mac_bytes * 16
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.sendto(magic_packet, (ip_address, port))
        print("Magic packet envoyé avec succès pour allumer l'ordinateur.")
    except ValueError:
        print("Erreur: Adresse MAC invalide.")
    except Exception as e:
        print("Erreur lors de l'envoi du magic packet:", str(e))

def is_valid_mac(mac_address):
    # Validation de l'adresse MAC à l'aide d'une expression régulière
    return re.match('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac_address) is not None

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
        if ip_address.strip() == '':
            ip_address = '<broadcast>'
        elif not is_valid_ip(ip_address):
            print("Erreur: Adresse IP invalide.")
            ip_address = ''
        port = input(f"Entrez le port à utiliser (par défaut {DEFAULT_PORT}): ")
        if port.strip() == '':
            port = DEFAULT_PORT
        else:
            try:
                port = int(port)
                if port < 0 or port > 65535:
                    raise ValueError("Port en dehors de la plage autorisée.")
            except ValueError:
                print("Erreur: Port invalide, utilisant le port par défaut.")
                port = DEFAULT_PORT

        wake_on_lan(mac_address, ip_address, port)
