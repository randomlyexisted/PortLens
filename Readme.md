# PortLens

A simple TCP port scanner written in Python.

PortLens is a cybersecurity and networking learning project that is being developed incrementally, with each version adding a new capability.

## Current Version

### v0.2.0 — Port Ranges

Version 0.2.0 extends the basic TCP scanner from scanning a single port to scanning a range of TCP ports.

### Features

* Accepts a target IP address
* Accepts a starting port
* Accepts an ending port
* Scans every port within the specified range
* Reports whether each port is open or closed
* Uses Python's built-in `socket` module
* Requires no external Python packages

## Requirements

* Python 3.x
* No external dependencies

## Usage

Run the scanner with:

```bash
python scanner.py
```

The program will ask for:

```text
Enter target IP:
Enter starting port:
Enter ending port:
```

Example:

```text
Enter target IP: 127.0.0.1
Enter starting port: 20
Enter ending port: 25

Port 20 is CLOSED
Port 21 is CLOSED
Port 22 is OPEN
Port 23 is CLOSED
Port 24 is CLOSED
Port 25 is OPEN
```

## How It Works

PortLens creates a TCP socket for each port in the specified range and attempts to establish a connection.

```text
Target IP
    |
    v
Starting Port ──→ Ending Port
    |
    v
Scan each port
    |
    v
TCP connection attempt
    |
   +---+---+
   |       |
Success  Failure
   |       |
   v       v
 OPEN    CLOSED
```

## Project Structure

```text
PortLens/
├── scanner.py
├── README.md
├── LICENSE
└── .gitignore
```

## Learning Goals

Through this version, I practiced:

* Python socket programming
* TCP connections
* IP addresses and ports
* Python `range()`
* Iterating through port ranges
* Exception handling
* Proper socket cleanup
* Basic network reconnaissance
* Git and GitHub workflow

## Disclaimer

PortLens is intended for **educational purposes and authorized security testing only**.

Only scan systems, networks, and devices that you own or have explicit permission to test.
