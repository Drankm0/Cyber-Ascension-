import psutil

SUSPICIOUS_KEYWORDS = [
    "keylog", "spy", "hook", "keystroke"
]

WHITELIST = [
    "keyboardservicesd", "thermalmonitord", "cameracaptured",
    "continuitycaptureagent", "spotify", "notion", "chrome",
    "brave", "code helper", "python", "icdd", "crashpad"
]

def is_whitelisted(name, cmd):
    name_lower = name.lower()
    cmd_lower = cmd.lower()
    for safe in WHITELIST:
        if safe in name_lower or safe in cmd_lower:
            return True
    return False

def scan_processes():
    print("\n=== KEYLOGGER DETECTOR v2 ===")
    print("Scanning running processes...\n")

    flagged = []

    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            name = proc.info['name'].lower()
            cmdline = ' '.join(proc.info['cmdline'] or []).lower()

            if is_whitelisted(proc.info['name'], cmdline):
                continue

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
        print("[✓] Clean. No keyloggers detected.")

    print(f"Total processes scanned: {len(list(psutil.process_iter()))}")

scan_processes()
