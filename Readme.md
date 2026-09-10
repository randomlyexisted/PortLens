# PortLens

A simple Python-based TCP port scanner built as a cybersecurity learning project.

## Current Version

**v0.6.0 — CLI Interface**

## Features

* Scan a target IP address
* Scan a range of TCP ports
* Identify open and closed ports
* Identify common services based on port numbers
* Scan multiple ports concurrently using multithreading
* Set a connection timeout for each port
* Handle common socket errors
* Command-line interface using Python's `argparse`
* Support both short and long command-line options
* Display `Unknown service` for unrecognized ports

## Usage

PortLens uses command-line arguments instead of interactive prompts.

### Basic Command

```bash
python scanner.py -t 127.0.0.1 -s 1 -e 100
```

### Long-form Arguments

```bash
python scanner.py --target 127.0.0.1 --start-port 1 --end-port 100
```

### Arguments

| Argument | Long Form      | Description              |
| -------- | -------------- | ------------------------ |
| `-t`     | `--target`     | Target IP address        |
| `-s`     | `--start-port` | Starting port            |
| `-e`     | `--end-port`   | Ending port              |
| `-h`     | `--help`       | Display help information |

All three scanning arguments (`target`, `start-port`, and `end-port`) are required.

## Help

To view the available options:

```bash
python scanner.py --help
```

Example:

```text
usage: scanner.py [-h] -t TARGET -s START_PORT -e END_PORT

PortLens - A simple TCP port scanner

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target IP address
  -s START_PORT, --start-port START_PORT
                        Starting port
  -e END_PORT, --end-port END_PORT
                        Ending port
```

## Example Output

```text
Port 21 is CLOSED
Port 22 is OPEN → SSH
Port 23 is CLOSED
Port 80 is OPEN → HTTP
Port 443 is OPEN → HTTPS
```

> The order of results may vary because multiple ports are scanned concurrently.

## How It Works

PortLens uses Python's built-in `socket` module to attempt TCP connections to each port in the specified range.

Each socket has a **1-second connection timeout**.

PortLens handles different connection results separately:

| Result               | Meaning                                           |
| -------------------- | ------------------------------------------------- |
| `OPEN`               | TCP connection succeeded                          |
| `CLOSED`             | Connection was actively refused                   |
| `FILTERED / TIMEOUT` | Connection attempt timed out                      |
| `ERROR`              | Another socket or operating-system error occurred |

For open ports, PortLens checks a predefined port-to-service mapping to provide a likely service name.

## Multithreading

PortLens uses Python's `threading` module to scan multiple ports concurrently.

Each port is assigned to a separate thread:

```text
Port 20 ─┐
Port 21 ─┤
Port 22 ─┼──→ Concurrent scanning
Port 23 ─┤
Port 24 ─┘
```

This allows PortLens to perform multiple connection attempts without waiting for each port to finish before starting the next one.

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
