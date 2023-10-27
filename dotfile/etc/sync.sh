#!/bin/sh -x

rsync -a /etc/pacman.conf pacman.conf
rsync -a /etc/pacman.d/mirrorlist pacman.d/mirrorlist
rsync -a /etc/pacman.d/hooks/ pacman.d/hooks
rsync -a /etc/system76-scheduler/ system76-scheduler
rsync -a /etc/systemd/system/bluetooth-disable-before-sleep.service systemd/system/
rsync -a /etc/systemd/system/intel-gpu-frequency.service systemd/system/
rsync -a /etc/systemd/system/kdump*.service systemd/system/
rsync -a /etc/mkinitcpio* .
rsync -a /etc/environment .
rsync -a /etc/default/grub default/
rsync -a /etc/tlp.d/ tlp.d
rsync -a /etc/modprobe.d/ modprobe.d
rsync -a /etc/docker/daemon.json docker/daemon.json
sudo rsync -a /etc/sudoers.d .
sudo chown taoky:taoky -R ./sudoers.d
