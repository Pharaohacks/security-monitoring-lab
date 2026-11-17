import re
from collections import defaultdict

LOG_FILE = "auth.log"
ALERT_THRESHOLD = 3

failed_attempts = defaultdict(int)
targeted_users = defaultdict(set)
successful_logins = defaultdict(int)

with open(LOG_FILE, "r") as file:
    for line in file:
        failed = re.search(
            r"Failed password for (\S+) from ([\d.]+)", line
        )

        accepted = re.search(
            r"Accepted password for (\S+) from ([\d.]+)", line
        )

        if failed:
            username, ip = failed.groups()
            failed_attempts[ip] += 1
            targeted_users[ip].add(username)

        elif accepted:
            username, ip = accepted.groups()
            successful_logins[ip] += 1

print("\n===== SECURITY MONITORING REPORT =====")

print("\nFAILED LOGIN ATTEMPTS:")
for ip, count in failed_attempts.items():
    print(f"{ip}: {count} failed attempts")

print("\nSUCCESSFUL LOGINS:")
for ip, count in successful_logins.items():
    print(f"{ip}: {count} successful logins")

print("\nSECURITY ALERTS:")
alerts_found = False

for ip, count in failed_attempts.items():
    if count >= ALERT_THRESHOLD:
        alerts_found = True
        users = ", ".join(sorted(targeted_users[ip]))
        print(f"[ALERT] {ip} generated {count} failed attempts.")
        print(f"        Targeted usernames: {users}")

if not alerts_found:
    print("No suspicious login patterns detected.")

print("\n===== INVESTIGATION COMPLETE =====")
