# PortLens

A simple TCP port scanner written in Python.

PortLens is a cybersecurity and networking learning project that is being developed incrementally, with each version adding a new capability.

## Current Version

### v0.1.0 — Basic TCP Scanner

The first version focuses on the fundamentals of TCP port scanning.

### Features

- Accepts a target IP address
- Accepts a TCP port
- Attempts a TCP connection to the specified port
- Reports whether the port is open or closed
- Uses Python's built-in `socket` module
- Requires no external Python packages

## Requirements

- Python 3.x
- No external dependencies

## Usage

Run the scanner with:

```bash
python scanner.py
```

The program will ask for a target IP address and port.

Example:

```text
Enter target IP: 127.0.0.1
Enter port: 80
Port 80 is OPEN
```

For a port that cannot be connected to:

```text
Enter target IP: 127.0.0.1
Enter port: 9999
Port 9999 is CLOSED
```

## How It Works

PortLens creates a TCP socket and attempts to connect to the specified target and port.

```text
Target IP + Port
       |
       v
Create TCP Socket
       |
       v
Attempt TCP Connection
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

This version was built to practice:

- Python socket programming
- TCP connections
- IP addresses and ports
- Exception handling
- Basic network reconnaissance
- Git and GitHub workflow

## Disclaimer

PortLens is intended for **educational purposes and authorized security testing only**.

Only scan systems, networks, and devices that you own or have explicit permission to test.
