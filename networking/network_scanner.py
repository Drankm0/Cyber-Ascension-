import subprocess

def scan_network(target):
    print(f"\n=== NETWORK SCANNER ===")
    print(f"Target: {target}")
    print(f"Scanning...\n")
    result = subprocess.run(
        ["nmap", "-sV", "--open", target],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)

target = input("Enter target IP or domain: ")
scan_network(target)
