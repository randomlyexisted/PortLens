import socket
import threading
import argparse


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

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect((target,port))

        if port in services:
            print(f"Port {port} is OPEN - {services[port]}")
        else:
            print(f"Port {port} is OPEN - Unknown service")
    except socket.timeout:
        print(f"Port {port} is FILTERED / TIMEOUT")
    except ConnectionRefusedError:
        print(f"Port {port} is CLOSED");
    except OSError as e:
        print(f"Port {port} ERROR: {e}")
    finally:
        sock.close()


parser = argparse.ArgumentParser(description="PortLens - A simple TCP port scanner")

parser.add_argument(
    "-t",
    "--target",
    required=True,
    help="Target IP address"
)

parser.add_argument(
    "-s",
    "--start-port",
    type=int,
    required=True,
    help="Starting port"
)

parser.add_argument(
    "-e",
    "--end-port",
    type=int,
    required=True,
    help="Ending port"
)

args = parser.parse_args()

target = args.target
s_port = args.start_port
e_port = args.end_port

threads = []

for port in range(s_port, e_port+1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
