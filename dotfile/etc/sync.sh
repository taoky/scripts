#!/bin/bash

if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root." >&2
    exit 1
fi

set -x

rsync -a /etc/pacman.conf pacman.conf
rsync -a /etc/pacman.d/mirrorlist pacman.d/mirrorlist
rsync -a --delete /etc/pacman.d/hooks/ pacman.d/hooks
rsync -a --delete /etc/system76-scheduler/ system76-scheduler
rsync -a /etc/systemd/system/*.service.d systemd/system/
rsync -a /etc/systemd/system/*.slice.d systemd/system/
rsync -a /etc/systemd/system/bluetooth-disable-before-sleep.service systemd/system/
rsync -a /etc/systemd/system/intel-gpu-frequency.service systemd/system/
rsync -a /etc/systemd/system/kdump*.service systemd/system/
rsync -a /etc/systemd/user/slice.d systemd/user/
rsync -a --delete /etc/mkinitcpio* .
rsync -a /etc/environment .
rsync -a /etc/default/grub default/
rsync -a --delete /etc/tlp.d/ tlp.d
rsync -a --delete /etc/modules-load.d/ modules-load.d
rsync -a /etc/docker/daemon.json docker/daemon.json
rsync -a --delete /etc/snapper/ snapper
rsync -a /etc/subgid subgid
rsync -a /etc/subuid subuid
rsync -a /etc/NetworkManager/conf.d/dns.conf NetworkManager/conf.d/
rsync -a /etc/nix/nix.conf nix/nix.conf
rsync -a --delete /etc/sudoers.d .
chown taoky:taoky -R ./sudoers.d ./snapper ./mkinitcpio.d ./modules-load.d ./pacman.d
