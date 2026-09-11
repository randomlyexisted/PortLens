import socket
import threading
import argparse
import json
import csv

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

results = []
lock = threading.Lock()

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = {
        "port": port,
        "state": "",
        "service": ""
    }

    try:
        sock.connect((target,port))

        result["state"] = "OPEN"

        if port in services:
            result["service"] = services[port] 
        else:
            result["service"] ="Unknown"
    except socket.timeout:
        result["state"] = "FILTERED / TIMEOUT"
        result["service"] = ""
    except ConnectionRefusedError:
        result["state"] = "CLOSED"
        result["service"] = str(e)
    except OSError as e:
        result["state"] = "ERROR"
        result["service"] = str(e)
    finally:
        sock.close()

    with lock:
        results.append(result)

def save_json(filename):
    with open(filename, "w") as file:
        json.dump(results,file,indent=4)

def save_csv(filename):
    with open(filename, "w", newline="")as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["port","state","service"]
        )
        writer.writeheader()
        writer.writerows(results)

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

parser.add_argument(
    "--json",
    help="Save results as a JSON file"
)

parser.add_argument(
    "--csv",
    help="Save results as a CSV file"
)


args = parser.parse_args()

try:
    target = socket.gethostbyname(args.target)
    print(f"Resolved {args.target} → {target}")
except:
    print(f"Could not resolve target: {args.target}")
    exit()

s_port = args.start_port
e_port = args.end_port

threads = []

for port in range(s_port, e_port+1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

results.sort(key=lambda x: x["port"])
    
for result in results:
    if result["service"]:
        print(f"Port {result['port']} is "
              f"{result['state']} → {result['service']}"
            )
    else:
        print(
            f"Port {result['port']} is "
            f"{result['state']}"
        )

if args.json:
    save_json(args.json)
    print(f"\nResults save to {args.json}")

if args.csv:
    save_csv(args.csv)
    print(f"Result saved to {args.csv}")
