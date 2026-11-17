# Security Incident Investigation Report

## Project
Security Monitoring & Incident Investigation Lab

## Investigation Type
SSH Authentication Failure Analysis

## Environment
Simulated authentication logs analyzed using Python.

## Executive Summary
The log analyzer identified two source IP addresses with repeated
SSH authentication failures exceeding the configured alert threshold
of three attempts.

## Findings

### Finding 1
- Source IP: 185.220.101.5
- Failed attempts: 4
- Targeted usernames: admin, root
- Severity: Medium
- Observation: Multiple authentication failures targeting
  privileged account names.

### Finding 2
- Source IP: 45.33.12.8
- Failed attempts: 3
- Targeted username: test
- Severity: Low
- Observation: Repeated authentication failures against one account.

## Successful Authentication Events
- 192.168.1.15: 1 successful login for jayce
- 192.168.1.20: 1 successful login for jayce

No evidence in this dataset links the successful logins
to the failed login activity.

## Recommended Actions
1. Review authentication logs for additional activity from flagged IPs.
2. Verify whether the targeted accounts are legitimate.
3. Enforce multi-factor authentication where supported.
4. Apply account lockout or rate-limiting policies.
5. Investigate further before blocking any IP address.

## Limitations
- Dataset contains simulated events.
- No live network traffic was analyzed.
- No evidence establishes that either source IP is malicious.
- Alert threshold is configured for demonstration purposes.

## Conclusion
The Python analyzer successfully identified repeated SSH
authentication failures and generated alerts for both source IPs.
The results demonstrate foundational security log analysis
and incident triage capabilities.
