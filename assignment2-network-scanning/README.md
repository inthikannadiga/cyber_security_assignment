# Network Scanning Automation

This project implements automated network scanning tools using Python. It performs basic network reconnaissance tasks such as host discovery, IP–MAC mapping, and network scanning using system utilities.

---

## 🚀 Features

* Ping Scanner (checks host availability)
* ARP Scanner (retrieves IP and MAC addresses)
* Nmap Scanner (performs network scanning)
* Unified Scanner (menu-based interface to run all tools)
* Export results to CSV format
* Network range scanning (e.g., 192.168.1.0/24)
* Multi-threaded scanning for faster execution
* Simple GUI using Tkinter
* Logging functionality with timestamps

---

## 📁 Project Structure

```
assignment2-network-scanning/
│
├── arp2.csv
├── arp_scanner.py
├── gui_scanner.py
├── main_scanner.py
├── nmap_scanner.py
├── ping_scanner.py
├── scan_log.txt
├── threaded_scanner.py
├── README.md
│
└── screenshots/
    ├── all_scans.png
    ├── arp_csv.png
    ├── arp_output.png
    ├── gui.png
    ├── logging_proof.png
    ├── menu.png
    ├── multithreading.png
    ├── nmap_output.png
    ├── ping_output.png
    └── range_scan.png
```

---

## 🛠 Requirements

* Python 3
* Nmap installed
* Kali Linux environment

---

## ▶️ How to Run

Run individual scanners:

```
python3 ping_scanner.py
python3 arp_scanner.py
python3 nmap_scanner.py
```

Run unified scanner:

```
python3 main_scanner.py
```

---

## 📊 Bonus Features Implemented

* CSV export of scan results
* Network range scanning using CIDR notation
* Multi-threaded scanning
* GUI interface using Tkinter
* Logging system using scan_log.txt

---

## 👩‍💻 Author

Tejaswini H L
