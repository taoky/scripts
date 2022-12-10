#!/bin/sh -e

sudo mount /dev/disk/by-uuid/0E62-46C6 /efi
sudo grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB
sudo grub-mkconfig -o /boot/grub/grub.cfg
sudo umount /efi
