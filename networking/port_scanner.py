import socket
from datetime import datetime

def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "unknown"

def scan_ports(target, start_port, end_port):
    print(f"\n=== PORT SCANNER ===")
    print(f"Target: {target}")
    print(f"Scanning ports {start_port}-{end_port}")
    print(f"Started: {datetime.now()}\n")
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            service = get_service(port)
            print(f"[OPEN] Port {port} — {service}")
            open_ports.append(port)
        sock.close()
    
    print(f"\nScan complete. {len(open_ports)} open ports found.")

target = input("Enter target IP or domain: ")
start = int(input("Start port: "))
end = int(input("End port: "))
scan_ports(target, start, end)
