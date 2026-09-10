# PortLens

A simple Python-based TCP port scanner built as a cybersecurity learning project.

## Current Version

**v0.5.0 — Timeouts + Error Handling**

## Features

* Scan a target IP address
* Scan a range of TCP ports
* Identify open and closed ports
* Identify common services based on port numbers
* Scan multiple ports concurrently using multithreading
* Set a connection timeout for each port
* Handle common socket errors
* Display `Unknown service` for unrecognized ports
* Simple command-line interface

## Example

```text
Enter target IP: 127.0.0.1
Enter starting port: 20
Enter ending port: 100

Port 22 is OPEN → SSH
Port 23 is CLOSED
Port 80 is OPEN → HTTP
```

> The order of results may vary because multiple ports are scanned concurrently.

## How It Works

PortLens uses Python's built-in `socket` module to attempt TCP connections to each port in the specified range.

Each socket has a **1-second connection timeout**. If a connection does not receive a response within the timeout period, PortLens reports:

```text
Port 445 is FILTERED / TIMEOUT
```

PortLens also handles different connection results separately:

| Result               | Meaning                                           |
| -------------------- | ------------------------------------------------- |
| `OPEN`               | TCP connection succeeded                          |
| `CLOSED`             | Connection was actively refused                   |
| `FILTERED / TIMEOUT` | Connection attempt timed out                      |
| `ERROR`              | Another socket or operating-system error occurred |

For open ports, PortLens checks a predefined port-to-service mapping to provide a likely service name.

## Supported Services

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

Ports that are not in the service list are displayed as `Unknown service`.

## Multithreading

Starting with v0.4.0, PortLens uses Python's `threading` module to scan multiple ports concurrently.

Instead of scanning ports one at a time:

```text
Port 20 → Port 21 → Port 22 → Port 23 → ...
```

multiple port scans can run concurrently:

```text
Port 20 ─┐
Port 21 ─┤
Port 22 ─┼──→ Concurrent scanning
Port 23 ─┤
Port 24 ─┘
```

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

Run the scanner:

```bash
python scanner.py
```

## Usage

When prompted, enter:

1. Target IP address
2. Starting port
3. Ending port

Example:

```text
Enter target IP: 127.0.0.1
Enter starting port: 1
Enter ending port: 100
```

## Learning Goals

This project is being developed to learn and practice:

* Python networking
* TCP/IP fundamentals
* Socket programming
* Port scanning concepts
* Service identification
* Multithreading
* Error handling
* Git and GitHub
* Cybersecurity fundamentals

## Disclaimer

PortLens is intended for educational purposes and authorized security testing only.

Only scan systems and networks that you own or have explicit permission to test.
