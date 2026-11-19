
# Security Monitoring Lab – Incident Report

## Executive Summary

A Python-based log analyzer was used to investigate simulated SSH authentication logs. The analyzer identified repeated authentication failures, time-based brute-force activity, and suspicious authentication sequences.

Three notable findings were identified:
- Two source IP addresses generated repeated failed login attempts.
- One source IP demonstrated a suspicious failed-to-successful login sequence.
- The highest severity alert involved a successful login occurring eight seconds after a failed attempt.

These findings demonstrate basic security monitoring, brute-force detection, authentication correlation, and incident investigation techniques.

## Finding 1 – Repeated SSH Authentication Failures

- **Source IP:** 185.220.101.5
- **Failed attempts:** 4
- **Targeted usernames:** admin, root
- **Severity:** Medium
- **Detection:** Four failed login attempts within 60 seconds.

### Recommended Mitigation
- Review authentication logs for additional suspicious activity.
- Verify whether the targeted accounts are legitimate.
- Enforce strong passwords and multi-factor authentication.
- Consider blocking the source IP if malicious activity is confirmed.

## Finding 2 – Repeated SSH Authentication Failures

- **Source IP:** 45.33.12.8
- **Failed attempts:** 3
- **Targeted username:** test
- **Severity:** Medium
- **Detection:** Three failed login attempts within 60 seconds.

### Recommended Mitigation
- Investigate the source of repeated authentication failures.
- Review the targeted account for unauthorized access.
- Implement account monitoring and authentication protections.

## Finding 3 – Suspicious Authentication Sequence

- **Source IP:** 203.0.113.50
- **Failed attempts:** 1
- **Successful logins:** 1
- **Time between events:** 8 seconds
- **Severity:** High
- **Detection:** A successful login occurred within 60 seconds after a failed login from the same source IP.

### Recommended Mitigation
- Investigate the successful login and verify whether it was authorized.
- Review the account's recent authentication history.
- Check for additional suspicious activity from the source IP.
- Consider resetting credentials if unauthorized access is suspected.

This sequence warrants investigation but does not independently establish account compromise.

## Detection Logic

The Python analyzer uses:

- Regular expressions to identify SSH authentication events.
- Timestamp parsing to establish event order.
- A 60-second detection window.
- A configurable threshold of three failed attempts.
- Failed-to-successful authentication correlation.
- Automated severity classification.

### Severity Classification

- **Low:** Fewer than three failed attempts.
- **Medium:** Three or more failed attempts within the detection window.
- **High:** A successful login occurs shortly after a failed login from the same source IP.

## Conclusion

This project demonstrates foundational security operations skills through Python-based log analysis, authentication monitoring, suspicious activity detection, and incident reporting.

The investigation highlights how authentication logs can be used to identify potential brute-force attempts and suspicious login behavior.
# Security Monitoring Lab – Incident Report

## Executive Summary

A Python-based log analyzer was used to investigate simulated SSH authentication logs. The analyzer identified two sources exhibiting repeated failed login attempts within a 60-second window and one source with a successful login occurring shortly after a failed attempt.

These findings demonstrate basic brute-force detection and suspicious authentication sequence correlation.

## Finding 1 – Repeated SSH Authentication Failures

- **Source IP:** 185.220.101.5
- **Failed attempts:** 4
- **Targeted usernames:** admin, root
- **Severity:** Medium
- **Detection:** Four failed login attempts within 60 seconds.

## Finding 2 – Repeated SSH Authentication Failures

- **Source IP:** 45.33.12.8
- **Failed attempts:** 3
- **Targeted username:** test
- **Severity:** Medium
- **Detection:** Three failed login attempts within 60 seconds.

## Finding 3 – Suspicious Authentication Sequence

- **Source IP:** 203.0.113.50
- **Failed attempts:** 1
- **Successful logins:** 1
- **Time between events:** 8 seconds
- **Severity:** High
- **Detection:** A successful login occurred within 60 seconds after a failed login from the same IP.

This sequence warrants investigation but does not independently establish account compromise.

## Detection Logic

The Python analyzer uses:
- Regular expressions to identify SSH authentication events.
- Timestamp parsing to establish event order.
- A 60-second detection window.
- A configurable threshold of three failed attempts.
- Automated severity classification:
  - Low: Fewer than three failures.
  - Medium: Three or four failures.
  - High: Five or more failures.
- Correlation of failed and successful logins from the same IP address.

A separate high-severity alert identifies successful authentication shortly after a failed attempt.

## Recommendations

1. Review authentication activity associated with flagged IP addresses.
2. Enable multi-factor authentication.
3. Implement SSH rate limiting and account lockout protections where appropriate.
4. Review successful login events following repeated authentication failures.
5. Centralize authentication logs for ongoing monitoring.

## Limitations

- All authentication events in this lab are simulated.
- The IP addresses are test data and have not been verified as malicious.
- The analyzer does not inspect live network traffic.
- A failed login followed by a successful login does not prove an account was compromised.
- Severity thresholds are demonstration rules, not a production security standard.

## Conclusion

This project demonstrates foundational security monitoring capabilities, including log parsing, time-based brute-force detection, authentication event correlation, and automated severity classification using Python.

The results are intended for educational and portfolio demonstration purposes.
