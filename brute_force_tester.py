import hashlib
import itertools
import string
import time

def hash_password(password, algo="md5"):
    if algo == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()

def dictionary_attack(target_hash, wordlist, algo="md5"):
    print(f"\n[*] Starting dictionary attack...")
    print(f"[*] Target hash: {target_hash}")
    print(f"[*] Algorithm: {algo}")
    print(f"[*] Wordlist size: {len(wordlist)} words\n")

    start = time.time()
    for word in wordlist:
        attempt = hash_password(word, algo)
        if attempt == target_hash:
            elapsed = time.time() - start
            print(f"[+] PASSWORD FOUND: '{word}'")
            print(f"[+] Time taken: {elapsed:.4f} seconds")
            return word
    elapsed = time.time() - start
    print(f"[-] Password not found in wordlist")
    print(f"[-] Time taken: {elapsed:.4f} seconds")
    return None

def brute_force_attack(target_hash, max_length, charset, algo="md5"):
    print(f"\n[*] Starting brute force attack...")
    print(f"[*] Target hash: {target_hash}")
    print(f"[*] Max length: {max_length}")
    print(f"[*] Charset: {charset}")
    print(f"[*] WARNING: This can take a long time for length > 4\n")

    start = time.time()
    attempts = 0
    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            attempt = ''.join(combo)
            attempts += 1
            if hash_password(attempt, algo) == target_hash:
                elapsed = time.time() - start
                print(f"[+] PASSWORD FOUND: '{attempt}'")
                print(f"[+] Attempts: {attempts}")
                print(f"[+] Time taken: {elapsed:.4f} seconds")
                return attempt
            if attempts % 100000 == 0:
                print(f"    ...{attempts} attempts so far")

    elapsed = time.time() - start
    print(f"[-] Password not found")
    print(f"[-] Attempts: {attempts}")
    print(f"[-] Time taken: {elapsed:.4f} seconds")
    return None

COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "abc123", "monkey",
    "letmein", "dragon", "111111", "baseball", "iloveyou", "trustno1",
    "sunshine", "master", "welcome", "shadow", "ashley", "football",
    "jesus", "michael", "ninja", "mustang", "password1", "admin",
    "zion", "houston", "texas", "decipher"
]

def menu():
    print("\n=== BRUTE FORCE / HASH CRACKER — CYBER ASCENSION OS ===")
    print("EDUCATIONAL USE ONLY — test your own passwords")
    print("\n1. Hash a password (see what the hash looks like)")
    print("2. Dictionary attack (built-in common passwords list)")
    print("3. Brute force attack (try every combination)")
    print("0. Exit")

while True:
    menu()
    choice = input("\nChoose an option: ")

    if choice == "0":
        print("Goodbye.")
        break

    elif choice == "1":
        pw = input("Enter password to hash: ")
        algo = input("Algorithm (md5/sha256): ").lower() or "md5"
        print(f"\n{algo.upper()} hash: {hash_password(pw, algo)}")

    elif choice == "2":
        pw = input("Enter a password to test (we'll hash it): ")
        algo = input("Algorithm (md5/sha256): ").lower() or "md5"
        target = hash_password(pw, algo)
        dictionary_attack(target, COMMON_PASSWORDS, algo)

    elif choice == "3":
        pw = input("Enter a SHORT password to test (1-4 chars recommended): ")
        algo = input("Algorithm (md5/sha256): ").lower() or "md5"
        target = hash_password(pw, algo)
        max_len = int(input("Max length to try (recommend 4 or less): "))
        charset_choice = input("Charset - (1) lowercase letters (2) lowercase+digits: ")
        if charset_choice == "2":
            charset = string.ascii_lowercase + string.digits
        else:
            charset = string.ascii_lowercase
        brute_force_attack(target, max_len, charset, algo)

    else:
        print("Invalid option.")
