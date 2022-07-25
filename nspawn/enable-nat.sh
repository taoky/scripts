#!/bin/sh

sudo iptables -t nat -A POSTROUTING -s 192.168.233.2/24 -j MASQUERADE
sudo iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i ve-vlab-ubuntu -j ACCEPT
