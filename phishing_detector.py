import re

SUSPICIOUS_KEYWORDS = [
    "verify your account", "urgent action required", "confirm your password",
    "click here immediately", "your account has been suspended",
    "unusual activity detected", "claim your prize", "act now",
    "limited time offer", "update your payment information"
]

SUSPICIOUS_DOMAINS = ["bit.ly", "tinyurl.com", "shorturl.at", "is.gd", "t.co"]

URGENT_WORDS = ["urgent", "immediately", "now", "warning", "alert", "suspended", "locked", "verify"]

def check_email(sender, subject, body):
    print("\n" + "=" * 55)
    print("   PHISHING EMAIL DETECTOR — CYBER ASCENSION OS")
    print("=" * 55)

    score = 0
    flags = []

    print("\n[SENDER ANALYSIS]")
    if "@" in sender:
        domain = sender.split("@")[1]
        print("  Domain: " + domain)
        if any(susp in domain for susp in ["-", "secure", "verify", "account"]):
            score += 2
            flags.append("Suspicious sender domain (contains security buzzwords)")
    else:
        score += 1
        flags.append("Malformed sender address")

    print("\n[SUBJECT ANALYSIS]")
    print("  Subject: " + subject)
    subject_lower = subject.lower()
    for word in URGENT_WORDS:
        if word in subject_lower:
            score += 1
            flags.append("Urgency keyword in subject: '" + word + "'")

    print("\n[BODY ANALYSIS]")
    body_lower = body.lower()
    for phrase in SUSPICIOUS_KEYWORDS:
        if phrase in body_lower:
            score += 2
            flags.append("Suspicious phrase found: '" + phrase + "'")

    print("\n[LINK ANALYSIS]")
    urls = re.findall(r'https?://[^\s]+', body)
    if urls:
        for url in urls:
            print("  Found URL: " + url)
            for domain in SUSPICIOUS_DOMAINS:
                if domain in url:
                    score += 3
                    flags.append("Shortened/suspicious link detected: " + url)
    else:
        print("  No links found")

    if "click here" in body_lower and urls:
        score += 1
        flags.append("Generic 'click here' link text — common phishing tactic")

    print("\n" + "=" * 55)
    print("[ANALYSIS RESULTS]")
    if flags:
        for flag in flags:
            print("  [!] " + flag)
    else:
        print("  [OK] No red flags detected")

    print("\n[RISK SCORE]: " + str(score))
    if score == 0:
        verdict = "LOW RISK"
    elif score <= 3:
        verdict = "MEDIUM RISK"
    else:
        verdict = "HIGH RISK - LIKELY PHISHING"

    print("[VERDICT]: " + verdict)
    print("=" * 55)


print("\n=== PHISHING EMAIL DETECTOR ===")
print("Paste email details below\n")

sender = input("Sender email address: ")
subject = input("Subject line: ")
print("Email body (paste full text, then type END on its own line):")

body_lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    body_lines.append(line)

body = "\n".join(body_lines)

check_email(sender, subject, body)
