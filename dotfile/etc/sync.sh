#!/bin/sh

rsync -a /etc/pacman.conf pacman.conf
rsync -a /etc/pacman.d/mirrorlist pacman.d/mirrorlist
rsync -a /etc/system76-scheduler/ system76-scheduler
