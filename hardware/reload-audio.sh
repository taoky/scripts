#!/bin/sh -x

# sof firmware does not work after hibernation
# this script reloads related kernel mod

sudo rmmod snd_sof_pci_intel_tgl
sudo modprobe snd_sof_pci_intel_tgl
