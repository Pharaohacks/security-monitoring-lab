
# Security Monitoring & Incident Investigation Lab

## Overview

A Python-based cybersecurity project that analyzes simulated SSH authentication logs, detects suspicious login activity, and generates alerts to support security monitoring and incident investigation.

## Technologies Used

- Python 3
- Regular Expressions
- Linux/Unix Authentication Logs
- Git & GitHub

## Project Features

- Parses SSH authentication events.
- Extracts usernames and source IP addresses.
- Tracks failed and successful login attempts.
- Detects repeated authentication failures.
- Identifies time-based brute-force activity.
- Correlates failed login attempts with subsequent successful logins.
- Assigns automated severity levels to suspicious activity.
- Generates security alerts.
- Documents investigation findings and recommended mitigation steps.

## Project Structure

| File | Description |
|---|---|
| `analyze_logs.py` | Python security log analyzer |
| `auth.log` | Simulated SSH authentication events |
| `incident_report.md` | Security investigation report |

## Detection Results

The analyzer identified suspicious authentication activity in the sample dataset.

### Finding 1
- Source IP: `185.220.101.5`
- Failed attempts: 4
- Targeted usernames: `admin`, `root`
- Severity: Medium

### Finding 2
- Source IP: `45.33.12.8`
- Failed attempts: 3
- Targeted username: `test`
- Severity: Medium

The analyzer also evaluates authentication activity within configurable time windows to identify potential brute-force attempts and suspicious login patterns.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Pharaohacks/security-monitoring-lab.git
   ```

2. Enter the project directory:

   ```bash
   cd security-monitoring-lab
   ```

3. Run the analyzer:

   ```bash
   python3 analyze_logs.py
   ```

## Project Purpose

This project demonstrates practical cybersecurity skills in log analysis, authentication monitoring, brute-force detection, incident investigation, and Python scripting.
# Security Monitoring & Incident Investigation Lab

## Overview
A Python-based cybersecurity project that analyzes simulated SSH authentication logs, detects repeated failed login attempts, and generates alerts for suspicious activity.

## Technologies Used
- Python 3
- Regular Expressions
- Linux/Unix Authentication Logs
- Git & GitHub

## Project Features
- Parses SSH authentication events.
- Extracts usernames and source IP addresses.
- Tracks failed and successful login attempts.
- Detects repeated authentication failures.
- Generates automated security alerts.
- Documents investigation findings and recommended mitigation steps.

## Project Structure

| File | Description |
|---|---|
| `analyze_logs.py` | Python security log analyzer |
| `auth.log` | Simulated SSH authentication events |
| `incident_report.md` | Security investigation report |

## Detection Results

The analyzer identified two suspicious authentication patterns in the sample dataset:

- `185.220.101.5` — 4 failed login attempts targeting `admin` and `root`.
- `45.33.12.8` — 3 failed login attempts targeting `test`.

The alert threshold is configurable in the Python script.

## How to Run

1. Clone the repository
   git clone https://github.com/Pharaohacks/security-monitoring-lab.git
2.  Enter the project directory
   cd security-monitoring-lab
 3. Run the analyzer
    python3 analyze_logs.py


Run the analyzer:

```bash
python3 analyze_logs.py
```

## Skills Demonstrated
- Python scripting
- Security log analysis
- Authentication monitoring
- Suspicious activity detection
- Basic incident triage
- Technical documentation

## Disclaimer
This project uses simulated authentication logs for educational purposes. The listed IP addresses have not been independently verified as malicious.
