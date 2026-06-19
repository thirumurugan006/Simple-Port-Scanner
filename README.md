# Simple Port Scanner

A Python-based network scanning tool that detects open TCP ports and identifies common services running on a target host. This project demonstrates the use of socket programming for basic network reconnaissance and security assessment.

## Features

* Scan target IP addresses or domain names
* Detect open TCP ports
* Identify common network services
* Display scan results in real time
* Measure total scan duration
* Lightweight and easy to use

## Technologies Used

* Python 3
* Socket Programming
* Datetime Module

## Installation

1. Clone the repository:

```bash
git clone https://github.com/thirumurugan006/Simple-Port-Scanner.git
cd Simple-Port-Scanner
```

2. Ensure Python 3 is installed:

```bash
python --version
```

## Usage

Run the program:

```bash
python port_scanner.py
```

Enter a target IP address or domain name when prompted.

Example:

```text
Enter Target IP or Domain: scanme.nmap.org
```

## Sample Output

```text
==================================================
        SIMPLE PORT SCANNER
==================================================
Enter Target IP or Domain: scanme.nmap.org

Scanning Target: scanme.nmap.org
IP Address: 45.33.xxx.xxx
--------------------------------------------------
[OPEN] Port 22    --> SSH
[OPEN] Port 80    --> HTTP
--------------------------------------------------
Total Open Ports Found: 2
Time Taken   : 0:00:03.124567
```

## Learning Outcomes

* TCP/IP Networking Fundamentals
* Socket Programming in Python
* Port Enumeration Techniques
* Network Reconnaissance Concepts
* Basic Cybersecurity Assessment

## Future Enhancements

* Multithreaded scanning
* Custom port range selection
* Banner grabbing
* Service version detection
* CSV report generation
* GUI using Tkinter
* Network subnet scanning

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Always obtain permission before scanning systems that you do not own or manage.

## Author

**Thirumurugan**

B.E. Computer Science and Engineering (Cyber Security)

GitHub: https://github.com/your-username
