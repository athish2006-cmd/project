import socket
import sys
from datetime import datetime

# 1. Define the target
# You can change this to a specific IP like '192.168.1.1'
target_host = input("Enter the target IP address: ")

# 2. Add a pretty banner
print("-" * 50)
print(f"Scanning Target: {target_host}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    # 3. Scan ports 1 to 1024 (System Ports)
    for port in range(1, 1025):
        # Create a socket object (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a short timeout so we don't wait forever on closed ports
        socket.setdefaulttimeout(1)
        
        # Attempt to connect (returns 0 if successful)
        result = s.connect_ex((target_host, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()

print("-" * 50)
print("Scanning finished.")