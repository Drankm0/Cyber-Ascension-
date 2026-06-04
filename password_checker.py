import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*]', password):
        score += 1

    if score == 5:
        print(f"Password strength: STRONG ✓ (score: {score}/5)")
    elif score >= 3:
        print(f"Password strength: MEDIUM ~ (score: {score}/5)")
    else:
        print(f"Password strength: WEAK ✗ (score: {score}/5)")

password = input("Enter a password to check: ")
check_password_strength(password)
