# MITRE ATT&CK Mapping — Splunk SOC Lab

**Project:** Splunk Multi-Stage Attack Detection & Incident Response Lab

**Incident ID:** SOC-SPL-001

**Data Source:** Synthetic web, authentication and network logs

## Detection-to-Technique Mapping

| Detection | ATT&CK Technique | Technique ID | Evidence Assessment |
|---|---|---|---|
| Web Reconnaissance | Active Scanning | T1595 | Repeated unsuccessful requests suggest endpoint enumeration |
| SQL Injection / Path Traversal | Exploit Public-Facing Application | T1190 | Web exploitation attempts observed; success not confirmed |
| Brute-Force Authentication | Brute Force | T1110 | Seven failed admin login attempts |
| Suspicious Login After Failures | Valid Accounts | T1078 | Candidate behavior only; unauthorized credential use unconfirmed |
| Sensitive Resource Access | Not conclusively mapped | — | HTTP 200 response; collection or data disclosure unconfirmed |
| Unusual Outbound Traffic | Not conclusively mapped | — | Large network transfer; exfiltration technique unconfirmed |

## Investigation Summary

The simulated attack began with endpoint reconnaissance, followed by web exploitation attempts and repeated authentication failures.

A successful administrator login occurred after the failed attempts. A sensitive export endpoint was subsequently accessed, followed by an unusually large outbound network flow.

Splunk Enterprise was used to correlate the available events, reconstruct their timeline and identify activity requiring investigation.

## Limitations

- The dataset is synthetic and does not represent an actual compromise.
- The HTTP 403 responses do not establish successful exploitation.
- Successful authentication does not establish unauthorized credential use.
- Access to the export endpoint does not establish successful data extraction.
- The outbound network event is temporally related but cannot be causally attributed to the suspicious source using the current evidence.

## References

- MITRE ATT&CK: https://attack.mitre.org/
- T1595: https://attack.mitre.org/techniques/T1595/
- T1190: https://attack.mitre.org/techniques/T1190/
- T1110: https://attack.mitre.org/techniques/T1110/
- T1078: https://attack.mitre.org/techniques/T1078/