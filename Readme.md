# PortLens 🔍

A simple multithreaded TCP port scanner written in Python, built as a cybersecurity learning project.

PortLens started as a basic TCP port scanner and is being developed version-by-version to understand how network scanning tools work internally.

> **Current Version: v0.9.0 — Banner Grabbing**

---

## 🚀 Features

PortLens currently supports:

* 🎯 Scan a specific target
* 🔢 Scan a range of TCP ports
* 🔎 Basic service identification based on port numbers
* ⚡ Multithreaded scanning
* ⏱️ Connection timeouts
* 🛡️ Basic socket error handling
* 💻 Command-line interface
* 🌐 DNS/domain name resolution
* 📄 JSON output
* 📊 CSV output
* 🏴 Banner grabbing
* 🔐 SSH banner detection
* 🌐 HTTP response/header grabbing

---

## 📌 Current Version

### v0.9.0 — Banner Grabbing

PortLens can now attempt to retrieve application-level information from open ports.

For example, an SSH server may return:

```text
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
```

An HTTP server may return:

```text
HTTP/1.1 200 OK
Server: Apache/2.4.7 (Ubuntu)
Content-Type: text/html
```

PortLens stores the retrieved banner along with the port state and service information.

---

## 🛠️ Requirements

* Python 3.x
* No external Python packages required

PortLens uses Python's built-in modules:

```text
socket
threading
argparse
json
csv
```

---

## 📥 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Enter the project directory:

```bash
cd Portlens
```

Run the scanner:

```bash
python scanner.py
```

---

## 💻 Usage

### Basic scan

```bash
python scanner.py -t 127.0.0.1 -s 1 -e 100
```

Where:

| Argument             | Description                      |
| -------------------- | -------------------------------- |
| `-t`, `--target`     | Target IP address or domain name |
| `-s`, `--start-port` | Starting port                    |
| `-e`, `--end-port`   | Ending port                      |
| `--json`             | Save results to a JSON file      |
| `--csv`              | Save results to a CSV file       |

---

## 🌐 Scanning a Domain

PortLens can resolve domain names before scanning.

Example:

```bash
python scanner.py -t scanme.nmap.org -s 20 -e 100
```

Output begins with:

```text
Resolved scanme.nmap.org → 45.33.32.156
```

The scanner then performs the TCP scan against the resolved IP address.

---

## 🏴 Banner Grabbing

Starting with **v0.9.0**, PortLens attempts to retrieve a banner from open ports.

The scanner first establishes a TCP connection:

```text
TCP Connection
      ↓
Port OPEN
      ↓
Attempt Banner Grab
      ↓
Receive Application Data
      ↓
Decode Banner
```

### SSH

SSH servers commonly send their identification string immediately after a connection.

Example:

```text
Port 22 is OPEN → SSH
Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
```

### HTTP

HTTP servers generally expect a request before sending a response.

PortLens sends a simple HTTP request:

```text
HEAD / HTTP/1.0
Host: localhost
```

The server may respond with information such as:

```text
HTTP/1.1 200 OK
Date: ...
Server: Apache/2.4.7 (Ubuntu)
Accept-Ranges: bytes
Vary: Accept-Encoding
Connection: close
Content-Type: text/html
```

### No Banner

An open port may not provide any banner.

In that case:

```text
Port 1234 is OPEN → Unknown
Banner: No banner
```

This does **not** mean that the port is closed.

Some services simply do not send information immediately, require a protocol-specific request, or intentionally hide their service information.

---

## 🔎 Service Identification

PortLens currently uses a simple port-number mapping:

| Port | Service                     |
| ---: | --------------------------- |
|   21 | FTP                         |
|   22 | SSH                         |
|   23 | Telnet                      |
|   25 | SMTP                        |
|   53 | DNS                         |
|   80 | HTTP                        |
|  110 | POP3                        |
|  143 | IMAP                        |
|  443 | HTTPS                       |
| 3306 | MySQL                       |
| 5432 | PostgreSQL                  |
| 8080 | HTTP Proxy / Alternate HTTP |

If an open port is not present in the mapping, PortLens reports:

```text
Unknown
```

> **Note:** This is port-based service identification, not full protocol detection. A service can technically run on a non-standard port.

---

## 📊 Port States

PortLens currently reports three main scan states.

### OPEN

The TCP connection was successfully established.

```text
Port 22 is OPEN → SSH
```

### CLOSED

The target actively refused the TCP connection.

```text
Port 25 is CLOSED
```

### FILTERED / TIMEOUT

The scanner did not receive a response before the timeout.

```text
Port 53 is FILTERED / TIMEOUT
```

A timeout does **not necessarily mean the port is closed**. A firewall or network filter may simply be dropping packets.

---

## ⚡ Multithreading

PortLens uses Python's `threading` module to scan multiple ports concurrently.

Instead of:

```text
Port 1 → Scan
Port 2 → Scan
Port 3 → Scan
Port 4 → Scan
```

