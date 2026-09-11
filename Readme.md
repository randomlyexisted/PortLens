# PortLens

**PortLens** is a simple Python-based TCP port scanner built as a cybersecurity learning project.

The project is developed version-by-version, with each release adding a new concept or feature. The goal is to understand how port scanning works while gradually building a more useful command-line security tool.

## Current Version

**v0.8.0 — JSON/CSV Output**

## Features

- Target IP address scanning
- Domain name resolution
- Custom port ranges
- TCP port scanning
- Open, closed, and filtered/timeout states
- Basic service identification using common port numbers
- Multithreaded scanning
- Socket timeout handling
- Error handling
- Command-line arguments
- JSON output
- CSV output
- Sorted scan results

## Installation

Make sure Python 3.x is installed.

Clone the repository:

```bash
git clone <your-repository-url>
cd PortLens
```

No external Python packages are required.

## Usage

### Basic Scan

```bash
python scanner.py -t 127.0.0.1 -s 1 -e 100
```

### Scan a Domain

```bash
python scanner.py -t scanme.nmap.org -s 20 -e 100
```

### Save Results as JSON

```bash
python scanner.py -t 127.0.0.1 -s 20 -e 100 --json results.json
```

Example:

```json
[
    {
        "port": 22,
        "state": "OPEN",
        "service": "SSH"
    },
    {
        "port": 23,
        "state": "CLOSED",
        "service": ""
    },
    {
        "port": 80,
        "state": "OPEN",
        "service": "HTTP"
    }
]
```

### Save Results as CSV

```bash
python scanner.py -t 127.0.0.1 -s 20 -e 100 --csv results.csv
```

Example:

```csv
port,state,service
22,OPEN,SSH
23,CLOSED,
80,OPEN,HTTP
```

### Save Both JSON and CSV

```bash
python scanner.py -t 127.0.0.1 -s 20 -e 100 --json results.json --csv results.csv
```

### View Help

```bash
python scanner.py --help
```

## Result States

| State | Meaning |
|---|---|
| `OPEN` | A TCP connection to the port succeeded. |
| `CLOSED` | The target actively refused the TCP connection. |
| `FILTERED / TIMEOUT` | No response was received within the configured timeout. |
| `ERROR` | Another socket/OS error occurred. |

A `FILTERED / TIMEOUT` result does **not** necessarily mean that the port is closed. A firewall or network filter may silently drop the connection attempt.

## Service Identification

PortLens currently identifies services using a static mapping of common port numbers.

| Port | Service |
|---:|---|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |
| 8080 | HTTP Proxy / Alternate HTTP |

This is **port-based service identification**, not actual service detection. A later version will introduce banner grabbing to inspect what service is actually running.

## How v0.8.0 Works

```text
Target
  ↓
DNS Resolution
  ↓
Port Range
  ↓
Create Threads
  ↓
Scan Ports
  ↓
Create Result
  ↓
Store Results
  ↓
Sort by Port
  ↓
Terminal / JSON / CSV
```

Because multiple threads access the shared results list, a thread lock is used when adding results.

## Requirements

- Python 3.x
- Standard Python libraries only

Libraries currently used:

- `socket`
- `threading`
- `argparse`
- `json`
- `csv`


## Learning Goals

PortLens is being developed to learn practical cybersecurity and programming concepts, including:

- TCP/IP fundamentals
- TCP port scanning
- Python sockets
- DNS resolution
- Multithreading
- Exception handling
- Command-line interfaces
- JSON and CSV data handling
- Git and GitHub version control
- Basic security tooling development


## Disclaimer

PortLens is an educational project.

Only scan systems that you own or have explicit permission to scan. Unauthorized port scanning may violate laws, organizational policies, or terms of service.
