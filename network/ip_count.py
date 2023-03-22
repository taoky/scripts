#!/usr/bin/env python3
# zcat access.log.gz | awk '{print $1}' | python ip_count.py
import ipaddress
import sys
from collections import defaultdict

IPV4_CIDR = 24
IPV6_CIDR = 48


def get_ip_prefix(ip: str) -> str:
    if ":" in ip:
        # IPv6
        suffix = f"/{IPV6_CIDR}"
    else:
        suffix = f"/{IPV4_CIDR}"
    network = ipaddress.ip_network(ip + suffix, strict=False)
    address = str(network.network_address) + suffix
    return address


if __name__ == "__main__":
    cnts = defaultdict(int)
    for line in sys.stdin:
        net = get_ip_prefix(line.strip())
        cnts[net] += 1
    sorted_cnts = sorted(cnts.items(), key=lambda x: x[1], reverse=False)
    for i in sorted_cnts:
        print(i)
