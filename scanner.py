import socket

target = input("Enter target IP:")
port = int(input("Enter port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((target,port))
    print(f"Port {port} is OPEN")
except:
    print(f"Port {port} is CLOSED")
finally:
    sock.close()