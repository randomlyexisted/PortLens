# PortLens

A simple Python-based TCP port scanner built as a cybersecurity learning project.

## Current Version

**v0.7.0 — DNS Resolution**

## Features

* Scan a target using an IPv4 address
* Scan a target using a domain name
* Resolve domain names to IPv4 addresses using DNS
* Scan a range of TCP ports
* Identify open and closed ports
* Detect connection timeouts
* Display `FILTERED / TIMEOUT` when a connection attempt receives no response within the timeout period
* Identify common services based on port numbers
* Scan multiple ports concurrently using multithreading
* Handle common socket errors
* Command-line interface using Python's `argparse`
* Support both short and long command-line options

## Usage

PortLens accepts either an IPv4 address or a domain name as the target.

### Scan an IP Address

```bash
python scanner.py -t 127.0.0.1 -s 1 -e 100
```

### Scan a Domain Name

```bash
python scanner.py -t scanme.nmap.org -s 1 -e 100
```

Before scanning, PortLens resolves the domain to an IPv4 address:

```text
Resolved scanme.nmap.org → <IP address>
```

The resolved address is then used for TCP port scanning.

## Command-Line Arguments

| Argument | Long Form      | Description                        |
| -------- | -------------- | ---------------------------------- |
| `-t`     | `--target`     | Target IPv4 address or domain name |
| `-s`     | `--start-port` | Starting port                      |
| `-e`     | `--end-port`   | Ending port                        |
| `-h`     | `--help`       | Display help information           |

All three scanning arguments are required.

## Help

To view the available options:

```bash
python scanner.py --help
```

## Example Output

```text
Resolved scanme.nmap.org → <IP address>

Port 22 is OPEN → SSH
Port 80 is OPEN → HTTP
Port 23 is CLOSED
Port 25 is FILTERED / TIMEOUT
```

> The order of results may vary because multiple ports are scanned concurrently.

## Port States

PortLens distinguishes between different TCP connection results:

| Result               | Meaning                                           |
| -------------------- | ------------------------------------------------- |
| `OPEN`               | TCP connection succeeded                          |
| `CLOSED`             | Connection was actively refused                   |
| `FILTERED / TIMEOUT` | No response was received before the timeout       |
| `ERROR`              | Another socket or operating-system error occurred |

### Why Can a Port Time Out?

A timeout does **not** necessarily mean that the port is closed.

For example:

```text
TCP SYN
   ↓
Target / Firewall
   ↓
No response
   ↓
Timeout
```

A firewall or network filter may silently drop the connection attempt.

On the other hand, a closed TCP port may actively reject the connection:

```text
TCP connection attempt
        ↓
      Target
        ↓
   Connection refused
        ↓
      CLOSED
```

PortLens therefore keeps `CLOSED` and `FILTERED / TIMEOUT` as separate states.

## DNS Resolution

PortLens uses Python's built-in:

```python
socket.gethostbyname()
```

to resolve a domain name to an IPv4 address.

For example:

```text
scanme.nmap.org
       ↓
     DNS
       ↓
IPv4 address
       ↓
TCP port scanning
```

If the domain cannot be resolved, PortLens displays:

```text
Could not resolve target: example.invalid
```

and stops the scan.

### Current DNS Limitation

The current implementation resolves the target to a **single IPv4 address**.

IPv6 and multiple-address handling are not currently supported.

## Multithreading

PortLens uses Python's `threading` module to scan multiple ports concurrently.

```text
Port 20 ─┐
Port 21 ─┤
Port 22 ─┼──→ Concurrent scanning
Port 23 ─┤
Port 24 ─┘
```

Because scans run concurrently, results may not appear in numerical port order.

## Timeout Handling

Each socket has a **1-second connection timeout**:

```python
sock.settimeout(1)
```

This prevents the scanner from waiting indefinitely for a response.

## Supported Services

PortLens currently recognizes common services based on their standard port numbers:

| Port | Service                     |
| ---- | --------------------------- |
| 21   | FTP                         |
| 22   | SSH                         |
| 23   | Telnet                      |
| 25   | SMTP                        |
| 53   | DNS                         |
| 80   | HTTP                        |
| 110  | POP3                        |
| 143  | IMAP                        |
| 443  | HTTPS                       |
| 3306 | MySQL                       |
| 5432 | PostgreSQL                  |
| 8080 | HTTP Proxy / Alternate HTTP |

Ports not present in the service mapping are displayed as `Unknown service`.

> Service identification is based on the port number. It does not verify the actual application running on the port.

## Requirements

* Python 3.x
* No external Python packages required

## Installation

Clone the repository:

```bash
git clone https://github.com/randomlyexisted/PortLens.git
```

Navigate to the project directory:

```bash
cd PortLens
```

Run PortLens:

```bash
python scanner.py -t 127.0.0.1 -s 1 -e 100
```

## Learning Goals

This project is being developed to learn and practice:

* Python networking
* TCP/IP fundamentals
* DNS resolution
* Socket programming
* Port scanning concepts
* Service identification
* Multithreading
* Error handling
* Command-line interfaces
* Git and GitHub
* Cybersecurity fundamentals

## Disclaimer

PortLens is intended for educational purposes and authorized security testing only.

Only scan systems and networks that you own or have explicit permission to test.
