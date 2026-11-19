import re
from collections import defaultdict
from datetime import datetime

LOG_FILE = "auth.log"
ALERT_THRESHOLD = 3
TIME_WINDOW_SECONDS = 60
LOG_YEAR = 2026
def classify_severity(failed_count):
    if failed_count >= 5:
        return "HIGH"
    elif failed_count >= ALERT_THRESHOLD:
        return "MEDIUM"
    return "LOW"
failed_attempts = defaultdict(list)
targeted_users = defaultdict(set)
successful_logins = defaultdict(list)

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

        if timestamp and (failed or accepted):
            event_time = datetime.strptime(
                f"{LOG_YEAR} {timestamp.group(1)}",
                "%Y %b %d %H:%M:%S"
            )

            if failed:
                username, ip = failed.groups()
                failed_attempts[ip].append(event_time)
                targeted_users[ip].add(username)

            elif accepted:
                username, ip = accepted.groups()
                successful_logins[ip].append(event_time)

print("\n===== SECURITY MONITORING REPORT =====")

print("\nFAILED LOGIN ATTEMPTS:")
for ip, events in failed_attempts.items():
    print(f"{ip}: {len(events)} failed attempts")

print("\nSUCCESSFUL LOGINS:")
for ip, events in successful_logins.items():
    print(f"{ip}: {len(events)} successful logins")

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

            severity = classify_severity(len(window)) 
            print(f"[{severity}] {ip}: {len(window)} failed attempts")
            print(f"       Within {TIME_WINDOW_SECONDS} seconds")
            print(f"       Targeted usernames: {users}")
            break

if not alerts_found:
    print("No time-based suspicious patterns detected.")

print("\nPOSSIBLE ACCOUNT COMPROMISE:")

compromise_found = False

for ip, failed_events in failed_attempts.items():
    for failed_time in failed_events:
        for successful_time in successful_logins.get(ip, []):
            time_difference = (
                successful_time - failed_time
            ).total_seconds()

            if 0 < time_difference <= TIME_WINDOW_SECONDS:
                print(
                    f"[HIGH] {ip}: Successful login occurred "
                    f"{int(time_difference)} seconds after a failed login."
                )
                compromise_found = True
                break

        if compromise_found:
            break

if not compromise_found:
    print("No matching failed-login and successful-login IP patterns detected.")

print("\n===== INVESTIGATION COMPLETE =====")

