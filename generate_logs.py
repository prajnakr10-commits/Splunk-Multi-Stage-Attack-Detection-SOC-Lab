
import csv
from pathlib import Path
from datetime import datetime, timedelta

# Output directory
output = Path(__file__).resolve().parent / "datasets"
output.mkdir(exist_ok=True)

# Synthetic attack scenario
start = datetime(2026, 10, 12, 10, 0)
attacker_ip = "198.51.100.77"

def ts(minutes):
    return (start + timedelta(minutes=minutes)).strftime(
        "%Y-%m-%dT%H:%M:%S"
    )

def save_csv(name, fields, rows):
    with open(output / name, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

# WEB APPLICATION LOGS
web = []

for i in range(40):
    web.append({
        "timestamp": ts(i),
        "src_ip": "192.0.2.25",
        "method": "GET",
        "uri": ["/", "/products", "/about"][i % 3],
        "status": 200,
        "user": "guest"
    })

# Web reconnaissance
for i in range(8):
    web.append({
        "timestamp": ts(3 + i),
        "src_ip": attacker_ip,
        "method": "GET",
        "uri": f"/hidden-path-{i}",
        "status": 404,
        "user": "guest"
    })

# SQL injection and path traversal attempts
for minute, uri in [
    (12, "/product?id=1%20UNION%20SELECT"),
    (13, "/download?file=../../etc/passwd")
]:
    web.append({
        "timestamp": ts(minute),
        "src_ip": attacker_ip,
        "method": "GET",
        "uri": uri,
        "status": 403,
        "user": "guest"
    })

# Authentication event correlation
web.append({
    "timestamp": ts(25),
    "src_ip": attacker_ip,
    "method": "GET",
    "uri": "/admin/export/customers.csv",
    "status": 200,
    "user": "admin"
})

# AUTHENTICATION LOGS
auth = []

for i in range(7):
    auth.append({
        "timestamp": ts(15 + i),
        "src_ip": attacker_ip,
        "user": "admin",
        "action": "failure",
        "application": "customer_portal"
    })

auth.append({
    "timestamp": ts(23),
    "src_ip": attacker_ip,
    "user": "admin",
    "action": "success",
    "application": "customer_portal"
})

auth.append({
    "timestamp": ts(6),
    "src_ip": "192.0.2.25",
    "user": "alice",
    "action": "success",
    "application": "customer_portal"
})

# NETWORK FLOW LOGS
network = [
    {
        "timestamp": ts(27),
        "src_ip": "10.0.0.20",
        "dest_ip": "203.0.113.80",
        "dest_port": 443,
        "bytes_out": 8500000,
        "action": "allowed"
    },
    {
        "timestamp": ts(8),
        "src_ip": "10.0.0.20",
        "dest_ip": "203.0.113.10",
        "dest_port": 443,
        "bytes_out": 12000,
        "action": "allowed"
    }
]

save_csv(
    "web.csv",
    ["timestamp", "src_ip", "method", "uri", "status", "user"],
    web
)

save_csv(
    "auth.csv",
    ["timestamp", "src_ip", "user", "action", "application"],
    auth
)

save_csv(
    "network.csv",
    ["timestamp", "src_ip", "dest_ip", "dest_port",
     "bytes_out", "action"],
    network
)

print("Successfully generated synthetic security logs!")
print(f"Web events: {len(web)}")
print(f"Authentication events: {len(auth)}")
print(f"Network events: {len(network)}")
