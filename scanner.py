import socket

target = input("Enter target IP:")
s_port = int(input("Enter starting port: "))
e_port = int(input("Enter ending port: "))



for port in range(s_port, e_port+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((target,port))
        print(f"Port {port} is OPEN")
    except:
        print(f"Port {port} is CLOSED")
    finally:
        sock.close()
