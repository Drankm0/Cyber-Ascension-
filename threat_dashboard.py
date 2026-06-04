import psutil
import os
import time
from datetime import datetime

WHITELIST = [
    "kernel", "launchd", "spotlight", "finder", "dock",
    "safari", "chrome", "brave", "spotify", "notion",
    "code", "python", "iterm", "zsh", "bash", "windowserver",
    "coreaudiod", "cfprefsd", "useractivityd"
]

def clear():
    os.system('clear')

def is_suspicious_proc(name, cpu):
    for safe in WHITELIST:
        if safe in name.lower():
            return False
    return cpu > 10.0

def get_open_connections():
    suspicious = []
    try:
        for conn in psutil.net_connections():
            if conn.status == 'ESTABLISHED' and conn.raddr:
                ip = conn.raddr.ip
                if ip.startswith('fe80') or ip.startswith('127.') or ip.startswith('192.168'):
                    continue
                suspicious.append(f"{ip}:{conn.raddr.port}")
    except psutil.AccessDenied:
        return ["Run with sudo for network data"]
    return suspicious[:8]

def dashboard():
    while True:
        clear()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        print("=" * 55)
        print("   SYSTEM THREAT DASHBOARD — CYBER ASCENSION OS")
        print(f"   {now}")
        print("=" * 55)

        cpu_bar = "█" * int(cpu / 5) + "░" * (20 - int(cpu / 5))
        ram_pct = ram.percent
        ram_bar = "█" * int(ram_pct / 5) + "░" * (20 - int(ram_pct / 5))

        print(f"\n[SYSTEM HEALTH]")
        print(f"  CPU : [{cpu_bar}] {cpu}%")
        print(f"  RAM : [{ram_bar}] {ram_pct}%")
        print(f"  DISK: {disk.percent}% used ({disk.free // (1024**3)}GB free)")

        print(f"\n[SUSPICIOUS PROCESSES — CPU > 10%]")
        flagged = []
        for proc in psutil.process_iter(['name', 'cpu_percent', 'pid']):
            try:
                if is_suspicious_proc(proc.info['name'], proc.info['cpu_percent']):
                    flagged.append(proc.info)
            except:
                pass

        if flagged:
            for p in flagged[:5]:
                print(f"  [!] PID {p['pid']} | {p['name']} | CPU: {p['cpu_percent']}%")
        else:
            print("  [✓] No suspicious processes detected")

        print(f"\n[EXTERNAL CONNECTIONS]")
        conns = get_open_connections()
        if conns:
            for c in conns:
                print(f"  [!] {c}")
        else:
            print("  [✓] No suspicious external connections")

        threat = 0
        if cpu > 80: threat += 2
        if ram_pct > 85: threat += 1
        if flagged: threat += len(flagged)
        if conns: threat += len(conns)

        level = "LOW ✓" if threat < 3 else "MEDIUM ⚠" if threat < 6 else "HIGH ⚠⚠"
        print(f"\n[THREAT LEVEL] {level}")
        print("\n  Refreshing in 5 seconds... Ctrl+C to exit")
        print("=" * 55)

        time.sleep(5)

try:
    dashboard()
except KeyboardInterrupt:
    print("\n\nDashboard closed.")
