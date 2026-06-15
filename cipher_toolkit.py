import base64

def caesar_cipher(text, shift, decode=False):
    if decode:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def rot13(text):
    return caesar_cipher(text, 13)

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception as e:
        return f"Error: {e}"

def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def menu():
    print("\n=== CIPHER TOOLKIT — CYBER ASCENSION OS ===")
    print("1. Caesar Cipher Encode")
    print("2. Caesar Cipher Decode")
    print("3. ROT13")
    print("4. Base64 Encode")
    print("5. Base64 Decode")
    print("6. XOR Cipher")
    print("0. Exit")

while True:
    menu()
    choice = input("\nChoose an option: ")

    if choice == "0":
        print("Goodbye.")
        break
    elif choice == "1":
        text = input("Enter text: ")
        shift = int(input("Enter shift (1-25): "))
        print("\nResult:", caesar_cipher(text, shift))
    elif choice == "2":
        text = input("Enter text: ")
        shift = int(input("Enter shift (1-25): "))
        print("\nResult:", caesar_cipher(text, shift, decode=True))
    elif choice == "3":
        text = input("Enter text: ")
        print("\nResult:", rot13(text))
    elif choice == "4":
        text = input("Enter text: ")
        print("\nResult:", base64_encode(text))
    elif choice == "5":
        text = input("Enter base64 text: ")
        print("\nResult:", base64_decode(text))
    elif choice == "6":
        text = input("Enter text: ")
        key = input("Enter XOR key: ")
        result = xor_cipher(text, key)
        print("\nResult (raw):", result)
        print("Result (base64 for safe display):", base64.b64encode(result.encode('utf-8', errors='replace')).decode())
    else:
        print("Invalid option.")
