#!/usr/bin/env python3
# zcat access.log.gz | awk '{print $1}' | python ip_count.py
import sys
from collections import defaultdict
from socket import inet_pton, inet_ntop, AF_INET, AF_INET6

IPV4_CIDR = 24
IPV6_CIDR = 48
IPV4_MAX = 32
IPV6_MAX = 128


def get_ip_prefix(ip: str) -> str:
    if ":" in ip:
        typ = AF_INET6
        suffix = IPV6_CIDR
        shift = IPV6_MAX - IPV6_CIDR
        bytelen = 16
    else:
        typ = AF_INET
        suffix = IPV4_CIDR
        shift = IPV4_MAX - IPV4_CIDR
        bytelen = 4
    ip = inet_pton(typ, ip)
    ip = int.from_bytes(ip, "big", signed=False) >> shift << shift
    address = inet_ntop(typ, int.to_bytes(ip, length=bytelen, byteorder="big")) + f"/{suffix}"
    return address


if __name__ == "__main__":
    cnts = defaultdict(int)
    for line in sys.stdin:
        net = get_ip_prefix(line.strip())
        cnts[net] += 1
    sorted_cnts = sorted(cnts.items(), key=lambda x: x[1], reverse=False)
    for i in sorted_cnts:
        print(i)
