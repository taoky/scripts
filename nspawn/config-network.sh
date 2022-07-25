#!/bin/sh

sudo ip address add 192.168.233.1/24 dev ve-vlab-ubuntu
sudo ip link set ve-vlab-ubuntu up
