# Simple Security Audit Script
# Performs basic port scanning, checks for common vulnerabilities,
# and generates an HTML report

import socket
from datetime import datetime

# Get target IP from user
target = input("Enter target IP: ")

# Ports to scan
ports = [21, 22, 80, 443]

# Service mapping
services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

# Basic vulnerability database
vulnerabilities = {
    "FTP": "Anonymous login may be enabled",
    "SSH": "Weak passwords may allow brute-force attacks",
    "HTTP": "Possible XSS or outdated server",
    "HTTPS": "SSL/TLS configuration should be verified"
}

results = []

print("\nStarting scan...\n")

# Scan each port
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        service = services.get(port, "Unknown")
        vuln = vulnerabilities.get(service, "No known issues")

        print(f"Port {port} is OPEN ({service})")

        results.append({
            "port": port,
            "service": service,
            "vulnerability": vuln
        })
    else:
        print(f"Port {port} is CLOSED")

    sock.close()

# Generate HTML report
filename = "security_report.html"

with open(filename, "w") as file:
    file.write("<html><head><title>Security Report</title></head><body>")
    file.write(f"<h2>Security Audit Report for {target}</h2>")
    file.write(f"<p>Date: {datetime.now()}</p>")
    file.write("<table border='1'>")
    file.write("<tr><th>Port</th><th>Service</th><th>Vulnerability</th></tr>")

    for entry in results:
        file.write(
            f"<tr><td>{entry['port']}</td>"
            f"<td>{entry['service']}</td>"
            f"<td>{entry['vulnerability']}</td></tr>"
        )

    file.write("</table>")
    file.write("</body></html>")

print("\nScan complete")
print(f"Report saved as {filename}")