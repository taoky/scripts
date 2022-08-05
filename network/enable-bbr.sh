#!/bin/sh

sysctl -w net.core.default_qdisc=cake
sysctl -w net.ipv4.tcp_congestion_control=bbr
