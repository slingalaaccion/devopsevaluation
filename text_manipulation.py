from collections import Counter

def analyze_access_log(log_file):
    """
    Analyzes an access log file and prints the top 10 IP addresses with the most requests.

    Args:
        log_file: Path to the access log file.
    """
    ip_addresses = []

    with open(log_file, 'r') as f:
        for line in f:
            ip_address = line.split()[0]
            ip_addresses.append(ip_address)

    ip_counts = Counter(ip_addresses)
    top_10_ips = ip_counts.most_common(10)

    print("Top 10 IP Addresses:")
    for ip, count in top_10_ips:
        print(f"{ip}")

if __name__ == "__main__":
    log_file_path = "access.log"  # Replace with the actual path to your log file
    analyze_access_log(log_file_path)