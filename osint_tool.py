import socket
import subprocess
import sys
from datetime import datetime

def osint_lookup(target):
    print("\n" + "=" * 55)
    print(f"   OSINT TOOL — CYBER ASCENSION OS")
    print(f"   Target: {target}")
    print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)

    # IP Resolution
    print("\n[DNS LOOKUP]")
    try:
        ip = socket.gethostbyname(target)
        print(f"  IP Address : {ip}")
        hostname = socket.gethostbyaddr(ip)
        print(f"  Hostname   : {hostname[0]}")
    except Exception as e:
        print(f"  Error: {e}")

    # WHOIS
    print("\n[WHOIS]")
    try:
        result = subprocess.run(
            ["whois", target],
            capture_output=True, text=True, timeout=10
        )
        lines = [l for l in result.stdout.split('\n')
                 if any(k in l.lower() for k in
                 ['registrar', 'created', 'expires', 'country', 'name server', 'org'])]
        for line in lines[:8]:
            print(f"  {line.strip()}")
    except Exception as e:
        print(f"  Error: {e}")

    # Port Scan
    print("\n[QUICK PORT SCAN — Top Ports]")
    common_ports = {
        21:'FTP', 22:'SSH', 23:'Telnet', 25:'SMTP',
        80:'HTTP', 443:'HTTPS', 3306:'MySQL', 8080:'HTTP-Alt'
    }
    try:
        ip = socket.gethostbyname(target)
        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            status = "[OPEN]" if result == 0 else "[closed]"
            print(f"  {status} Port {port} — {service}")
            sock.close()
    except Exception as e:
        print(f"  Error: {e}")

    print("\n" + "=" * 55)

target = input("Enter domain or IP to investigate: ")
osint_lookup(target)
