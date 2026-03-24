import tkinter as tk
from tkinter import messagebox
import os

def run_ping():
    ip = entry.get()
    if ip:
        os.system(f"ping -c 2 {ip}")
    else:
        messagebox.showerror("Error", "Enter IP")

def run_arp():
    os.system("python3 arp_scanner.py")

def run_nmap():
    ip = entry.get()
    if ip:
        os.system(f"nmap {ip}")
    else:
        messagebox.showerror("Error", "Enter IP")

# window
root = tk.Tk()
root.title("Network Scanner")
root.geometry("300x200")

# label + input
tk.Label(root, text="Enter IP:").pack()
entry = tk.Entry(root)
entry.pack()

# buttons
tk.Button(root, text="Ping Scan", command=run_ping).pack(pady=5)
tk.Button(root, text="ARP Scan", command=run_arp).pack(pady=5)
tk.Button(root, text="Nmap Scan", command=run_nmap).pack(pady=5)

root.mainloop()
