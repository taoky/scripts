#!/bin/sh -e

pactl unload-module $(pactl list short modules | grep "sink_name=VirtualSpeaker" | cut -f1)
pactl unload-module $(pactl list short modules | grep "sink_name=VirtualMic" | cut -f1)

