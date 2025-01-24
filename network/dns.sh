#!/bin/bash -e

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <local|nm>"
    exit 1
fi

SCRIPT_DIR=$(dirname "$(realpath "$0")")

case $1 in
    local)
        echo -e "search taoky.moe\nnameserver 127.0.0.1" > /etc/resolv.conf.local
        mv /etc/resolv.conf.local /etc/resolv.conf
        ;;
    nm)
        ln -sf /run/NetworkManager/resolv.conf /etc/resolv.conf
        ;;
    *)
        echo "Invalid argument: $1"
        exit 1
        ;;
esac