PortLens creates threads:

```text
             ┌─ Port 1
             ├─ Port 2
Scanner ─────┼─ Port 3
             ├─ Port 4
             └─ Port 5
```

This makes scanning a range of ports considerably faster than scanning each port sequentially.

A `threading.Lock()` is also used when adding scan results to the shared results list.

---

## ⏱️ Timeout Handling

Each socket uses a one-second timeout:

```python
sock.settimeout(1)
```

This prevents the scanner from waiting indefinitely for a response.

Timeouts are handled separately:

```python
except socket.timeout:
    result["state"] = "FILTERED / TIMEOUT"
```

---

## 📄 JSON Output

Results can be saved as JSON:

```bash
python scanner.py -t 127.0.0.1 -s 20 -e 100 --json results.json
```

Example:

```json
[
    {
        "port": 22,
        "state": "OPEN",
        "service": "SSH",
        "banner": "SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13"
    },
    {
        "port": 80,
        "state": "OPEN",
        "service": "HTTP",
        "banner": "HTTP/1.1 200 OK\r\n..."
    }
]
```

---

## 📊 CSV Output

Results can also be saved as CSV:

```bash
python scanner.py -t 127.0.0.1 -s 20 -e 100 --csv results.csv
```

The CSV contains:

```text
port,state,service,banner
```

Example:

```text
22,OPEN,SSH,SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
80,OPEN,HTTP,HTTP/1.1 200 OK...
```

Both formats can be generated at the same time:

```bash
python scanner.py -t 127.0.0.1 -s 20 -e 100 --json results.json --csv results.csv
```

---

## 🧠 How PortLens Works

The overall workflow is:

```text
                ┌──────────────────┐
                │   Command Line   │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ Resolve Target   │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │  Create Threads  │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │   TCP Connect    │
                └────────┬─────────┘
                         ↓
              ┌──────────┴──────────┐
              ↓                     ↓
           Success                Timeout
              ↓                     ↓
            OPEN             FILTERED/TIMEOUT
              ↓
       ┌──────┴──────┐
       ↓             ↓
  Identify       Grab Banner
   Service            ↓
       └──────┬──────┘
              ↓
        Store Result
              ↓
       Wait for Threads
              ↓
         Sort Results
              ↓
        Display Results
              ↓
       JSON / CSV Output
```

---

## 📁 Project Structure

```text
Portlens/
│
├── scanner.py
├── README.md
└── ...
```

---

## 🧪 Example Scan

Command:

```bash
python scanner.py -t scanme.nmap.org -s 20 -e 100
```

Example output:

```text
Resolved scanme.nmap.org → 45.33.32.156

Port 20 is FILTERED / TIMEOUT
Port 21 is FILTERED / TIMEOUT

Port 22 is OPEN → SSH
Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13

Port 23 is FILTERED / TIMEOUT
...
Port 80 is OPEN → HTTP
Banner: HTTP/1.1 200 OK
Date: ...
Server: Apache/2.4.7 (Ubuntu)
Accept-Ranges: bytes
Vary: Accept-Encoding
Connection: close
Content-Type: text/html

Port 81 is FILTERED / TIMEOUT
...
Port 100 is FILTERED / TIMEOUT
```


## 🎯 Learning Goals

This project is primarily being developed to understand cybersecurity and networking concepts through implementation.

Key concepts explored:

* TCP/IP networking
* TCP connections
* Ports and services
* Socket programming
* DNS resolution
* Multithreading
* Thread synchronization
* Network timeouts
* Exception handling
* Protocol-level communication
* Banner grabbing
* HTTP requests
* SSH identification
* CLI application development
* JSON and CSV data handling
* Git and version-controlled development

---

## ⚠️ Limitations

PortLens is a **learning project**, not a replacement for professional network scanning tools.

Current limitations include:

* TCP connect scanning only
* Basic port-number-based service identification
* Limited protocol-specific banner grabbing
* Only a simple HTTP probe is currently implemented
* Some services may not return banners
* Timeouts can represent filtering rather than a definitively filtered port
* No UDP scanning
* No stealth/SYN scanning
* No advanced service/version detection
* No operating-system detection

These limitations are intentional because the project is being developed incrementally to understand the underlying concepts.

---

## ⚖️ Legal & Ethical Use

Only scan systems that you own or have explicit permission to test.

Publicly accessible systems are **not automatically authorized targets**.

Port scanning systems without permission may violate laws, policies, or terms of service.

This project is intended for:

* Personal labs
* CTF environments
* Cybersecurity training
* Authorized penetration testing
* Systems you own or have permission to scan

---

## 👨‍💻 Project Status

**PortLens v0.9.0**

The project is currently in active development.

The next milestone is:

```text
v1.0.0 — Stable Release + Tests + Documentation
```

The goal of v1.0.0 is to turn the current learning implementation into a cleaner, tested, and documented stable release.
