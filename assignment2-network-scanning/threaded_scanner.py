import threading
import os

# function to run ping
def ping(ip):
    print(f"Scanning {ip}...")
    os.system(f"ping -c 1 {ip} > /dev/null")

# list of IPs (you can change range)
ips = ["127.0.0.1", "8.8.8.8", "1.1.1.1"]

threads = []

# create threads
for ip in ips:
    t = threading.Thread(target=ping, args=(ip,))
    threads.append(t)
    t.start()

# wait for all threads
for t in threads:
    t.join()

print("\nScanning completed using multi-threading!")
