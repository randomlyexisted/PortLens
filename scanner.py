import socket

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP Proxy / Alternate HTTP"
}

target = input("Enter target IP:")
s_port = int(input("Enter starting port: "))
e_port = int(input("Enter ending port: "))



for port in range(s_port, e_port+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((target,port))
        if port in services:
            print(f"Port {port} is OPEN - {services[port]}")
        else:
            print(f"Port {port} is OPEN - Unknown service")
    except:
        print(f"Port {port} is CLOSED")
    finally:
        sock.close()
