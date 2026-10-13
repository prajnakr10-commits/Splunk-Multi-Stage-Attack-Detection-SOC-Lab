# SOC Incident Investigation & Response Report

**Incident ID:** SOC-SPL-001  
**Incident Title:** Suspected Multi-Stage Web Application Attack and Account Misuse  
**SIEM Platform:** Splunk Enterprise  
**Incident Date:** 12 October 2026  
**Severity:** High (Simulated Lab Priority)  
**Status:** Investigation Completed — Simulated Incident  
**Data Source:** Synthetic Web, Authentication and Network Logs

---

## 1. Executive Summary

A simulated multi-stage attack targeting a customer web application was investigated using Splunk Enterprise.

The observed activity included web reconnaissance, SQL injection and path traversal attempts, repeated authentication failures, a successful administrator login, sensitive resource access, and a subsequent large outbound network flow.

Six detection queries were developed to identify suspicious behaviors. Splunk searches were used to reconstruct the event timeline and investigate potential relationships between the observed activities.

The exercise demonstrated detection engineering, security event correlation, threat hunting, incident triage and incident response documentation.

## 2. Affected Assets

| Asset | Details |
|---|---|
| Application | Customer Portal (Synthetic) |
| Web Server | 10.0.0.20 |
| Suspicious Source | 198.51.100.77 |
| External Destination | 203.0.113.80 |
| Target Account | admin |
| SIEM Index | soc_attack_detection |

## 3. Incident Timeline

| Time | Activity | Evidence |
|---|---|---|
| 10:03–10:10 | Web Reconnaissance | Eight HTTP 404 responses |
| 10:12 | SQL Injection Attempt | UNION SELECT request, HTTP 403 |
| 10:13 | Path Traversal Attempt | Directory traversal request, HTTP 403 |
| 10:15–10:21 | Authentication Failures | Seven failed admin logins |
| 10:23 | Successful Authentication | Admin login from suspicious IP |
| 10:25 | Sensitive Resource Access | Customer export endpoint, HTTP 200 |
| 10:27 | Large Outbound Network Flow | 8.11 MiB outbound from web server |

## 4. Security Findings

### Finding 1 — Web Reconnaissance

The source IP generated eight HTTP 404 responses while requesting non-existing endpoints, indicating potential web directory enumeration.

### Finding 2 — Web Exploitation Attempts

The source submitted requests containing SQL injection and path traversal patterns. Both requests received HTTP 403 responses. Exploitation success was not established.

### Finding 3 — Suspicious Authentication Sequence

Seven failed login attempts were followed by a successful authentication against the admin account from the same source IP.

This sequence suggests possible password guessing followed by account access. Whether the credentials were used without authorization remains unconfirmed.

### Finding 4 — Sensitive Resource Access

A request to the customer export endpoint returned HTTP 200 shortly after the successful admin login.

The response indicates the endpoint was accessed successfully at the HTTP level. It does not confirm that sensitive information was extracted.

### Finding 5 — Unusual Outbound Network Flow

The web server generated an outbound connection involving approximately 8.11 MiB of transferred data.

The event occurred two minutes after sensitive endpoint access, but available logs do not prove the events were causally related or establish data exfiltration.

## 5. MITRE ATT&CK Mapping

| Technique | ID | Assessment |
|---|---|---|
| Active Scanning | T1595 | Consistent with endpoint enumeration |
| Exploit Public-Facing Application | T1190 | Exploitation attempts observed |
| Brute Force | T1110 | Repeated failed authentication |
| Valid Accounts | T1078 | Potential; unauthorized use not confirmed |

Sensitive resource access and outbound traffic require additional context before assigning specific collection or exfiltration techniques.

## 6. SOC Incident Triage

**Triage Priority:** High (Lab Scenario)

**Detection Assessment:** Positive identification of simulated suspicious behaviors.

**Actual Compromise:** Not established.

**Escalation Decision:** Simulated escalation to SOC Tier 2 for deeper analysis.

The combination of authentication activity, sensitive endpoint access, and outbound network traffic warrants investigation.

## 7. Recommended Incident Response

### Identification

Correlate the web, authentication and network events to establish the sequence and scope of suspicious activity.

### Containment

If unauthorized activity is validated in a production environment, consider revoking suspicious sessions, temporarily restricting malicious source IPs, and protecting the affected account.

### Eradication

If compromise is confirmed, investigate exploited weaknesses, address application vulnerabilities, rotate affected credentials and remove unauthorized access mechanisms.

### Recovery

Restore authorized access, verify application integrity and monitor the affected systems for recurring indicators.

### Lessons Learned

Improve authentication monitoring, administrative export logging, event correlation, outbound traffic visibility and baseline-based alert thresholds.

## 8. Investigation Limitations

- All events were generated for an authorized synthetic training exercise.
- A successful login does not prove an account compromise.
- HTTP 200 does not establish sensitive data disclosure.
- The outbound network event is not causally linked to the attacker using available evidence.
- The limited dataset is insufficient for establishing normal traffic baselines.

## 9. Final Conclusion

The Splunk SOC lab successfully demonstrated identification and correlation of suspicious activity across web application, authentication and network event sources.

The investigation produced six detection queries, a multi-stage incident timeline, a security monitoring dashboard, an incident triage assessment and response recommendations.

**Final Disposition:** Authorized simulated security incident; investigation completed with no confirmed real-world compromise or data loss.