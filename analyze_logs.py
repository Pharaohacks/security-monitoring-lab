import re
from collections import defaultdict
from datetime import datetime

LOG_FILE = "auth.log"
ALERT_THRESHOLD = 3
TIME_WINDOW_SECONDS = 60

failed_attempts = defaultdict(list)
targeted_users = defaultdict(set)
successful_logins = defaultdict(int)

with open(LOG_FILE, "r") as file:
    for line in file:
        timestamp = re.search(
            r"(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})", line
        )

        failed = re.search(
            r"Failed password for (\S+) from ([\d.]+)", line
        )

        accepted = re.search(
            r"Accepted password for (\S+) from ([\d.]+)", line
        )

        if failed and timestamp:
            username, ip = failed.groups()
            event_time = datetime.strptime(
                "2026 " + timestamp.group(1), "%Y %b %d %H:%M:%S"
            )
            failed_attempts[ip].append(event_time)
            targeted_users[ip].add(username)

        elif accepted:
            username, ip = accepted.groups()
            successful_logins[ip] += 1

print("\n===== SECURITY MONITORING REPORT =====")

print("\nFAILED LOGIN ATTEMPTS:")
for ip, events in failed_attempts.items():
    print(f"{ip}: {len(events)} failed attempts")

print("\nSUCCESSFUL LOGINS:")
for ip, count in successful_logins.items():
    print(f"{ip}: {count} successful logins")

print("\nTIME-BASED SECURITY ALERTS:")

alerts_found = False

for ip, events in failed_attempts.items():
    events.sort()

    for start in range(len(events)):
        window = [
            event for event in events
            if 0 <= (event - events[start]).total_seconds()
            <= TIME_WINDOW_SECONDS
        ]

        if len(window) >= ALERT_THRESHOLD:
            alerts_found = True
            users = ", ".join(sorted(targeted_users[ip]))

            print(f"[HIGH] {ip}: {len(window)} failed attempts")
            print(f"       Within {TIME_WINDOW_SECONDS} seconds")
            print(f"       Targeted usernames: {users}")
            break

if not alerts_found:
    print("No time-based suspicious patterns detected.")

print("\n===== INVESTIGATION COMPLETE =====")
