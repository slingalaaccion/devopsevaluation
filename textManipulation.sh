#!/bin/bash

# Extract IP addresses
ip_addresses=$(awk '{print $1}' access.log)

# Count occurrences of each IP address
ip_counts=$(echo "$ip_addresses" | tr ' ' '\n' | sort | uniq -c | sort -nr)

# Print top 10 IP addresses
echo "Top 10 IP Addresses:"
head -n 10 <<< "$ip_counts" | awk '{print $2}'