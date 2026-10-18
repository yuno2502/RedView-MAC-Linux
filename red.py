import subprocess
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

red = ".".join(ip.split(".")[:3]) + ".0/24"

print("Escaneando:", red)
print("Introduce la contraseña si te la pide.\n")

subprocess.run([
    "sudo", "nmap", "-sn", "-PR", "-PE",
    "-PS22,80,443", "-PA80,443", red])

input("\nPulsa Enter para salir...")
