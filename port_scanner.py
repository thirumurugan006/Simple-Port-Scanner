import socket
from datetime import datetime

# Common ports and services
services = {
    20: "FTP Data",
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
    3389: "RDP"
}

print("=" * 50)
print("        SIMPLE PORT SCANNER")
print("=" * 50)

target = input("Enter Target IP or Domain: ")

try:
    # Convert domain name to IP
    target_ip = socket.gethostbyname(target)

    print("\nScanning Target:", target)
    print("IP Address:", target_ip)
    print("-" * 50)

    start_time = datetime.now()

    open_ports = []

    # Scan ports 1 to 1024
    for port in range(1, 1025):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.5)

        result = scanner.connect_ex((target_ip, port))

        if result == 0:
            service = services.get(port, "Unknown Service")
            open_ports.append((port, service))
            print(f"[OPEN] Port {port:<5} --> {service}")

        scanner.close()

    end_time = datetime.now()

    print("-" * 50)

    if len(open_ports) == 0:
        print("No open ports found.")
    else:
        print(f"Total Open Ports Found: {len(open_ports)}")

    print("Scan Started :", start_time.strftime("%H:%M:%S"))
    print("Scan Finished:", end_time.strftime("%H:%M:%S"))
    print("Time Taken   :", end_time - start_time)

except socket.gaierror:
    print("Error: Hostname could not be resolved.")

except socket.error:
    print("Error: Could not connect to server.")

except KeyboardInterrupt:
    print("\nScan interrupted by user.")

except Exception as e:
    print("Unexpected Error:", e)
