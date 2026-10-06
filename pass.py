import re

with open("passwords.txt", "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

for password in passwords:
    has_letter = re.search(r"[A-Za-z]", password)
    has_number = re.search(r"\d", password)
    has_special = re.search(r"[^A-Za-z0-9]", password)

    if has_letter and has_number and has_special:
        print("POLICY MATCH")