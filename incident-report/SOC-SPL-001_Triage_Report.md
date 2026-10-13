# SOC Incident Triage Record

**Incident ID:** SOC-SPL-001

**Incident Title:** Suspected Multi-Stage Web Application Attack and Account Misuse

**SIEM Platform:** Splunk Enterprise

**Incident Date:** 12 October 2026

**Priority:** High (simulated lab)

**Investigation Status:** Initial triage completed — simulated escalation recommended

**Affected Application:** Customer Portal (Synthetic Lab)

**Suspicious Source IP:** 198.51.100.77

**Affected Account:** admin

## Incident Summary

It was observed that a simulated source IP generated repeated HTTP 404 responses, attempted SQL injection and path traversal, and performed seven failed authentication attempts against the admin account.

A successful authentication was subsequently recorded at 10:23 AM, followed by access to a sensitive customer export endpoint at 10:25 AM.

At 10:27 AM, a separate network log recorded approximately 8.11 MiB of outbound traffic from the web server to an external destination.

## SOC Analyst Assessment

The authentication and sensitive resource access sequence is suspicious and warrants further investigation.

The outbound network flow occurred shortly afterward, but the available evidence does not establish a causal relationship or confirm data exfiltration.

The activity was generated for an authorized SOC training exercise. No real-world compromise or data loss is claimed.

## Recommended Response Actions

1. Validate the affected administrator account and authentication history.
2. Review authentication sessions and source IP activity.
3. Investigate the export endpoint and its access records.
4. Examine web-server process and outbound connection telemetry.
5. Confirm whether the outbound destination and data transfer were authorized.
6. Consider temporary session revocation or IP blocking if malicious activity is confirmed in a real environment.
7. Escalate the correlated evidence to SOC Tier 2 for deeper investigation.

**Triage Decision:** Simulated escalation to SOC Tier 2.

**Final Disposition:** Authorized synthetic attack simulation; no confirmed real-world compromise.