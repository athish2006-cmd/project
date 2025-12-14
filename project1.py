import socket
import concurrent.futures
from datetime import datetime

target_host = input("Enter the target IP address: ")
print("-" * 50)
print(f"Scanning {target_host} with Multi-threading...")
print("-" * 50)

def scan_port(port):
    """
    Scans a single port and prints if it is open.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Timeout of 1 second
        result = s.connect_ex((target_host, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

# Start the timer
start_time = datetime.now()

# Using ThreadPoolExecutor to run scans in parallel
# max_workers=100 means we scan 100 ports at once
try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        # Scan ports 1 to 1024
        ports = range(1, 1025) 
        executor.map(scan_port, ports)

except KeyboardInterrupt:
    print("\nExiting...")

end_time = datetime.now()
print("-" * 50)
print(f"Scanning completed in: {end_time - start_time}")