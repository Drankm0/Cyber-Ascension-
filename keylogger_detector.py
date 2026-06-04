import psutil
import os

SUSPICIOUS_KEYWORDS = [
    "keylog", "logger", "spy", "hook", "capture",
    "pynput", "keyboard", "keystroke", "monitor"
]

def scan_processes():
    print("\n=== KEYLOGGER DETECTOR ===")
    print("Scanning running processes...\n")
    
    flagged = []
    
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            name = proc.info['name'].lower()
            cmdline = ' '.join(proc.info['cmdline'] or []).lower()
            
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in name or keyword in cmdline:
                    flagged.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'cmd': cmdline[:80]
                    })
                    break
        except:
            pass
    
    if flagged:
        print(f"[!] SUSPICIOUS PROCESSES FOUND: {len(flagged)}\n")
        for p in flagged:
            print(f"PID: {p['pid']} | Name: {p['name']}")
            print(f"CMD: {p['cmd']}\n")
    else:
        print("[✓] No suspicious processes detected.")
    
    print(f"\nTotal processes scanned: {len(list(psutil.process_iter()))}")

scan_processes()
