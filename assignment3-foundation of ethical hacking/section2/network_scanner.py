# Basic Network Port Scanner (Rewritten)


import socket
import time

# Ask the user for the target IP address
target = input("Enter target IP: ")

# Ask the user for the ports to scan
# Example input: 21 22 80
ports_input = input("Enter ports (space separated): ")
ports = [int(port) for port in ports_input.split()]

# Start the timer
start_time = time.time()

# File where scan results will be saved
output_file = "scanresults.txt"

print("\nScanning started...\n")

# Open the file in write mode
with open(output_file, "w") as file:
    file.write(f"Scan results for {target}\n")
    file.write("--------------------------\n")

    # Loop through each port
    for port in ports:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Wait at most 1 second for a response
        sock.settimeout(1)

        # Try connecting to the target and port
        result = sock.connect_ex((target, port))

        # Port is open if connect_ex returns 0
        if result == 0:
            message = f"Port {port} is OPEN"
        else:
            message = f"Port {port} is CLOSED"

        # Show result on screen and save to file
        print(message)
        file.write(message + "\n")

        # Close the socket after checking the port
        sock.close()

    # Stop the timer after all ports are scanned
    end_time = time.time()
    duration = end_time - start_time

    file.write("--------------------------\n")
    file.write(f"Scan duration: {duration:.2f} seconds\n")

print("\nScan completed ")
print(f"Time taken: {duration:.2f} seconds")
print(f"Results saved in {output_file} ")


