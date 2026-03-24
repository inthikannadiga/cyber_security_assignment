#!/usr/bin/env python3

import os
import datetime

# logging function
def log(message):
    time = datetime.datetime.now().strftime("%H:%M:%S")
    with open("scan_log.txt", "a") as f:
        f.write(f"[{time}] {message}\n")

# ping scan
def ping_scan():
    ip = input("Enter IP: ")
    log(f"Ping scan started for {ip}")
    os.system(f"ping -c 2 {ip}")
    log(f"Ping scan completed for {ip}")

# arp scan
def arp_scan():
    log("ARP scan started")
    os.system("python3 arp_scanner.py")
    log("ARP scan completed")

# nmap scan
def nmap_scan():
    ip = input("Enter IP or range: ")
    log(f"Nmap scan started for {ip}")
    os.system(f"nmap {ip}")
    log(f"Nmap scan completed for {ip}")

# run all
def run_all():
    ip = input("Enter IP: ")
    log(f"Running all scans for {ip}")
    os.system(f"ping -c 2 {ip}")
    os.system("python3 arp_scanner.py")
    os.system(f"nmap {ip}")
    log(f"All scans completed for {ip}")

# main menu
def main():
    log("Program started")

    while True:
        print("\n===== Network Scanner =====")
        print("1. Ping Scan")
        print("2. ARP Scan")
        print("3. Nmap Scan")
        print("4. Run All Scans")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            ping_scan()
        elif choice == "2":
            arp_scan()
        elif choice == "3":
            nmap_scan()
        elif choice == "4":
            run_all()
        elif choice == "5":
            log("Program exited")
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
