import socket
import concurrent.futures
import argparse

parser = argparse.ArgumentParser(description="Escáner de Puertos Táctico")
parser.add_argument("-i", "--ip", required=True, help="Dirección IP objetivo")
parser.add_argument("-p", "--puertos", type=int, default=100, help="Límite máximo de puertos")

args = parser.parse_args()
objetivo = args.ip
limite_puertos = args.puertos

def escanear_puerto(puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1.0)
    
    resultado = s.connect_ex((objetivo, puerto))
    if resultado == 0:
        try:
            # Si conecta, intentamos recibir datos (Banner Grabbing)
            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            if banner:
                print(f"[*] Puerto {puerto} ABIERTO - Banner: {banner}")
            else:
                print(f"[*] Puerto {puerto} ABIERTO - (Sin banner visible)")
        except:
            # Si el puerto no envía datos y da timeout, igual reportamos que está abierto
            print(f"[*] Puerto {puerto} ABIERTO")
            
    s.close()

print(f"Iniciando escaneo con Banner Grabbing en {objetivo} (Puertos 1 al {limite_puertos})...")

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as ejecutor:
    ejecutor.map(escanear_puerto, range(1, limite_puertos + 1))

print("Escaneo finalizado.")

