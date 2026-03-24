#!/usr/bin/env python3

import subprocess
import csv

def arp_scan():
    print("=" * 50)
    print("ARP Scanner")
    print("=" * 50)

    try:
        # Run arp-scan (active scan → guarantees output)
        result = subprocess.check_output(
            ["sudo", "arp-scan", "--localnet"],
            stderr=subprocess.DEVNULL
        ).decode()

        lines = result.split("\n")
        devices = []

        print("\nIP Address        | MAC Address")
        print("=" * 50)

        for line in lines:
            if "\t" in line:
                parts = line.split("\t")
                if len(parts) >= 2:
                    ip = parts[0]
                    mac = parts[1]

                    print(f"{ip:<17} | {mac}")
                    devices.append([ip, mac])

        print("=" * 50)
        print(f"Total: {len(devices)}")

        # Save to CSV
        choice = input("\nSave results to CSV? (y/n): ").lower()

        if choice == 'y':
            filename = input("Enter filename (default arp.csv): ") or "arp.csv"

            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["IP Address", "MAC Address"])
                writer.writerows(devices)

            print(f"Saved to {filename}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    arp_scan()
